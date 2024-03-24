import json
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .core import GostBill
    from .core_models import FieldInstance


class FieldSerializer:
    field: 'FieldInstance'

    def __init__(self, field: 'FieldInstance'):
        self.field = field

    def serialize(self) -> dict:
        return {
            'name': self.field.name,
            'value': self.field.value,
            'definition': self.field.model.definition,
            'short': self.field.model.short,
            'long': self.field.model.long,
            'required': self.field.model.required,
        }

    def __str__(self):
        return json.dumps(self.serialize())


class BillSerializer:
    bill: 'GostBill'

    def __init__(self, bill: 'GostBill'):
        self.bill = bill

    def serialize(self) -> dict:
        return {
            'name': self.bill.__class__.__name__,
            'encoding': ('cp1251', 'utf_8', 'koi8_r')[
                int(self.bill.service_data.encoding) - 1
            ],
            'description': self.bill.__doc__ or '',
            'fields': [
                self.bill[field].serialize()
                for field in self.bill._fieldnames
            ],
        }

    def __str__(self):
        return json.dumps(self.serialize(), ensure_ascii=False, indent=4)
