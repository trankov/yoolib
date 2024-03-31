from collections.abc import Sequence

from isoworld.countries import CountriesA2

from pydantic import BaseModel, Field

from ..common.amount import Amount
from .definitions import (
    ReceiptAgentType,
    ReceiptMeasure,
    ReceiptPaymentMode,
    ReceiptPaymentSubject,
    ReceiptVatCode,
)
from .industry_details import ReceiptIndustryDetails
from .mark_code_info import ReceiptMarkCodeInfo
from .mark_quantity import ReceiptMarkQuantity
from .supplier import ReceiptSupplier


class ReceiptPaymentItem(BaseModel):
    """
    Товар или услуга в чеке.

    В общем случае, достаточно указать только `description` и `amount`.
    Обязательные поля `quantity` и `vat_code` имеют значения по умолчанию
    `1` и `NO_VAT` соответственно. Если ваши значения отличаются от
    дефолтных, их тоже нужно передать.
    """

    # Required
    description: str = Field(..., max_length=128)
    amount: Amount

    # Required with defaults
    quantity: float = Field(1)
    vat_code: ReceiptVatCode = ReceiptVatCode.NO_VAT

    # Optional
    payment_subject: ReceiptPaymentSubject | None
    payment_mode: ReceiptPaymentMode | None
    country_of_origin_code: CountriesA2 | None
    customs_declaration_number: str | None = Field(None, min_length=1, max_length=32)
    excise: str | None
    supplier: ReceiptSupplier | None
    agent_type: ReceiptAgentType | None
    mark_code_info: ReceiptMarkCodeInfo | None
    measure: ReceiptMeasure | None
    payment_subject_industry_details: Sequence[ReceiptIndustryDetails] | None
    product_code: str | None
    mark_mode: str | None = Field(None, description='Должен передавать "0"')
    mark_quantity: ReceiptMarkQuantity | None
