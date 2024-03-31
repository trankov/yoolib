from dataclasses import dataclass

from ..models.common import Amount
from ..models.confirmations import PaymentConfirmationTypes
from ..models.payments.airline import AirTicket, Leg, Passenger
from ..models.payments.payment_method import PaymentMethodType
from ..models.payments.recipient import Recipient
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
    receipt = None
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
        receipt=bricks.receipt,
        recipient=bricks.recipient(account_id='123', gateway_id='321'),
        confirmation=bricks.confirmation(
            confirmation_type=bricks.PaymentConfirmationTypes.REDIRECT,
            return_url='321',
        ),
        capture=True,
        metadata={'key': 'value'},
    )  # type: ignore
