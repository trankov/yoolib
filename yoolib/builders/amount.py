from isoworld import currencies

from ..models.common import Amount


def add_amount(
    self,
    value: float,
    attr_name: str = 'amount',
    currency: currencies.CurrencyCode = currencies.CurrencyCode.RUB
):
    setattr(self, attr_name, Amount(value=value, currency=currency))
    return self


# В partial пеередавать attr_name если отличен от 'amount'
