from collections.abc import Sequence

from pydantic import BaseModel, Field


class Passenger(BaseModel):
    """
    Список пассажиров. Необходимо использовать латинские буквы,
    например SERGEI, IVANOV.
    """

    first_name: str = Field(..., pattern=r'[A-Za-z]{1,64}')
    last_name: str = Field(..., pattern=r'[A-Za-z]{1,64}')


class Leg(BaseModel):
    """
    Перелёт
    """

    departure_airport: str = Field(..., pattern=r'[A-Z]{3}')
    destination_airport: str = Field(..., pattern=r'[A-Z]{3}')
    departure_date: str = Field(..., pattern=r'\d{4}-\d{2}-\d{2}')
    carrier_code: str | None = Field(None, pattern=r'[A-Z]{2,3}')


class AirTicket(BaseModel):
    """
    Объект с данными для продажи авиабилетов. Используется только
    для платежей банковской картой.

    https://clck.ru/39kemf
    """

    ticket_number: str | None = Field(None, pattern=r'[0-9]{1,150}')
    booking_reference: str | None = Field(None, min_length=1, max_length=20)
    passengers: Sequence[Passenger] | None = None
    legs: Sequence[Leg] | None = None
