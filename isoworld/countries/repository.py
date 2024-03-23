from .countrydict import COUNTRIES
from .countrytuples import COUNTRYKEYS, COUNTRYTUPLES


def get(**kwargs) -> dict[str, str | int] | None:
    if not set(kwargs.keys()).issubset(COUNTRYKEYS):
        raise AttributeError(f'Invalid country parameters: {kwargs.keys()}')

    return next(
        (
            country
            for country in COUNTRIES
            if all(country[kw] == kwargs[kw] for kw in kwargs) # pylint: disable=C0206
        ),
        None,
    )


def find(*args) -> dict[str, str | int] | None:
    """
    Return first found country which contains all values passed in *args
    """
    if not args:
        return None
    row = next((i for i in COUNTRYTUPLES if set(args).issubset(i)), None)
    return {i[0]: i[1] for i in zip(COUNTRYKEYS, row)} if row else None
