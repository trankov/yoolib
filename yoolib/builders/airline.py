from collections.abc import Sequence

from ..models.payments.airline import Passenger


class AddPassengers:
    def __init__(self, passengers: Sequence[tuple[str, str]]):
        self.passengers = passengers

    def __get__(self, instance, owner):
        return [
            Passenger(
                first_name=first_name,
                last_name=last_name,
            ) for first_name, last_name in self.passengers
        ]
