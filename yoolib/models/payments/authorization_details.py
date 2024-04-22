from pydantic import BaseModel, Field

from .docs import DOCS


class Secure3D(BaseModel):
    """
    Данные о прохождении пользователем аутентификации по 3‑D Secure
    для подтверждения платежа.
    """

    applied: bool = Field(..., description=DOCS.Secure3D.applied)


class AuthorizationDetails(BaseModel):
    """
    Данные об авторизации платежа.
    """

    rrn: str | None = Field(None, description=DOCS.AuthorizationDetails.rrn)
    auth_code: str | None = Field(
        None, description=DOCS.AuthorizationDetails.auth_code
    )
    three_d_secure: Secure3D = Field(
        ..., description=DOCS.AuthorizationDetails.three_d_secure
    )
