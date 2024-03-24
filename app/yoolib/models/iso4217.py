# DO NOT AUTOFORMAT THIS

"""
Currency codes as in ISO 4217 2015
"""

__all__ = [
    "CURRENCY_TYPES",
    "CURRENCY_LIST",
]

from typing import Literal, TypeAlias, get_args


CURRENCY_TYPES: TypeAlias = Literal[
    "AFN", "EUR", "ALL", "DZD", "USD", "EUR", "AOA", "XCD", "XCD", "ARS", "AMD",
    "AWG", "AUD", "EUR", "AZN", "BSD", "BHD", "BDT", "BBD", "BYN", "EUR", "BZD",
    "XOF", "BMD", "INR", "BTN", "BOB", "BOV", "USD", "BAM", "BWP", "NOK", "BRL",
    "USD", "BND", "BGN", "XOF", "BIF", "CVE", "KHR", "XAF", "CAD", "KYD", "XAF",
    "XAF", "CLP", "CLF", "CNY", "AUD", "AUD", "COP", "COU", "KMF", "CDF", "XAF",
    "NZD", "CRC", "XOF", "HRK", "CUP", "CUC", "ANG", "EUR", "CZK", "DKK", "DJF",
    "XCD", "DOP", "USD", "EGP", "SVC", "USD", "XAF", "ERN", "EUR", "SZL", "ETB",
    "EUR", "FKP", "DKK", "FJD", "EUR", "EUR", "EUR", "XPF", "EUR", "XAF", "GMD",
    "GEL", "EUR", "GHS", "GIP", "EUR", "DKK", "XCD", "EUR", "USD", "GTQ", "GBP",
    "GNF", "XOF", "GYD", "HTG", "USD", "AUD", "EUR", "HNL", "HKD", "HUF", "ISK",
    "INR", "IDR", "XDR", "IRR", "IQD", "EUR", "GBP", "ILS", "EUR", "JMD", "JPY",
    "GBP", "JOD", "KZT", "KES", "AUD", "KPW", "KRW", "KWD", "KGS", "LAK", "EUR",
    "LBP", "LSL", "ZAR", "LRD", "LYD", "CHF", "EUR", "EUR", "MOP", "MKD", "MGA",
    "MWK", "MYR", "MVR", "XOF", "EUR", "USD", "EUR", "MRU", "MUR", "EUR", "XUA",
    "MXN", "MXV", "USD", "MDL", "EUR", "MNT", "EUR", "XCD", "MAD", "MZN", "MMK",
    "NAD", "ZAR", "AUD", "NPR", "EUR", "XPF", "NZD", "NIO", "XOF", "NGN", "NZD",
    "AUD", "USD", "NOK", "OMR", "PKR", "USD", "PAB", "USD", "PGK", "PYG", "PEN",
    "PHP", "NZD", "PLN", "EUR", "USD", "QAR", "EUR", "RON", "RUB", "RWF", "EUR",
    "SHP", "XCD", "XCD", "EUR", "EUR", "XCD", "WST", "EUR", "STN", "SAR", "XOF",
    "RSD", "SCR", "SLL", "SGD", "ANG", "XSU", "EUR", "EUR", "SBD", "SOS", "ZAR",
    "SSP", "EUR", "LKR", "SDG", "SRD", "NOK", "SEK", "CHF", "CHE", "CHW", "SYP",
    "TWD", "TJS", "TZS", "THB", "USD", "XOF", "NZD", "TOP", "TTD", "TND", "TRY",
    "TMT", "USD", "AUD", "UGX", "UAH", "AED", "GBP", "USD", "USD", "USN", "UYU",
    "UYI", "UYW", "UZS", "VUV", "VES", "VED", "VND", "USD", "USD", "XPF", "MAD",
    "YER", "ZMW", "ZWL", "XBA", "XBB", "XBC", "XBD", "XTS", "XXX", "XAU", "XPD",
    "XPT", "XAG"
]

CURRENCY_LIST: tuple[str] = get_args(CURRENCY_TYPES)
