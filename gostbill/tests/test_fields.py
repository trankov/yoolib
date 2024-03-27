from .. import fields
from ..core_models import FieldInstance


def test_field_instance():
    field_instance = FieldInstance('amount', fields.Sum.model, 'test')
    assert field_instance.name == 'amount'
    assert field_instance.model == fields.Sum.model
    assert field_instance.value == 'test'


def test_field_structure():
    field = fields.Sum
    assert hasattr(field, 'model')
    assert issubclass(field, fields.Requisite)
    assert field.model
    assert field.model.definition
    assert field.model.short
    assert field.model.long
    assert field.model.required


def test_field_assigning():
    class TestClass:
        test_field = fields.Sum()

    test_class = TestClass()
    test_class.test_field = 100
    assert test_class.test_field
    assert test_class.test_field == '100'
