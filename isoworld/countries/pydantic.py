from pydantic import BaseModel

from . import enums, repository


class CountryModel(BaseModel):
    short_en: str
    long_en: str
    short_ru: str
    long_ru: str
    a2: enums.CountriesA2
    a3: enums.CountriesA3
    num: enums.CountriesNum
    tld: str

    @classmethod
    def get(cls, **kwargs) -> 'CountryModel | None':
        obj = repository.get(**kwargs)
        return cls.model_validate(obj) if obj else None

    @classmethod
    def find(cls, *args) -> 'CountryModel | None':
        obj = repository.find(*args)
        return cls.model_validate(obj) if obj else None
