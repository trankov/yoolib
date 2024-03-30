from collections.abc import Sequence
from enum import IntEnum, StrEnum

from isoworld import countries, currencies

from pydantic import BaseModel, EmailStr, Field, root_validator, validator

from . import validators


class VAT(IntEnum):
    """
    Код ставки НДС

    https://clck.ru/39j9xn
    """

    NO_VAT = 1
    RATE_0 = 2
    RATE_10 = 3
    RATE_20 = 4
    RATE_10_110 = 5
    RATE_20_120 = 6


class PaymentSubject(StrEnum):
    COMMODITY = 'commodity'
    EXCISE = 'excise'
    JOB = 'job'
    SERVICE = 'service'
    GAMBLING_BET = 'gambling_bet'
    GAMBLING_PRIZE = 'gambling_prize'
    LOTTERY = 'lottery'
    LOTTERY_PRIZE = 'lottery_prize'
    INTELLECTUAL_ACTIVITY = 'intellectual_activity'
    PAYMENT = 'payment'
    AGENT_COMMISSION = 'agent_commission'
    PROPERTY_RIGHT = 'property_right'
    NON_OPERATING_GAIN = 'non_operating_gain'
    INSURANCE_PREMIUM = 'insurance_premium'
    SALES_TAX = 'sales_tax'
    RESORT_FEE = 'resort_fee'
    COMPOSITE = 'composite'
    ANOTHER = 'another'


class PaymentMode(StrEnum):
    FULL_PREPAYMENT = 'full_prepayment'
    PARTIAL_PREPAYMENT = 'partial_prepayment'
    ADVANCE = 'advance'
    FULL_PAYMENT = 'full_payment'
    PARTIAL_PAYMENT = 'partial_payment'
    CREDIT = 'credit'
    CREDIT_PAYMENT = 'credit_payment'


class PaymentStatus(StrEnum):
    """
    Статус платежа. Возможные значения: pending, waiting_for_capture,
    succeeded и canceled.
    """

    PENDING = 'pending'
    WAITING_FOR_CAPTURE = 'waiting_for_capture'
    SUCCEEDED = 'succeeded'
    CANCELED = 'canceled'


class PaymentParty(StrEnum):
    YOO_MONEY = 'yoo_money'
    PAYMENT_NETWORK = 'payment_network'
    MERCHANT = 'merchant'


class CancellationDetails(BaseModel):
    """
    Кто принял решение об отмене транзакции

    https://clck.ru/39j9aP
    """

    party: PaymentParty
    reason: str


class Amount(BaseModel):
    """
    Сумма платежа.

    https://yookassa.ru/developers/api#payment_object_amount
    """

    currency: currencies.CurrencyCode = currencies.CurrencyCode.RUB
    value: float = 0.0

    # @validator('currency')
    # def currency_match_iso4217(cls, value):
    #     return validators.currency_match_iso4217(value)


class Customer(BaseModel):
    """
    Информация о пользователе
    https://yookassa.ru/developers/api#create_payment_receipt_customer

    """

    email: EmailStr | str | None = None
    full_name: str | None = Field(max_length=256)
    inn: str | None  # = Field(hint='If None, put passport in `full_name`')
    phone: str | None = None

    # @validator('inn')
    # def inn_conditions(cls, value):
    #     return validators.inn_conditions(value)

    # @validator('phone')
    # def phone_is_e164(cls, value):
    #     return validators.phone_is_e164(value)

    # @root_validator
    # def phone_or_email(cls, values):
    #     return validators.phone_or_email(values)


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
        default='Бронирование',
    )
    excise: str | None = Field(
        default=None,
        # pattern=r'\d+\.{0;1}\d{0;2}',
        description=(
            'Сумма акциза товара с учетом копеек. Десятичное число'
            'с точностью до 2 символов после точки.'
        ),
    )
    payment_mode: PaymentMode | None = Field(
        None, description='Признак способа расчета'
    )
    payment_subject: PaymentSubject | None = Field(
        None, description='Признак предмета расчета'
    )
    product_code: str | None = Field(
        None,
        description=(
            'Обязательный параметр, если товар нужно маркировать. https://clck.ru/39jA2N'
        ),
    )
    quantity: str = '1'
    vat_code: VAT = Field(ge=1, le=6, default=VAT.NO_VAT)

    # @validator('quantity')
    # def quantity_is_numeric(cls, value: str):
    #     return validators.quantity_is_numeric(value)

    # @validator('product_code')
    # def is_prod_code_hex_max32(cls, value):
    #     return validators.is_prod_code_hex_max32(value)

    # @validator('country_of_origin_code')
    # def country_code_len2(cls, value):
    #     return validators.country_code_len2(value)

    class Config:
        use_enum_values = True
