from pydantic import BaseModel, Field


class ReceiptOperationalDetails(BaseModel):
    """Операционный реквизит чека 54ФЗ.1270"""

    operation_id: int = Field(..., ge=0, le=255)
    value: str = Field(..., max_length=64)
    created_at: str
