"""https://yookassa.ru/developers/api#payment_object_payment_method"""

__all__ = ['PaymentMethods', 'get_payment_method_model']

from enum import StrEnum
from typing import TypeAlias

from isoworld import countries

from pydantic import BaseModel, ConfigDict, Field

from ..common import Amount
from .vat import VatData


class BankCardSource(StrEnum):
    """Источник данных банковской карты"""

    APPLE_PAY = 'apple_pay'
    GOOGLE_PAY = 'google_pay'
    MIR_PAY = 'mir_pay'


class PaymentMethodType(StrEnum):
    """Тип способа оплаты"""

    ALFABANK = 'alfabank'
    APPLE_PAY = 'apple_pay'
    BANK_CARD = 'bank_card'
    CASH = 'cash'
    GOOGLE_PAY = 'google_pay'
    INSTALLMENTS = 'installments'
    MOBILE_BALANCE = 'mobile_balance'
    QIWI = 'qiwi'
    SBER_LOAN = 'sber_loan'
    SBERBANK = 'sberbank'
    SBER_B2B = 'b2b_sberbank'
    SBP = 'sbp'
    TINKOFF_BANK = 'tinkoff_bank'
    WEBMONEY = 'webmoney'
    WECHAT = 'wechat'
    YOO_MONEY = 'yoo_money'


class BankCardType(StrEnum):
    """Тип банковской карты"""

    MC = 'MasterCard'
    MAESTRO = 'MasterCard'
    VISA = 'Visa'
    VISA_ELECTRON = 'Visa'
    MIR = 'Mir'
    UNION_PAY = 'UnionPay'
    JCB = 'JCB'
    AMEX = 'AmericanExpress'
    DINERS_CLUB = 'DinersClub'
    DISCOVER_CARD = 'DiscoverCard'
    INSTAPAYMENT = 'InstaPayment'
    INSTAPAYMENT_TM = 'InstaPaymentTM'
    LASER = 'Laser'
    DANKORT = 'Dankort'
    SOLO = 'Solo'
    SWITCH = 'Switch'
    UNKNOWN = 'Unknown'


class CardProduct(BaseModel):
    """
    Карточный продукт платежной системы, с которым ассоциирована
    банковская карта.
    """

    code: str
    name: str | None


class BankCard(BaseModel):
    """Данные банковской карты"""

    model_config = ConfigDict(use_enum_values=True)

    # https://yookassa.ru/developers/api#payment_object_payment_method_bank_card_card_first6
    first6: str | None
    last4: str = Field(..., min_length=4, max_length=4)
    expiry_year: str
    expiry_month: str
    card_type: BankCardType
    card_product: CardProduct | None
    issuer_country: countries.CountriesA2 | None = countries.CountriesA2.RUSSIA
    issuer_name: str | None
    source: BankCardSource | None


class PayerBankDetails(BaseModel):
    """Банковские реквизиты плательщика (юридического лица или ИП)"""

    full_name: str = Field(..., max_length=800)
    short_name: str = Field(..., max_length=160)
    address: str = Field(..., max_length=500)
    inn: str = Field(..., pattern=r'\d{10}|\d{12}')
    bank_name: str = Field(..., min_length=1, max_length=350)
    bank_branch: str = Field(..., min_length=1, max_length=140)
    bank_bik: str = Field(..., pattern=r'\d{9}')
    account: str = Field(..., pattern=r'\d{20}')
    kpp: str | None = Field(None, pattern=r'\d{9}')


class AbstractPaymentMethod(BaseModel):
    type: PaymentMethodType
    id: str
    saved: bool
    title: str | None


class SberLoanPaymentMethod(AbstractPaymentMethod):
    """
    «Покупки в кредит» от СберБанка
    https://clck.ru/39kYs8
    """

    type: PaymentMethodType = PaymentMethodType.SBER_LOAN
    discount_amount: Amount | None
    loan_option: str


class AlfabankPaymentMethod(AbstractPaymentMethod):
    """Альфа-Клик"""

    type: PaymentMethodType = PaymentMethodType.ALFABANK
    login: str | None


class MobileBalancePaymentMethod(AbstractPaymentMethod):
    """Мобильный баланс"""

    type: PaymentMethodType = PaymentMethodType.MOBILE_BALANCE


class SplitPaymentMethod(AbstractPaymentMethod):
    """Рассрочка"""

    type: PaymentMethodType = PaymentMethodType.INSTALLMENTS


class BankCardPaymentMethod(AbstractPaymentMethod):
    """Банковская карта"""

    type: PaymentMethodType = PaymentMethodType.BANK_CARD
    card: BankCard


class CashPaymentMethod(AbstractPaymentMethod):
    """Наличные"""

    type: PaymentMethodType = PaymentMethodType.CASH


class SBPPaymentMethod(AbstractPaymentMethod):
    """Система быстрых платежей"""

    type: PaymentMethodType = PaymentMethodType.SBP
    sbp_operation_id: str | None


class SberBusinessPaymentMethod(AbstractPaymentMethod):
    """Сбербанк Бизнес Онлайн"""

    type: PaymentMethodType = PaymentMethodType.SBER_B2B
    payer_bank_details: PayerBankDetails | None
    payment_purpose: str = Field(..., max_length=210)
    vat_data: VatData


class YooMoneyPaymentMethod(AbstractPaymentMethod):
    """ЮMoney"""

    type: PaymentMethodType = PaymentMethodType.YOO_MONEY
    account_number: str | None


class ApplePaymentMethod(AbstractPaymentMethod):
    """ApplePay"""

    type: PaymentMethodType = PaymentMethodType.APPLE_PAY


class GooglePaymentMethod(AbstractPaymentMethod):
    """GooglePay"""

    type: PaymentMethodType = PaymentMethodType.GOOGLE_PAY


class QiwiPaymentMethod(AbstractPaymentMethod):
    """Qiwi Кошелёк"""

    type: PaymentMethodType = PaymentMethodType.QIWI


class SberPayPaymentMethod(AbstractPaymentMethod):
    """SberPay"""

    type: PaymentMethodType = PaymentMethodType.SBERBANK
    card: BankCard | None
    phone: str | None


class TinkoffPaymentMethod(AbstractPaymentMethod):
    """TinkoffPay"""

    type: PaymentMethodType = PaymentMethodType.TINKOFF_BANK


class WeChatPaymentMethod(AbstractPaymentMethod):
    type: PaymentMethodType = PaymentMethodType.WECHAT


class WebMoneyPaymentMethod(AbstractPaymentMethod):
    type: PaymentMethodType = PaymentMethodType.WEBMONEY


PaymentMethods: TypeAlias = (
    SberLoanPaymentMethod
    | AlfabankPaymentMethod
    | MobileBalancePaymentMethod
    | SplitPaymentMethod
    | BankCardPaymentMethod
    | CashPaymentMethod
    | SBPPaymentMethod
    | SberBusinessPaymentMethod
    | YooMoneyPaymentMethod
    | ApplePaymentMethod
    | GooglePaymentMethod
    | QiwiPaymentMethod
    | SberPayPaymentMethod
    | TinkoffPaymentMethod
    | WeChatPaymentMethod
    | WebMoneyPaymentMethod
)


def get_payment_method_model(
    method_type: PaymentMethodType,
) -> type[AbstractPaymentMethod] | None:
    return next(
        (i for i in AbstractPaymentMethod.__subclasses__() if i.type == method_type),
        None,
    )
