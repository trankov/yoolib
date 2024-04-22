from enum import StrEnum


class PaymentConfirmationTypes(StrEnum):
    EMBEDDED = 'embedded'
    EXTERNAL = 'external'
    QR = 'qr'
    MOBILE_APPLICATION = 'mobile_application'
    REDIRECT = 'redirect'


class Locales(StrEnum):
    RU = 'ru_RU'
    EN = 'en_US'
