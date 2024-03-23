from typing import Any, Literal, Sequence, TypeAlias

from enum import Enum

from pydantic import BaseModel, Field

from . import common, validators
from .confirmations import ConfirmationInModels, ConfirmationOutModels


class Recipient(BaseModel):
    """
    Получатель платежа
    https://yookassa.ru/developers/api#payment_object_recipient
    """

    account_id: str = Field(..., description="Идентификатор магазина в ЮKassa")
    gateway_id: str = Field(
        ...,
        description="Идентификатор субаккаунта. Используется для разделения "
        "потоков платежей в рамках одного аккаунта",
    )


# class Confirmation:
#     """
#     Выбранный способ подтверждения платежа. Присутствует, когда платеж ожидает
#     подтверждения от пользователя.
#     https://yookassa.ru/developers/payment-acceptance/getting-started/
#         payment-process#user-confirmation
#     """

#     class Embedded(BaseModel):
#         type: Literal["embedded"] = "embedded"
#         confirmation_token: str | None = Field(
#             ...,
#             description="Токен для инициализации платежного виджета ЮKassa. "
#             "https://yookassa.ru/developers/payment-acceptance/integration-scenarios/widget/basics",
#         )

#     class External(BaseModel):
#         type: Literal["external"] = "external"

#     class MobileApplication(BaseModel):
#         type: Literal["mobile_application"] = "mobile_application"
#         confirmation_url: str = Field(
#             default="mobile_application",
#             description="Диплинк на мобильное приложение, в котором "
#             "пользователь подтверждает платеж.",
#         )

#     class QRcode(BaseModel):
#         type: Literal["qr"] = Field("qr", description="Данные для генерации QR-кода.")
#         confirmation_data: str

#     class Redirect(BaseModel):
#         type: Literal["redirect"] = "redirect"
#         confirmation_url: str | None = Field(
#             None, description="Куда перенаправить для подтверждения оплаты"
#         )
#         enforce: bool | None = Field(
#             None,
#             description="Запрос на проведение платежа с аутентификацией по "
#             "3-D Secure. Будет работать, если оплату банковской картой вы "
#             "по умолчанию принимаете без подтверждения платежа пользователем. "
#             "В остальных случаях аутентификацией по 3-D Secure "
#             "будет управлять ЮKassa.",
#         )
#         return_url: str | None = Field(
#             default="",
#             description="URL, на который вернется пользователь после "
#             "подтверждения или отмены платежа на веб-странице. "
#             "Не более 2048 символов.",
#         )


class Metadata(validators.MetadataValidator):
    """
    For validation of dict passed to PaymentMetadata(value: dict)()

    Example:
    ```
    prop = PaymentMetadata({'order-id': 7364})
    # prop == {'order-id': 7364} (error didn't catched)

    prop = PaymentMetadata({'order-id': 7364})()
    # ValueError: All values must be UTF-8 strings
    ```

    Constraints:
      * Max 16 keys
      * Max 32 key lenght
      * Max 512 value length
      * Value must be UTF-8 string

    """

    def __init__(self, d: dict):
        self.update(d)

    def __call__(self):
        self.full_validation()
        return self


class Transfer(BaseModel):
    account_id: str = Field(
        ...,
        description="Идентификатор магазина, в пользу которого вы "
        "принимаете оплату. Выдается ЮKassa, отображается в разделе "
        "Продавцы личного кабинета (столбец shopId).",
    )
    amount: common.Amount = Field(
        ...,
        description="Сумма, которую необходимо перевести магазину. "
        "Комиссия за проданные товары и услуги, которая удерживается "
        "с магазина в вашу пользу.",
    )
    platform_fee_amount: common.Amount | None = None
    metadata: Metadata | None = None


class Payment(BaseModel):
    """
    Объект платежа (Payment) содержит всю информацию о платеже, актуальную
    на текущий момент времени. Он формируется при создании платежа и приходит
    в ответ на любой запрос, связанный с платежами.

    https://yookassa.ru/developers/api#payment_object

    """

    id: str = Field(..., description="Идентификатор платежа в ЮKassa")
    status: common.PAYMENT_STATUS_TYPES
    amount: common.Amount = Field(
        ...,
        description="Сумма платежа, которую получит магазин, — значение amount "
        "за вычетом комиссии ЮKassa.",
    )
    income_amount: common.Amount | None = Field(
        None,
        description="Описание транзакции (не более 128 символов), которое "
        "вы увидите в личном кабинете ЮKassa, а пользователь — при оплате.",
        example="Оплата заказа № 72 для user@yoomoney.ru",
    )
    description: str | None = Field(max_length=128, default="")
    recipient: Recipient | None = None
    payment_method: Any = Field(
        None,
        description="Время подтверждения платежа. Указывается по UTC и "
        "передается в формате ISO 8601.",
    )
    captured_at: str | None = Field(
        None,
        description="Время создания заказа. Указывается по UTC и передается"
        "в формате ISO 8601. Пример: 2017-11-03T11:52:31.827Z",
    )
    created_at: str | None = None
    expires_at: str | None = Field(
        None,
        description="Время, до которого вы можете бесплатно отменить "
        "или подтвердить платеж. В указанное время платеж в статусе "
        "waiting_for_capture будет автоматически отменен. Указывается "
        "по UTC и передается в формате ISO 8601. "
        "Пример: 2017-11-03T11:52:31.827Z",
    )
    confirmation: ConfirmationOutModels | None
    test: bool | None = Field(True, description="Признак тестовой операции")
    refunded_amount: common.Amount | None = Field(
        None,
        description="Сумма, которая вернулась пользователю. Присутствует, "
        "если у этого платежа есть успешные возвраты. Код валюты "
        "в формате ISO-4217. Должен соответствовать валюте субаккаунта "
        "(recipient.gateway_id), если вы разделяете потоки платежей, "
        "и валюте аккаунта (shopId в личном кабинете), если не разделяете. "
        "Признак оплаты заказа.",
    )
    paid: bool
    refundable: bool = Field(description="Возможность провести возврат по API")
    receipt_registration: Literal["pending", "succeeded", "canceled"] | None = Field(
        None,
        description="Статус доставки данных для чека в онлайн-кассу "
        "(pending, succeeded или canceled). Присутствует, если вы "
        "используете решение ЮKassa для работы по 54-ФЗ. ",
    )
    # Usage: metadata=PaymentMetadata(some_dict)()
    metadata: Metadata | None = None
    cancellation_details: common.CancellationDetails | None = None
    # https://yookassa.ru/developers/api#payment_object_authorization_details
    authorization_details: Any = None
    # https://yookassa.ru/developers/api#payment_object_transfers
    transfers: Any = None
    deal: Any = None
    merchant_customer_id: str | None = None
    context: str | None = None

    class Config:
        arbitrary_types_allowed = True
        use_enum_values = True


class NewPayment(BaseModel):
    """
    Create a new payment
    https://yookassa.ru/developers/api#create_payment

    """

    amount: common.Amount
    capture: bool | None = True
    client_ip: str | None = None
    confirmation: ConfirmationInModels
    description: str | None = Field(max_length=128, default=None)
    merchant_customer_id: str | None = Field(
        default=None,
        max_length=200,
        description="Идентификатор покупателя в вашей системе, например, "
        "электронная почта или номер телефона. Не более 200 символов. "
        "Присутствует, если вы хотите запомнить банковскую карту "
        "и отобразить ее при повторном платеже в виджете ЮKassa. "
        "https://yookassa.ru/developers/api#create_payment_merchant_customer_id",
    )
    metadata: Metadata | None = None
    payment_method_data: Any = None
    payment_method_id: str | None = None
    payment_token: str | None = None
    receipt: common.Receipt | None = None
    recipient: Recipient | None = None
    save_payment_method: bool | None = False
    transfers: Sequence[Transfer] | None = None
    deal: dict | None = Field(
        None,
        description="Данные о сделке, в составе которой проходит платеж. "
        "Необходимо передавать, если вы проводите Безопасную сделку. "
        "https://yookassa.ru/developers/api#create_payment_deal",
    )
    airline: dict | None = Field(
        None,
        description="Используется для продажи авиабилетов "
        "https://yookassa.ru/developers/api#create_payment_airline",
    )

    class Config:
        arbitrary_types_allowed = True
        use_enum_values = True
