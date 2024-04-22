from isoworld.currencies import CurrencyCode

from pydantic import BaseModel


class Amount(BaseModel):
    """
    Сумма платежа.

    По умолчанию: Amount(currency='RUB', value=0.0)

    https://yookassa.ru/developers/api#payment_object_amount
    """

    currency: CurrencyCode = CurrencyCode.RUB
    value: float = 0.0
