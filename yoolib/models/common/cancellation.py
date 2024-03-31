from pydantic import BaseModel

from .definitions import PaymentParty


class CancellationDetails(BaseModel):
    """
    Кто принял решение об отмене транзакции

    https://clck.ru/39j9aP
    """

    party: PaymentParty
    reason: str
