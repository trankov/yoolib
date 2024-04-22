from typing import TypeAlias

from pydantic import BaseModel, Field

from .definitions import Locales, PaymentConfirmationTypes


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
        '',
        description=(
            'Диплинк на мобильное приложение, в котором пользователь '
            'подтверждает платеж.'
        ),
        max_length=2048,
    )


class ConfirmationRedirectInModel(ConfirmationBaseInModel):
    type: PaymentConfirmationTypes = PaymentConfirmationTypes.REDIRECT
    enforce: bool | None = False
    return_url: str = Field('', max_length=2048)


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


ConfirmationInModels: TypeAlias = (
    ConfirmationEmbeddedInModel
    | ConfirmationExternalInModel
    | ConfirmationMobileApplicationInModel
    | ConfirmationQRcodeInModel
    | ConfirmationRedirectInModel
)
