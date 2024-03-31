from enum import StrEnum
from typing import Literal, TypeAlias, Union

from pydantic import BaseModel, Field


class PaymentConfirmationTypes(StrEnum):
    EMBEDDED = 'embedded'
    EXTERNAL = 'external'
    QR = 'qr'
    MOBILE_APPLICATION = 'mobile_application'
    REDIRECT = 'redirect'


class Locales(StrEnum):
    RU = 'ru_RU'
    EN = 'en_US'


# Input Shemas


class ConfirmationBaseInModel(BaseModel):
    type: PaymentConfirmationTypes
    locale: Locales | None = Locales.RU


class ConfirmationEmbeddedInModel(ConfirmationBaseInModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.EMBEDDED


class ConfirmationExternalInModel(ConfirmationBaseInModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.EXTERNAL


class ConfirmationQRcodeInModel(ConfirmationBaseInModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.QR


class ConfirmationMobileApplicationInModel(ConfirmationBaseInModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.MOBILE_APPLICATION
    return_url: str = Field(
        description=(
            'Диплинк на мобильное приложение, в котором пользователь '
            'подтверждает платеж.'
        ),
        max_length=2048,
    )


class ConfirmationRedirectInModel(ConfirmationBaseInModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.REDIRECT
    enforce: bool | None = False
    return_url: str = Field(..., max_length=2048)


def get_confirmation_in_model(
    confirmation_type: PaymentConfirmationTypes,
) -> type[ConfirmationBaseInModel] | None:
    return {
        PaymentConfirmationTypes.EMBEDDED: ConfirmationEmbeddedInModel,
        PaymentConfirmationTypes.EXTERNAL: ConfirmationExternalInModel,
        PaymentConfirmationTypes.QR: ConfirmationQRcodeInModel,
        PaymentConfirmationTypes.MOBILE_APPLICATION: ConfirmationMobileApplicationInModel,
        PaymentConfirmationTypes.REDIRECT: ConfirmationRedirectInModel,
    }.get(confirmation_type)


# Output Shemas


class ConfirmationBaseOutModel(BaseModel):
    type: PaymentConfirmationTypes


class ConfirmationEmbeddedOutModel(ConfirmationBaseOutModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.EMBEDDED
    confirmation_token: str


class ConfirmationExternalOutModel(ConfirmationBaseOutModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.EXTERNAL


class ConfirmationMobileApplicationOutModel(ConfirmationBaseOutModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.MOBILE_APPLICATION
    confirmation_url: str


class ConfirmationQRcodeOutModel(ConfirmationBaseOutModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.QR
    confirmation_data: str


class ConfirmationRedirectOutModel(ConfirmationBaseOutModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.REDIRECT
    confirmation_url: str
    enforce: bool | None
    return_url: str | None


# Type Aliases for confirmations

ConfirmationOutModels: TypeAlias = (
    ConfirmationEmbeddedOutModel
    | ConfirmationExternalOutModel
    | ConfirmationMobileApplicationOutModel
    | ConfirmationQRcodeOutModel
    | ConfirmationRedirectOutModel
)

ConfirmationInModels: TypeAlias = (
    ConfirmationEmbeddedInModel
    | ConfirmationExternalInModel
    | ConfirmationMobileApplicationInModel
    | ConfirmationQRcodeInModel
    | ConfirmationRedirectInModel
)
