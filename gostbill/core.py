from types import SimpleNamespace
from typing import TypeVar

from . import requisite_models as rm
from .core_models import BankingDetails, FieldInstance, ServiceData
from .serializers import BillSerializer


class RequisiteError(Exception):
    pass


class Requisite:
    model: rm.RequisiteModel

    def __init__(
        self,
        model: rm.RequisiteModel | None = None,
    ):
        if model:
            self.model = model
        # It is assumed that the model is defined in a subclass
        if not self.model:
            raise RequisiteError(
                f'Requisite model is not defined for {self.__class__.__name__}'
            )

    def __str__(self):
        return self.model.definition

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.hidden_name)

    def __set__(self, instance, value):
        instance.__dict__[self.hidden_name] = self.model.validator(value)

    def __set_name__(self, owner, name):
        self.public_name = name
        self.hidden_name = f'_{name}'

    def __delete__(self, instance):
        del instance.__dict__[self.hidden_name]


class GostBill:
    service_data: ServiceData = ServiceData()
    delimiter: str = '|'

    @property
    def _attrs(self) -> SimpleNamespace:
        return SimpleNamespace(
            **{
                i[0]: i[1].model
                for i in self.__class__.__dict__.items()
                if isinstance(i[1], Requisite)
            }
        )

    @property
    def __requisites(self) -> list[str]:
        return [
            f'{i[1].model.definition}={getattr(self, i[0], "")}'
            for i in self.__class__.__dict__.items()
            if isinstance(i[1], Requisite)
        ]

    @property
    def _fieldnames(self) -> list[str]:
        return [
            i[0]
            for i in self.__class__.__dict__.items()
            if isinstance(i[1], Requisite)
        ]

    @property
    def _definitions_declared(self) -> set[str]:
        return {i.model.definition for i in self}

    def __len__(self) -> int:
        return len(self._fieldnames)

    def __next__(self):
        yield from (
            FieldInstance(i, getattr(self._attrs, i), getattr(self, i))
            for i in self._fieldnames
        )

    def __iter__(self):
        return next(self)

    def __getitem__(self, key) -> FieldInstance:
        if isinstance(key, int):
            key = self._fieldnames[key]
        return FieldInstance(key, getattr(self._attrs, key), getattr(self, key))

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({", ".join(self.__requisites)})'

    def __str__(self) -> str:
        return (
            f'{self.service_data}{self.delimiter}'
            f'{self.delimiter.join(self.__requisites)}'
        )

    def __bytes__(self) -> bytes:
        return str(self).encode(encoding=self.service_data.encoding.codepage)

    @property
    def serializer(self) -> BillSerializer:
        return BillSerializer(self)

    @property
    def required_satisfied(self) -> bool:
        return BankingDetails.REQUIRED.issubset(self._definitions_declared)

    @property
    def additional_satisfied(self) -> bool:
        return BankingDetails.ADDITIONAL.issubset(self._definitions_declared)

    @property
    def definitions_correct(self) -> bool:
        return self._definitions_declared.issubset(BankingDetails.full_set())


GostBillType = TypeVar('GostBillType', bound=GostBill)
