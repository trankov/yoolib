from collections.abc import Sequence

from pydantic import BaseModel, Field

from ..common.definitions import TaxSystemNumCode
from .definitions import ReceiptStatus, ReceiptType
from .industry_details import ReceiptIndustryDetails
from .operational_details import ReceiptOperationalDetails
from .payment_item import ReceiptPaymentItem
from .settlements import ReceiptSettlement


class Receipt(BaseModel):
    id: str = Field(..., description='Идентификатор чека в ЮKassa')
    type: ReceiptType = Field(..., description='Тип чека в онлайн-кассе')
    payment_id: str | None = Field(None, description='Идентификатор платежа')
    refund_id: str | None = Field(None, description='Идентификатор возврата')
    status: ReceiptStatus = Field(
        ..., description='Статус доставки данных для чека в онлайн-кассу'
    )
    fiscal_document_number: str | None = Field(
        None, description='Номер фискального документа'
    )
    fiscal_attribute: str | None = Field(
        None, description=(
            'Фискальный признак чека. Формируется фискальным накопителем '
            'на основе данных, переданных для регистрации чека.'
        )
    )
    registered_at: str | None = Field(
        None, description=(
            'Дата и время формирования чека в фискальном накопителе. '
            'Указывается в формате ISO 8601.'
        )
    )
    fiscal_provider_id : str | None = Field(
        None, description=(
            'Идентификатор чека в онлайн-кассе. Присутствует, если чек '
            'удалось зарегистрировать.'
        )
    )
    items: Sequence[ReceiptPaymentItem] = Field(
        ..., description='Список платежных данных max=100'
    )
    settlements: Sequence[ReceiptSettlement] | None
    on_behalf_of: str | None = Field(
        None,
        description=(
            'Идентификатор магазина, от имени которого нужно отправить чек. '
            'Выдается ЮKassa. Присутствует, если вы используете Сплитование платежей'
        )
    )
    tax_system_code: TaxSystemNumCode | None
    receipt_industry_details: Sequence[ReceiptIndustryDetails] | None
    receipt_operational_details: ReceiptOperationalDetails | None
