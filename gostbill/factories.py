from dataclasses import dataclass

from .core import GostBill, Requisite


@dataclass
class BillFactory:
    @classmethod
    def create_bill(cls, bill_class: type[GostBill]) -> GostBill:
        bill = bill_class()
        fields = bill._fieldnames
        for name, value in cls.__dict__.items():
            if name in fields:
                setattr(bill, name, value)
        return bill
