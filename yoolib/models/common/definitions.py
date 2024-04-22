from enum import IntEnum, StrEnum


class VATRateNum(IntEnum):
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


class TaxSystemNumCode(IntEnum):
    """
    Код системы налогообложения
    https://clck.ru/39nNBj
    """

    GENERAL = 1
    USN_INCOME = 2
    USN_INCOME_MINUS_EXPENSES = 3
    ENVD = 4
    ESN = 5
    PATENT = 6
