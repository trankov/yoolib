from collections.abc import Sequence
from typing import Literal

from pydantic import BaseModel

from ..common.amount import Amount


class Settlement(BaseModel):
    """
    Данные о распределении денег. Сумма вознаграждения продавца.
    """

    type: Literal['payout'] = 'payout'
    amount: Amount


class Deal(BaseModel):
    """
    Данные о сделке, в составе которой проходит платеж. Необходимо передавать,
    если вы проводите Безопасную сделку .
    """

    id: str
    settlements: Sequence[Settlement]
