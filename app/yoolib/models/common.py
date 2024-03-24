from enum import IntEnum

from typing import Literal, Sequence, TypeAlias

from pydantic import BaseModel, EmailStr, Field, validator, root_validator
from .iso3166 import CountryA2
from . import validators


class VAT(IntEnum):
    """
    Код ставки НДС
    https://yookassa.ru/developers/payment-acceptance/scenario-extensions/54fz/parameters-values#vat-codes
    """
    NO_VAT = 1
    RATE_0 = 2
    RATE_10 = 3
    RATE_20 = 4
    RATE_10_110 = 5
    RATE_20_120 = 6


# PaymentItem.payment_subject
PAYMENT_SUBJECT_TYPES: TypeAlias = Literal[
    "commodity",
    "excise",
    "job",
    "service",
    "gambling_bet",
    "gambling_prize",
    "lottery",
    "lottery_prize",
    "intellectual_activity",
    "payment",
    "agent_commission",
    "property_right",
    "non_operating_gain",
    "insurance_premium",
    "sales_tax",
    "resort_fee",
    "composite",
    "another",
]


# PaymentItem.payment_mode
PAYMENT_MODE_TYPES: TypeAlias = Literal[
    "full_prepayment",
    "partial_prepayment",
    "advance",
    "full_payment",
    "partial_payment",
    "credit",
    "credit_payment",
]


PAYMENT_STATUS_TYPES: TypeAlias = Literal[
    "pending", "waiting_for_capture", "succeeded", "canceled"
]



class CancellationDetails(BaseModel):
    """
    Кто принял решение об отмене транзакции

    https://yookassa.ru/developers/payment-acceptance/after-the-payment/
        declined-payments#cancellation-details-reason
    """

    party: Literal["yoo_money", "payment_network", "merchant"]
    reason: str


class Amount(BaseModel):
    """
    Сумма платежа.
    https://yookassa.ru/developers/api#payment_object_amount

    """

    currency: CountryA2.type_alias = CountryA2.type_enum.RUB
    value: float = 0.0

    @validator("currency")
    def currency_match_iso4217(cls, value):
        return validators.currency_match_iso4217(value)


class Customer(BaseModel):
    """
    Информация о пользователе
    https://yookassa.ru/developers/api#create_payment_receipt_customer

    """

    email: EmailStr | str | None = None
    full_name: str | None = Field(max_length=256)
    inn: str | None = Field(tip="If None, put passport in `full_name`")
    phone: str | None = None

    @validator("inn")
    def inn_conditions(cls, value):
        return validators.inn_conditions(value)

    @validator("phone")
    def phone_is_e164(cls, value):
        return validators.phone_is_e164(value)

    @root_validator
    def phone_or_email(cls, values):
        return validators.phone_or_email(values)


class PaymentItem(BaseModel):
    """
    Элемент списка товаров в заказе (не более 100 товаров).
    https://yookassa.ru/developers/api#create_payment_receipt_items

    """

    amount: Amount
    country_of_origin_code: str | None = None
    customs_declaration_number: str | None = Field(None, min_length=1, max_length=32)
    description: str = Field(
        max_length=128,
        default="Бронирование",
    )
    excise: str | None = Field(
        default=None,
        regex=r"\d+\.{0;1}\d{0;2}",
        description="Сумма акциза товара с учетом копеек. Десятичное число"
        "с точностью до 2 символов после точки.",
    )
    payment_mode: PAYMENT_MODE_TYPES | None = Field(
        None, description="Признак способа расчета"
    )
    payment_subject: PAYMENT_SUBJECT_TYPES | None= Field(
        None, description="Признак предмета расчета"
    )
    product_code: str | None = Field(
        None,
        description="Обязательный параметр, если товар нужно маркировать."
        "https://yookassa.ru/developers/api#create_payment_receipt_items_product_code",
    )
    quantity: str = "1"
    vat_code: VAT = Field(ge=1, le=6, default=VAT.NO_VAT)

    @validator("quantity")
    def quantity_is_numeric(cls, value: str):
        return validators.quantity_is_numeric(value)

    @validator("product_code")
    def is_prod_code_hex_max32(cls, value):
        return validators.is_prod_code_hex_max32(value)

    @validator("country_of_origin_code")
    def country_code_len2(cls, value):
        return validators.country_code_len2(value)

    class Config:
        use_enum_values = True


class Receipt(BaseModel):
    """
    Данные для формирования чека в онлайн-кассе (для соблюдения 54-ФЗ).
    https://yookassa.ru/developers/api#create_payment_receipt

    """
    customer: Customer | None
    items: Sequence[PaymentItem]
    tax_system_code: int | None = Field(ge=1, le=6)
