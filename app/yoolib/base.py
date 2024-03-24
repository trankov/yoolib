from functools import singledispatchmethod
from uuid import UUID

from . import models
from .builders import NewPaymentBuilder
from .client import YooClient, yoo_client
from .exceptions import YooError


class YooPayment:
    """
    A Payment object that provides high level access to the YooKassa API.

    Принимает
    - либо id платежа в виде строки или UUID;
    - либо объект `NewPayment` из `yoolib.schemas`.

    При инициализации делает запрос к API YooKassa и получает используемый
    в нём объект платежа (Payment). В случае, если передан id, запускается
    метод `get_payment`. Если передан объект `NewPayment`, платёж создаётся
    методом `create`. Результат ответа (объект Payment) хранится в атрибуте
    `state` в виде pydantic-схемы.

    Все методы, кроме `refund`, возвращают объект `Payment` и обновляют его
    в атрибуте `state`. Все методы, кроме `create`, используют аргументы
    из атрибута `state`, если они не переданы при вызове.

    ### Методы:
    - `get_payment`: получить из API YouKassa объект платежа
    - `create`: создать новый платеж

    Как правило, два описанных выше метода не вызываются вручную при работе
    с библиотекой, так как вызываются при инициализации объекта YooPayment.
    Тем не менее, если это необходимо, они доступны так же, как и остальные,
    без каких-либо ограничений.

    - `capture`: принять отложенный платеж
    - `cancel`: отменить платеж
    - `refund`: возврат платежа (не обновляет state и возвращает `RefundModel`

    ### Атрибуты:
    - `state`: объект `Payment` в актуальном состоянии
    - `client`: объект `YooClient`, используемый для данного экземпляра. Может
    быть использован для низкоуровневого доступа к API YooKassa напрямую.
    Его вызовы не обновляют атрибут `state` автоматически. Если вы его
    используете, вручную обновите `state` вызовом метода `get_payment()`,
    кроме случаев, когда вы используете `client.refund()`.

    ### NewPaymentBuilder:
    Для удобства можно использовать `YooPayment.builder`, который является
    псевдонимом для класса `yoolib2.builders.NewPaymentBuilder`.

    ### Пример создания нового платежа
    ```
    from yoolib2 import YooPayment

    new_payment = YooPayment.builder(
        amount=1200,
        merchant_email="merchant@email.tld"
    ).build_customer(
        customer_email="customer@email.tld",
        customer_full_name="Иван Иванов",
        customer_phone="+79123456789",
    ).build_transfers(
        account_id="123456789",
        fee_amount=60.55
    ).build_receipt(
        payment_mode="partial_prepayment",
    )

    if redirect_request == "link":
        new_payment = new_payment.make_confirmation_redirect(
            return_url="https://mysite.tld/success",
        )
    elif redirect_request == "modal":
        new_payment = new_payment.make_confirmation_embedded()

    payment = YooPayment(new_payment)

    print(payment.state.status == "pending")
    ```
    """

    _client: YooClient | None = None
    state: models.Payment

    def __init__(self, payment: str | UUID | models.NewPayment):
        self._post_init(payment)

    @singledispatchmethod
    def _post_init(self, payment_arg: str | UUID | models.NewPayment):
        raise NotImplementedError("Payment must be either str, UUID or NewPayment")

    @_post_init.register
    def _(self, payment_arg: str):
        try:
            _ = UUID(hex=payment_arg, version=4)
        except ValueError as err:
            raise YooError(f"Invalid payment id: {payment_arg}") from err #.as_status(422) from err
        self.get_payment(payment_arg)

    @_post_init.register
    def _create(self, payment_arg: UUID):
        self.get_payment(str(payment_arg))

    @_post_init.register
    def _(self, payment_arg: models.NewPayment):
        self.create(payment_arg)

    def get_payment(self, payment_id: str | None = None) -> models.Payment:
        """
        Get payment. If `payment_id` is not provided, the state's id will
        be used. Pass `payment_id` to get payment.
        """
        self.state = self.client.payment(payment_id or self.state.id)
        return self.state

    def create(self, new_payment: models.NewPayment) -> models.Payment:
        """
        Create a new payment from the provided `NewPayment` object.
        Use `NewPaymentBuilder` to create a `NewPayment` object convinently.
        """
        self.state = self.client.pay(new_payment)
        return self.state

    def capture(
        self, payment_id: str | None = None, amount: int | float | None = None
    ) -> models.Payment:
        """
        Capture payment. If `amount` is not provided, the state's amount will
        be used. Pass `amount` to partial capture of a payment.
        """
        amount_ = models.Amount(value=float(amount)) if amount else self.state.amount
        self.state = self.client.capture(
            payment_id=payment_id or self.state.id,
            amount=amount_,
        )
        return self.state

    def cancel(self, payment_id: str | None = None) -> models.Payment:
        """
        Cancel payment. If `payment_id` is not provided, the state's id will
        be used.
        """
        self.state = self.client.cancel(payment_id or self.state.id)
        return self.state

    def refund(
        self,
        payment_id: str | None = None,
        amount: int | float | None = None,
        source_shop_id: str | None = None,
    ) -> models.RefundModel:
        """
        Refund payment.

        If `amount` is not provided, the state's `income_amount`
        will be used. Pass `amount` to partial refund of a payment.

        If `source_shop_id` is not provided, the first `state`'s `transfers`'s
        `account_id` will be used. If no `transfers` are found, the None
        will be used at your own risk.

        Pass your custom `RefundRequest` object to `client.refund()` method
        for more complex usage.
        """
        amount_ = (
            models.Amount(value=float(amount)) if amount else self.state.income_amount
        )
        assert amount_
        sources = None
        if source_shop_id:
            sources = (
                models.refund.RefundSource(account_id=source_shop_id, amount=amount_),
            )
        else:
            _transfers = getattr(self.state, "transfers", None)
            if _transfers and len(_transfers):
                sources = (
                    models.refund.RefundSource(
                        account_id=self.state.transfers[0].get("account_id"),
                        amount=amount_,
                    ),
                )
        refund_request = models.RefundRequest(
            payment_id=payment_id or self.state.id,
            amount=amount_,
            description=f"Возврат {amount_.value} ₽ от Go&Guide",
            sources=sources,
        )
        return self.client.refund(refund_request=refund_request)

    @property
    def client(self) -> YooClient:
        if self._client is None:
            self._client = yoo_client()
        return self._client

    @classmethod
    @property
    def builder(cls) -> type[NewPaymentBuilder]:
        return NewPaymentBuilder
