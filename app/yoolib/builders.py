from decimal import Decimal
from typing import Self

from .models import common, confirmations, payments


class NewPaymentBuilder:
    amount_value: CompulsoryDecimal = CompulsoryDecimal()
    capture: bool = False
    description: str = ""
    merchant_email: str = ""
    metadata: dict = dict()
    save_payment_method: bool = False

    amount: common.Amount | None = None
    customer: common.Customer | None = None
    receipt: common.Receipt | None = None
    transfers: list[payments.Transfer] | None = None

    def __init__(
        self,
        amount: int | str | float | Decimal,
        description: str = "",
        merchant_email: str = "",
        metadata: dict[str, str] = dict(),
        capture: bool = False,
        save_payment_method: bool = False,
    ):
        self.amount_value = amount
        self.description = description
        self.merchant_email = merchant_email
        self.metadata = metadata
        self.capture = capture
        self.save_payment_method = save_payment_method

        self._build_amount()

    def _build_amount(self) -> Self:
        if not self.amount:
            self.amount = common.Amount(value=self.amount_value, currency="RUB")
        return self

    def build_customer(
        self,
        customer_email=None,
        customer_full_name=None,
        customer_inn=None,
        customer_phone=None,
    ) -> Self:
        if not self.customer:
            self.customer = common.Customer(
                email=customer_email,
                full_name=customer_full_name,
                inn=customer_inn,
                phone=customer_phone,
            )
        return self

    def build_receipt(
        self,
        tax_system_code=None,
        quantity: int = 1,
        payment_subject: common.PAYMENT_SUBJECT_TYPES = "service",
        payment_mode: common.PAYMENT_MODE_TYPES = "full_prepayment",
        customs_declaration_number=None,
        product_code=None,
    ) -> Self:
        if not self.receipt:
            assert self.amount and self.customer
            self.receipt = common.Receipt(
                tax_system_code=tax_system_code,
                customer=self.customer,
                items=[
                    common.PaymentItem(
                        amount=self.amount,
                        description=self.description,
                        quantity=f"{quantity}",
                        vat_code=common.VAT.NO_VAT,
                        payment_subject=payment_subject,
                        payment_mode=payment_mode,
                        customs_declaration_number=customs_declaration_number,
                        product_code=product_code,
                    )
                ],
            )
        return self

    def build_transfers(self, account_id, fee_amount) -> Self:
        if not account_id:
            raise YooError(
                "An account_id is required, nothing has been passed."
            ).as_status(400)
        assert self.amount
        self.transfers = [
            payments.Transfer(
                account_id=account_id,
                amount=self.amount,
                platform_fee_amount=common.Amount(value=fee_amount, currency="RUB"),
            )
        ]
        return self


    def pre_build(self) -> dict:
        """Build params with no confirmation, preparing for final make"""
        return dict(
            amount=self.amount,
            description=self.description,
            capture=self.capture,
            merchant_customer_id=self.merchant_email,
            receipt=self.receipt,
            transfers=self.transfers,
            save_payment_method=self.save_payment_method,
            metadata=payments.Metadata(self.metadata)(),
        )

    def make_confirmation_redirect(
        self, return_url: str, enforce=False
    ) -> payments.NewPayment:
        return payments.NewPayment(
            **self.pre_build(),
            confirmation=confirmations.ConfirmationRedirectInModel(
                enforce=enforce,
                return_url=return_url,
            ),  # type: ignore
        )

    def make_confirmation_embedded(self) -> payments.NewPayment:
        return payments.NewPayment(
            **self.pre_build(),
            confirmation=confirmations.ConfirmationEmbeddedInModel(),  # type: ignore
        )

    def make_confirmation_external(self) -> payments.NewPayment:
        return payments.NewPayment(
            **self.pre_build(),
            confirmation=confirmations.ConfirmationExternalInModel(),  # type: ignore
        )

    def make_confirmation_qr(self) -> payments.NewPayment:
        return payments.NewPayment(
            **self.pre_build(),
            confirmation=confirmations.ConfirmationQrInModel(),  # type: ignore
        )

    def make_confirmation_mobile_application(self, return_url: str) -> payments.NewPayment:
        return payments.NewPayment(
            **self.pre_build(),
            confirmation=confirmations.ConfirmationMobileApplicationInModel(
                return_url=return_url,
            ),  # type: ignore
        )
