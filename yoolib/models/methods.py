"""https://yookassa.ru/developers/api#payment_object_payment_method"""


from dataclasses import dataclass
from enum import Enum
from typing import Literal, TypeAlias

from . import iso3166
from pydantic import BaseModel, Field, validator
from vrtour.commons.exceptions import YooError


BANK_CARD_SOURCE_TYPES: TypeAlias = Literal[
    "apple_pay",
    "google_pay",
]

PAYMENT_METHOD_TYPES: TypeAlias = Literal[
    "alfabank",
    "apple_pay",
    "bank_card",
    "cash",
    "google_pay",
    "installments",
    "mobile_balance",
    "qiwi",
    "sberbank",
    "tinkoff_bank",
    "wechat",
    "yoo_money",
]


class CARD_TYPES(str, Enum):
    MC = "MasterCard"
    MAESTRO = "MasterCard"
    VISA = "Visa"
    VISA_ELECTRON = "Visa"
    MIR = "Mir"
    UPAY = "UnionPay"
    JCB = "JCB"
    AMEX = "AmericanExpress"
    DINERS = "DinersClub"
    DISCOVER = "DiscoverCard"
    INSTAPAYMENT = ("InstaPayment",)
    INSTAPAYMENT_TM = "InstaPaymentTM"
    LASER = "Laser"
    DANKORT = "Dankort"
    SOLO = "Solo"
    SWITCH = "Switch"
    UNKNOWN = "Unknown"


class BankCard(BaseModel):
    first6: str | None = Field(
        default=...,
        description=(
            # https://yookassa.ru/developers/api#payment_object_payment_method_bank_card_card_first6
            "Первые 6 цифр номера карты (BIN). При оплате картой, сохраненной"
            "в ЮKassa  и других сервисах, переданный BIN может не соответствовать"
            "значениям last4, expiry_year, expiry_month. При оплате картой,"
            "сохраненной в Apple Pay или Google Pay, в параметре передается"
            "Device Account Number."
        ),
    )
    last4: str
    card_type: CARD_TYPES
    expiry_month: str
    expiry_year: str
    issuer_country: str | None = "RU"
    issuer_name: str | None = Field(
        default=..., description="Наименование банка, выпустившего карту"
    )
    source: BANK_CARD_SOURCE_TYPES | None

    @validator("expiry_year")
    def is_year_four_digits(cls, value):
        if value.isdigit and len(value) == 4:
            return value
        raise ValueError("Year must be 4 digits string, {value} doesn't match")

    @validator("expiry_month")
    def is_month_valid(cls, value):
        if value.isdigit and len(value) == 2:
            return value
        raise ValueError(
            "Month must be 2 digits string with leading zero "
            "if neccesary, {value} doesn't match"
        )

    @validator("issuer_country")
    def issuer_country_len2(cls, value: iso3166.COUNTRY_A2_TYPES):
        if value in iso3166.COUNTRY_A2_LIST:
            return value
        raise ValueError(f'Bad Alfa-2 country code: "{value}".')


class PaymentMethod(BaseModel):
    type: str = "bank_card"
    id: str = Field(..., description="Идентификатор способа оплаты")
    saved: bool = Field(
        default=False,
        description=(
            "С помощью сохраненного способа оплаты можно проводить "
            "безакцептные списания"
        ),
    )
    title: str | None = Field(None, description="Название способа оплаты")


class AlfabankPaymentMethod(PaymentMethod):
    type: str = "alfabank"
    login: str | None = Field(
        default=None,
        description=(
            "Логин пользователя в Альфа-Клике "
            "(привязанный телефон или дополнительный логин)"
        )
    )


class MobileBalancePaymentMethod(PaymentMethod):
    type: str = "mobile_balance"


class SplitPaymentMethod(PaymentMethod):
    type: str = "installments"


class BankCardPaymentMethod(PaymentMethod):
    type: str = "bank_card"
    card: BankCard


class CashPaymentMethod(PaymentMethod):
    type: str = "cash"


class SberBusinessPaymentMethod(PaymentMethod):
    # TO BE DONE
    type: str = "b2b_sberbank"


class TinkoffPaymentMethod(PaymentMethod):
    type: str = "tinkoff_bank"


class YooMoneyPaymentMethod(PaymentMethod):
    type: str = "yoo_money"
    account_number: str = Field(
        ..., description="Номер кошелька, из которого заплатил пользователь"
    )


class ApplePaymentMethod(PaymentMethod):
    type: str = "apple_pay"


class GooglePaymentMethod(PaymentMethod):
    type: str = "google_pay"


class QiwiPaymentMethod(PaymentMethod):
    type: str = "qiwi"


class SberPaymentMethod(PaymentMethod):
    type: str = "sberbank"
    phone: str | None = None

    @validator("phone")
    def is_phone_valid(cls, value: str):
        if value.isdigit() and value.startswith("79") and len(value) == 11:
            return value
        raise YooError("Invalid phone number").as_status(422)


class WeChatPaymentMethod(PaymentMethod):
    type: str = "wechat"


class WebMoneyPaymentMethod(PaymentMethod):
    type: str = "webmoney"


@dataclass(frozen=True, slots=True)
class PaymentMethodCard:
    alfabank = AlfabankPaymentMethod
    apple_pay = ApplePaymentMethod
    bank_card = BankCardPaymentMethod
    cash = CashPaymentMethod
    google_pay = GooglePaymentMethod
    installments = SplitPaymentMethod
    mobile_balance = MobileBalancePaymentMethod
    qiwi = QiwiPaymentMethod
    sberbank = SberPaymentMethod
    tinkoff_bank = TinkoffPaymentMethod
    wechat = WeChatPaymentMethod
    yoo_money = YooMoneyPaymentMethod
