from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict, Field

from ..common.amount import Amount
from ..receipts.___receipts import Receipt
from .airline import AirTicket
from .confirmations import ConfirmationInModels
from .deal import Deal
from .docs import DOCS
from .fraud_data import FraudData
from .metadata import Metadata
from .newpayment_method import PaymentMethodData
from .recipient import Recipient
from .transfer import Transfer


class NewPayment(BaseModel):
    """
    Create a new payment

    https://yookassa.ru/developers/api#create_payment
    """

    model_config = ConfigDict(
        use_enum_values=True,
        arbitrary_types_allowed=True,
    )

    amount: Amount
    description: str | None = Field(max_length=128, default=None)
    receipt: Receipt | None = None
    recipient: Recipient | None = None
    payment_token: str | None = None
    payment_method_id: str | None = None
    payment_method_data: PaymentMethodData | None = None
    confirmation: ConfirmationInModels
    save_payment_method: bool | None = None
    capture: bool | None = None
    client_ip: str | None = None
    metadata: Metadata | None = None
    airline: AirTicket | None = Field(None, description=DOCS.Payment.airline)
    transfers: Sequence[Transfer] | None = None
    deal: Sequence[Deal] | None = Field(None, description=DOCS.Payment.deal)
    fraud_data: FraudData | None = None
    merchant_customer_id: str | None = Field(
        None, max_length=200, description=DOCS.Payment.merchant_customer_id
    )
