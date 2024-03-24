from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from typing import TYPE_CHECKING

from .requisite_models import RequisiteModel
from .serializers import FieldSerializer


class Charset(StrEnum):
    WIN1251 = '1'
    UTF8 = '2'
    KOI8_R = '3'


class FormatID(StrEnum):
    ST = 'ST'


class FormatVersion(StrEnum):
    DEFAULT = '0001'


@dataclass(frozen=True, slots=True)
class FieldInstance:
    name: str
    model: RequisiteModel
    value: str

    def serialize(self, serializer: Callable = FieldSerializer) -> dict:
        # Serializer must get a FieldInstance and return a dict
        return serializer(self).serialize()


@dataclass(frozen=True, slots=True)
class ServiceData:
    encoding: Charset = Charset.UTF8
    format_id: FormatID = FormatID.ST
    format_version: FormatVersion = FormatVersion.DEFAULT

    def __str__(self):
        return f'{self.format_id}{self.format_version}{self.encoding}'
