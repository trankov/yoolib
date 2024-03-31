from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict, Field

from ..common import Amount, CancellationDetails, PaymentStatus
from ..receipts.___receipts import ReceiptRegistration
from .authorization_details import AuthorizationDetails
from .confirmations import ConfirmationOutModels
from .deal import Deal
from .docs import DOCS
from .metadata import Metadata
from .payment_method import PaymentMethods
from .recipient import Recipient
from .transfer import Transfer


class Payment(BaseModel):
    """
    Объект платежа (Payment) содержит всю информацию о платеже, актуальную
    на текущий момент времени. Он формируется при создании платежа и приходит
    в ответ на любой запрос, связанный с платежами.

    https://yookassa.ru/developers/api#payment_object
    """

    model_config = ConfigDict(
        use_enum_values=True,
        arbitrary_types_allowed=True,
    )

    id: str = Field(..., description=DOCS.Payment.id)
    status: PaymentStatus
    amount: Amount = Field(..., description=DOCS.Payment.amount)
    income_amount: Amount | None = Field(
        None,
        description=DOCS.Payment.income_amount,
        examples=['Оплата заказа № 72 для user@yoomoney.ru'],
    )
    description: str | None = Field('', max_length=128)
    recipient: Recipient | None = None
    payment_method: PaymentMethods | None = Field(
        None, description=DOCS.Payment.payment_method
    )
    captured_at: str | None = Field(None, description=DOCS.Payment.captured_at)
    created_at: str | None = None
    expires_at: str | None = Field(None, description=DOCS.Payment.expires_at)
    confirmation: ConfirmationOutModels | None
    test: bool | None = Field(True, description=DOCS.Payment.test)
    refunded_amount: Amount | None = Field(
        None, description=DOCS.Payment.refunded_amount
    )
    paid: bool
    refundable: bool = Field(description=DOCS.Payment.refundable)
    receipt_registration: ReceiptRegistration | None = Field(
        None, description=DOCS.Payment.receipt_registration
    )
    metadata: Metadata | None = None
    cancellation_details: CancellationDetails | None = None
    authorization_details: AuthorizationDetails | None = None
    transfers: Sequence[Transfer] | None = None
    deal: Deal | None = None
    merchant_customer_id: str | None = None
    # context: str | None = None
