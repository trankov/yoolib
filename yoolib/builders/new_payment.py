from collections.abc import Callable
from typing import Any, Self

from isoworld.currencies import CurrencyCode

from ..models.confirmations import PaymentConfirmationTypes
from ..models.payments.new_payment import NewPayment
from . import (
    amount as amount_builder,
    payment_method_data as payment_method_data_builder,
    recipient as recipient_builder,
)


class NewPaymentBuilder:
# pylint: disable=too-many-instance-attributes

    amount = None
    recipient = None
    payment_method_data = None

    add_amount = amount_builder.add_amount
    add_recipient = recipient_builder.add_recipient
    add_payment_method_data = payment_method_data_builder.add_payment_method_data

    def __init__(
        self,
        use_confirmation: PaymentConfirmationTypes = PaymentConfirmationTypes.EMBEDDED,
        confirmation_url: str = '',
        use_currency: CurrencyCode = CurrencyCode.RUB,
    ) -> None:
        self.use_currency = use_currency
        self.confirmation_url = confirmation_url
        self.use_confirmation = use_confirmation

    def add_simple_scope(
        self,
        amount: float | None = None,
        description: str | None = None,
        payment_token: str | None = None,
        payment_method_id: str | None = None,
        save_payment_method: bool | None = None,
        capture: bool | None = None,
        client_ip: str | None = None,
    ):
        if amount:
            self.add_amount(value=amount, currency=self.use_currency)
        self.description = description
        self.payment_token = payment_token
        self.payment_method_id = payment_method_id
        self.save_payment_method = save_payment_method
        self.capture = capture
        self.client_ip = client_ip

    def create(self) -> dict:
        return {
            'amount': self.amount,
            'recipient': self.recipient,
            'payment_method_data': self.payment_method_data,
        }
