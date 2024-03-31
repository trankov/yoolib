from dataclasses import dataclass

from ..models.common import Amount, Customer
from ..models.payments.airline import AirTicket, Leg, Passenger
from ..models.payments.confirmations import PaymentConfirmationTypes
from ..models.payments.payment_method import PaymentMethodType
from ..models.payments.recipient import Recipient
from ..models.receipts.payment_receipt import PaymentReceipt
from .airline import AddPassengers
from .confirmation import AddConfirmation
from .payment_method_data import AddPaymentMethodData


@dataclass(frozen=True, slots=True, eq=False, init=False)
class bricks:
    """
    Кирпичики для создания нового платежа. Одноимённый метод содержит ссылку
    на класс Pydantic или переопределяющий дескриптор со входными параметрами.

    Если входной параметр требует выражение Enum, одноименные алиасы на них
    содержатся здесь же.
    """

    amount = Amount
    customer = Customer
    receipt = PaymentReceipt
    recipient = Recipient
    payment_method_data = AddPaymentMethodData
    confirmation = AddConfirmation
    airline = AirTicket
    airline_leg = Leg
    airline_passenger = Passenger
    airline_passengers = AddPassengers

    PaymentConfirmationTypes = PaymentConfirmationTypes
    PaymentMethodType = PaymentMethodType


NewPaymentBuilder = None


if __name__ == '__main__':
    from ..models.payments.new_payment import NewPayment

    new_payment = NewPayment(
        amount=bricks.amount(value=100),
        description='test',
        receipt=bricks.receipt(
            customer=bricks.customer(
                email='ivan@yookassa.ru',
                full_name='Ivan Petrov',
            ),
            items=[],
            tax_system_code=None,
            receipt_industry_details=None,
            receipt_operational_details=None,
        ),
        recipient=bricks.recipient(account_id='123', gateway_id='321'),
        confirmation=bricks.confirmation(
            confirmation_type=bricks.PaymentConfirmationTypes.REDIRECT,
            return_url='321',
        ),
        capture=True,
        metadata={'key': 'value'},
        airline=bricks.airline(
            ticket_number='123',
            booking_reference='321',
            legs=[
                bricks.airline_leg(
                    departure_airport='SVO',
                    destination_airport='LED',
                    departure_date='2022-01-01',
                    carrier_code='SU',
                )
            ],
            passengers=[
                bricks.airline_passenger(first_name='STEPAN', last_name='IVANOV'),
                bricks.airline_passenger(first_name='VIKTORIA', last_name='IVANOVA'),
            ]
        ),
        deal=None,
        merchant_customer_id=None,
    )
