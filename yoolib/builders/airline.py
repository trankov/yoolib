from collections.abc import Sequence

from ..models.payments.airline import Passenger


class AddPassengers:
    """
    Передаётся набор кортежей типа ('NAME', 'SURNAME').
    """

    def __init__(self, *args):
        self.passengers = args

    def __get__(self, instance, owner) -> list[Passenger]:
        return [
            Passenger(
                first_name=first_name,
                last_name=last_name,
            ) for first_name, last_name in self.passengers
        ]
