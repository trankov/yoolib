from pydantic import BaseModel, Field

from ..common.amount import Amount
from .docs import DOCS
from .metadata import Metadata


class Transfer(BaseModel):
    account_id: str = Field(..., description=DOCS.Transfer.account_id)
    amount: Amount = Field(..., description=DOCS.Transfer.amount)
    platform_fee_amount: Amount | None = None
    metadata: Metadata | None = None
