from typing import TypeAlias

from pydantic import BaseModel

from .definitions import PaymentConfirmationTypes


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


ConfirmationOutModels: TypeAlias = (
    ConfirmationEmbeddedOutModel
    | ConfirmationExternalOutModel
    | ConfirmationMobileApplicationOutModel
    | ConfirmationQRcodeOutModel
    | ConfirmationRedirectOutModel
)
