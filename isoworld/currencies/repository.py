from .currencydict import CURRENCIES
from .currencytuples import CURRENCYKEYS, CURRENCYTUPLES


def get(**kwargs) -> dict[str, str | int] | None:
    if not set(kwargs.keys()).issubset(CURRENCYKEYS):
        raise AttributeError(f'Invalid country parameters: {kwargs.keys()}')

    return next(
        (
            country
            for country in CURRENCIES
            if all(country[kw] == kwargs[kw] for kw in kwargs) # pylint: disable=C0206
        ),
        None,
    )


def find(**kwargs) -> list[dict[str, str | int]]:
    return [i for i in CURRENCIES if all(i[kw] == kwargs[kw] for kw in kwargs)]  # pylint: disable=C0206
