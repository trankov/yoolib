from pydantic import BaseModel, Field

from ..common.amount import Amount
from .definitions import ReceiptCalcType


class ReceiptSettlement(BaseModel):
    """
    Перечень совершенных расчетов
    """

    type: ReceiptCalcType
    amount: Amount
