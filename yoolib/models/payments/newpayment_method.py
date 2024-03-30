from typing import TypeAlias

from pydantic import BaseModel, Field

from .payment_method import PaymentMethodType
from .vat import VatData


class NewPaymentBankCard(BaseModel):
    """Данные банковской карты для нового платежа"""

    number: str = Field(..., pattern=r'[0-9]{16,19}')
    expiry_year: str = Field(..., pattern=r'[0-9]{4}')
    expiry_month: str = Field(..., pattern=r'[0-9]{2}')
    cardholder: str | None = Field(None, pattern=r'[A-Za-z]{0,26}')
    csc: str | None = Field(None, pattern=r'[0-9]{3,4}')


class AbstractPaymentMethodData(BaseModel):
    type: PaymentMethodType


class SberLoanPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.SBER_LOAN


class MobileBalancePaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.MOBILE_BALANCE
    phone: str


class BankCardPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.BANK_CARD
    card: NewPaymentBankCard | None


class SplitPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.INSTALLMENTS


class CashPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.CASH


class SBPPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.SBP


class SberBusinessPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.SBER_B2B
    payment_purpose: str = Field(..., max_length=210)
    vat_data: VatData


class YooMoneyPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.YOO_MONEY


class SberPayPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.SBERBANK
    phone: str | None


class TinkoffBankPaymentMethodData(AbstractPaymentMethodData):
    type: PaymentMethodType = PaymentMethodType.TINKOFF_BANK


PaymentMethodData: TypeAlias = (
    SberLoanPaymentMethodData
    | MobileBalancePaymentMethodData
    | BankCardPaymentMethodData
    | SplitPaymentMethodData
    | CashPaymentMethodData
    | SBPPaymentMethodData
    | SberBusinessPaymentMethodData
    | YooMoneyPaymentMethodData
    | SberPayPaymentMethodData
    | TinkoffBankPaymentMethodData
)


def get_newpayment_method_data_model(
    payment_method_type: PaymentMethodType,
) -> type[AbstractPaymentMethodData] | None:
    """Возвращает модель данных для нового платежа"""
    return next(
        (
            i
            for i in AbstractPaymentMethodData.__subclasses__()
            if i.type == payment_method_type
        ),
        None,
    )
