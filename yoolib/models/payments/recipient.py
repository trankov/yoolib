from pydantic import BaseModel, ConfigDict, Field

from .docs import DOCS


class Recipient(BaseModel):
    """
    Получатель платежа
    https://yookassa.ru/developers/api#payment_object_recipient
    """

    account_id: str = Field(..., description=DOCS.Recipient.account_id)
    gateway_id: str = Field(..., description=DOCS.Recipient.gateway_id)
