from enum import IntEnum, StrEnum


class ReceiptStatus(StrEnum):
    """
    Статус регистрации чека в онлайн-кассе
    """

    PENDING = 'pending'
    SUCCEDED = 'succeeded'
    CANCELED = 'canceled'


class ReceiptType(StrEnum):
    """
    Тип чека в онлайн-кассе: приход (payment) или возврат прихода (refund)
    """

    PAYMENT = 'payment'
    REFUND = 'refund'


class ReceiptVatCode(IntEnum):
    """
    Коды ставок НДС
    https://clck.ru/39nFco
    """

    NO_VAT = 1                  # Без НДС
    ZERO_RATE = 2               # НДС по ставке 0%
    PERCENT_RATE_10 = 3         # НДС по ставке 10%
    PERCENT_RATE_20 = 4         # НДС чека по ставке 20%
    ESTIMATION_RATE_10_110 = 5  # НДС чека по расчетной ставке 10/110
    ESTIMATION_RATE_20_120 = 6  # НДС чека по расчетной ставке 20/120


class ReceiptPaymentSubject(StrEnum):
    """
    Признак предмета расчета
    https://clck.ru/39nFaN
    """

    COMMODITY = 'commodity'
    JOB = 'job'
    SERVICE = 'service'
    PAYMENT = 'payment'
    CASINO = 'casino'
    GAMBLING_BET = 'gambling_bet'
    GAMBLING_PRIZE = 'gambling_prize'
    LOTTERY = 'lottery'
    LOTTERY_PRIZE = 'lottery_prize'
    INTELLECTUAL_ACTIVITY = 'intellectual_activity'
    AGENT_COMMISSION = 'agent_commission'
    PROPERTY_RIGHT = 'property_right'
    NON_OPERATING_GAIN = 'non_operating_gain'
    INSURANCE_PREMIUM = 'insurance_premium'
    SALES_TAX = 'sales_tax'
    RESORT_FEE = 'resort_fee'
    MARKED = 'marked'
    NON_MARKED = 'non_marked'
    FINE = 'fine'
    TAX = 'tax'
    LIEN = 'lien'
    COST = 'cost'
    AGENT_WITHDRAWALS = 'agent_withdrawals'
    PENSION_INSURANCE_WITHOUT_PAYOUTS = 'pension_insurance_without_payouts'
    PENSION_INSURANCE_WITH_PAYOUTS = 'pension_insurance_with_payouts'
    HEALTH_INSURANCE_WITHOUT_PAYOUTS = 'health_insurance_without_payouts'
    HEALTH_INSURANCE_WITH_PAYOUTS = 'health_insurance_with_payouts'
    HEALTH_INSURANCE = 'health_insurance'
    ANOTHER = 'another'


class ReceiptPaymentMode(StrEnum):
    """
    Признак способа расчета
    https://clck.ru/39nFi7
    """

    FULL_PREPAYMENT = 'full_prepayment'
    FULL_PAYMENT = 'full_payment'


class ReceiptMeasure(StrEnum):
    """
    Мера количества предмета расчета
    https://clck.ru/39nFq3
    """

    PIECE = 'piece'
    GRAM = 'gram'
    KILOGRAM = 'kilogram'
    TON = 'ton'
    CENTIMETER = 'centimeter'
    DECIMETER = 'decimeter'
    METER = 'meter'
    SQUARE_CENTIMETER = 'square_centimeter'
    SQUARE_DECIMETER = 'square_decimeter'
    SQUARE_METER = 'square_meter'
    MILLILITER = 'milliliter'
    LITER = 'liter'
    CUBIC_METER = 'cubic_meter'
    KILOWATT_HOUR = 'kilowatt_hour'
    GIGACALORIE = 'gigacalorie'
    DAY = 'day'
    HOUR = 'hour'
    MINUTE = 'minute'
    SECOND = 'second'
    KILOBYTE = 'kilobyte'
    MEGABYTE = 'megabyte'
    GIGABYTE = 'gigabyte'
    TERABYTE = 'terabyte'
    ANOTHER = 'another'


class ReceiptCalcType(StrEnum):
    """
    Тип расчета
    https://clck.ru/39nGHz
    """

    CASHLESS = 'cashless'
    PREPAYMENT = 'prepayment'
    POSTPAYMENT = 'postpayment'
    CONSIDERATION = 'consideration'


class ReceiptAgentType(StrEnum):
    """
    Тип посредника

    Тип посредника передается в запросе на создание чека  в массиве items,
    в параметре agent_type, если вы отправляете данные для формирования чека
    по сценарию Сначала платеж, потом чек. Параметр agent_type нужно передавать,
    начиная с ФФД 1.1. Убедитесь, что ваша онлайн-касса обновлена до этой версии.


    https://clck.ru/39nKhR
    """

    BANKING_PAYMENT_AGENT = 'banking_payment_agent'
    BANKING_PAYMENT_SUBAGENT = 'banking_payment_subagent'
    PAYMENT_AGENT = 'payment_agent'
    PAYMENT_SUBAGENT = 'payment_subagent'
    ATTORNEY = 'attorney'
    COMMISSIONER = 'commissioner'
    AGENT = 'agent'
