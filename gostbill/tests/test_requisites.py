from .. import validators
from ..requisite_models import RequisiteModel


# Happy path tests
def test_requisite_model_happy_path():

    model = RequisiteModel(
        definition="Name",
        short='short',
        long='long',
        required=True,
        validator=validators.Name
    )

    expected_repr = (
        "RequisiteModel(definition='Name', short='short', long='long', "
        "required=True, validator=gostbill.validators.Name)"
    )

    assert repr(model) == expected_repr
