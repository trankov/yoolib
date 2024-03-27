from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum, StrEnum

from .requisite_models import RequisiteModel
from .serializers import FieldSerializer


@dataclass(frozen=True, slots=True)
class FieldInstance:
    name: str
    model: RequisiteModel
    value: str | int | float | None

    def serialize(self, serializer: Callable = FieldSerializer):
        # Serializer must get a FieldInstance and return a dict
        return serializer(self).serialize()


@dataclass(frozen=True, slots=True)
class ServiceData:
    class Charset(StrEnum):
        WIN1251 = '1'
        UTF8 = '2'
        KOI8_R = '3'

    class FormatID(StrEnum):
        ST = 'ST'

    class FormatVersion(StrEnum):
        DEFAULT = '0001'

    encoding: Charset = Charset.UTF8
    format_id: FormatID = FormatID.ST
    format_version: FormatVersion = FormatVersion.DEFAULT

    def __str__(self):
        return f'{self.format_id}{self.format_version}{self.encoding}'


class BankingDetails(set, Enum):
    REQUIRED = {
        'Name',
        'PersonalAcc',
        'BankName',
        'BIC',
        'CorrespAcc',
    }
    ADDITIONAL = {
        'Sum',
        'Puprose',
        'PayeeINN',
        'PayerINN',
        'DrawerStatus',
        'KPP',
        'CBC',
        'OKTMO',
        'PaytReason',
        'TaxPeriod',
        'DocNo',
        'DocDate',
        'TaxPaytKind',
    }
    OPTIONAL = {
        'LastName',
        'FirstName',
        'MiddleName',
        'PayerAddress',
        'PersonalAccount',
        'DocIdx',
        'PensAcc',
        'Contract',
        'PersAcc',
        'Flat',
        'Phone',
        'PayerIdType',
        'PayerIdNum',
        'ChildFio',
        'BirthDate',
        'PaymTerm',
        'PaymPeriod',
        'Category',
        'ServiceName',
        'CounterId',
        'CounterVal',
        'QuittId',
        'QuittDate',
        'InstNum',
        'ClassNum',
        'SpecFio',
        'AddAmount',
        'RuleId',
        'ExecId',
        'RegType',
        'UIN',
        'TechCode',
    }

    @classmethod
    def full_set(cls) -> set:
        """
        Return a full set of banking details
        """
        return cls.REQUIRED | cls.ADDITIONAL | cls.OPTIONAL
