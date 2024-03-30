from collections.abc import Sequence
from enum import StrEnum

from pydantic import BaseModel, Field

from .common import Customer, PaymentItem


class ReceiptRegistration(StrEnum):
    """
    Статус регистрации чека в онлайн-кассе.
    """

    pending = 'pending'
    succeeded = 'succeeded'
    canceled = 'canceled'


class Receipt(BaseModel):
    """
    Данные для формирования чека в онлайн-кассе (для соблюдения 54-ФЗ).
    https://yookassa.ru/developers/api#create_payment_receipt
    """

    customer: Customer | None
    items: Sequence[PaymentItem]
    tax_system_code: int | None = Field(ge=1, le=6)
