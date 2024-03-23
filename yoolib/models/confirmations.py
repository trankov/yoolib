from enum import Enum
from typing import Literal, TypeAlias, Union

from pydantic import BaseModel, Field

PAYMENT_CONFIRMATION_TYPES: TypeAlias = Literal[
    "embedded",
    "external",
    "qr",
    "mobile_application",
    "redirect",
]

# Input Shemas


class ConfirmationBaseInModel(BaseModel):
    type: PAYMENT_CONFIRMATION_TYPES
    locale: Literal["ru_RU", "en_US"] | None = "ru_RU"


class ConfirmationEmbeddedInModel(ConfirmationBaseInModel):
    type: Literal["embedded"] = "embedded"


class ConfirmationExternalInModel(ConfirmationBaseInModel):
    type: Literal["external"] = "external"


class ConfirmationQRcodeInModel(ConfirmationBaseInModel):
    type: Literal["qr"] = "qr"


class ConfirmationMobileApplicationInModel(ConfirmationBaseInModel):
    type: Literal["mobile_application"] = "mobile_application"
    return_url: str = Field(
        description=(
            "Диплинк на мобильное приложение, в котором пользователь "
            "подтверждает платеж."
        ),
        max_length=2048,
    )


class ConfirmationRedirectInModel(ConfirmationBaseInModel):
    type: Literal["redirect"] = "redirect"
    enforce: bool | None = False
    return_url: str = Field(..., max_length=2048)


# Output Shemas


class ConfirmationBaseOutModel(BaseModel):
    type: PAYMENT_CONFIRMATION_TYPES


class ConfirmationEmbeddedOutModel(ConfirmationBaseOutModel):
    type: Literal["embedded"]
    confirmation_token: str


class ConfirmationExternalOutModel(ConfirmationBaseOutModel):
    type: Literal["external"]


class ConfirmationMobileApplicationOutModel(ConfirmationBaseOutModel):
    type: Literal["mobile_application"]
    confirmation_url: str


class ConfirmationQRcodeOutModel(ConfirmationBaseOutModel):
    type: Literal["qr"]
    confirmation_data: str


class ConfirmationRedirectOutModel(ConfirmationBaseOutModel):
    type: Literal["redirect"]
    confirmation_url: str
    enforce: bool | None
    return_url: str | None


# Type Aliases for confirmations

ConfirmationOutModels: TypeAlias = Union[
    ConfirmationEmbeddedOutModel,
    ConfirmationExternalOutModel,
    ConfirmationMobileApplicationOutModel,
    ConfirmationQRcodeOutModel,
    ConfirmationRedirectOutModel,
]

ConfirmationInModels: TypeAlias = Union[
    ConfirmationEmbeddedInModel,
    ConfirmationExternalInModel,
    ConfirmationMobileApplicationInModel,
    ConfirmationQRcodeInModel,
    ConfirmationRedirectInModel,
]
