from string import hexdigits

from . import iso3166  # country codes
from . import iso4217  # currency code

from vrtour.commons.exceptions import YooError


def currency_match_iso4217(value: iso4217.CURRENCY_TYPES):
    if value not in iso4217.CURRENCY_LIST:
        raise YooError(
            f"There is no `{value}` in ISO-2417:2015 standard"
        ).as_status(422)
    return value


def inn_conditions(value: str):
    if value is None:
        return None
    val_len = len(value)
    if all((value.isdecimal, any((val_len == 10, val_len == 12)))):
        return value
    raise YooError("INN must be 10 or 12 digits").as_status(422)


def phone_is_e164(value):
    if value is None:
        return None
    if all((value.isdecimal, 3 < len(value) < 15)):
        return value
    raise YooError(
        f"Phone {value} incorrect (3 to 15 digits of ITU-T E.164)"
    ).as_status(422)


def phone_or_email(values):
    if {values.get("phone"), values.get("email")} == {None}:
        raise YooError(
            "There must be at least one of <phone> or <email>"
        ).as_status(422)
    return values


def quantity_is_numeric(value):
    if value.isdigit():
        return value
    raise YooError(f"Value {value} must be string of integers").as_status(422)


def is_prod_code_hex_max32(value):
    # Example of product code (from docs):
    # 00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00
    # 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00
    if not value: return value
    hex_seq = value.upper().split(" ")
    if all(
        (
            1 <= len(hex_seq) <= 32,
            all(
                (all(hexdigit in hexdigits for hexdigit in chunk), len(chunk) == 2)
                for chunk in hex_seq
            ),
        )
    ):
        return value
    raise YooError(f"`product_code` {value} is invalid").as_status(422)


def country_code_len2(value: iso3166.COUNTRY_A2_TYPES):
    if value in iso3166.COUNTRY_A2_LIST:
        return value
    raise YooError(f'Bad Alfa-2 country code: "{value}"').as_status(422)


class MetadataValidator(dict):
    def full_validation(self):
        self.max16keys()
        self.key32chars()
        self.value512UTF8chars()

    def max16keys(self):
        if len(self) > 16:
            raise YooError("Too many Metadata keys (max=16)").as_status(422)

    def key32chars(self):
        for k in self.keys():
            if len(k) > 32:
                raise YooError(
                    f'Too long Metadata key "{k}" (max=32)'
                ).as_status(422)

    def value512UTF8chars(self):
        for v in self.values():
            if type(v) is not str:
                raise YooError(
                    "All Metadata values must be UTF-8 strings"
                ).as_status(422)
            if len(v) > 512:
                raise YooError(
                    f'Too long Metadata value "{v[:8]}…{v[-8:]}" (max=512)'
                ).as_status(422)
