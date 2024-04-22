from .. import fields
from ..core import GostBill
from ..factories import BillFactory


class MockGostBill(GostBill):
    name = fields.Name()
    amount = fields.Sum()


class AnotherMockGostBill(GostBill):
    uin = fields.UIN()
    date = fields.DocDate()


class CommonFactory(BillFactory):
    name = 'name_field'
    amount = '1000.00'
    uin = '1234567890'
    date = '2024-03-29'


# Happy path tests
def test_create_bill_happy_path():
    mock_bill: MockGostBill = CommonFactory.create_bill(MockGostBill)
    another_mock_bill: AnotherMockGostBill = CommonFactory.create_bill(
        AnotherMockGostBill
    )

    assert isinstance(mock_bill, MockGostBill)
    assert isinstance(another_mock_bill, AnotherMockGostBill)
    assert issubclass(mock_bill.__class__, GostBill)
    assert issubclass(another_mock_bill.__class__, GostBill)
    assert mock_bill.name == 'name_field'
    assert mock_bill.amount == '1000.00'
    assert another_mock_bill.uin == '1234567890'
    assert another_mock_bill.date == '2024-03-29'
    assert hasattr(mock_bill, 'name')
    assert hasattr(mock_bill, 'amount')
    assert not hasattr(mock_bill, 'uin')
    assert not hasattr(mock_bill, 'date')
    assert hasattr(another_mock_bill, 'uin')
    assert hasattr(another_mock_bill, 'date')
    assert not hasattr(another_mock_bill, 'amount')
    assert not hasattr(another_mock_bill, 'name')
