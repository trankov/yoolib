from collections.abc import Sequence

from pydantic import BaseModel

from ..common import Customer
from ..common.definitions import TaxSystemNumCode
from .industry_details import ReceiptIndustryDetails
from .operational_details import ReceiptOperationalDetails
from .payment_item import ReceiptPaymentItem


class PaymentReceipt(BaseModel):
    """
    Данные для формирования чека в онлайн-кассе (для соблюдения 54-ФЗ).
    https://yookassa.ru/developers/api#create_payment_receipt
    """

    # Mandatory
    items: Sequence[ReceiptPaymentItem]

    # Optional
    customer: Customer | None = None
    tax_system_code: TaxSystemNumCode | None = None
    receipt_industry_details: Sequence[ReceiptIndustryDetails] | None = None
    receipt_operational_details: ReceiptOperationalDetails | None = None
