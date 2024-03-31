from isoworld import currencies

from pydantic import BaseModel


class Amount(BaseModel):
    """
    Сумма платежа.

    https://yookassa.ru/developers/api#payment_object_amount
    """

    currency: currencies.CurrencyCode = currencies.CurrencyCode.RUB
    value: float = 0.0
