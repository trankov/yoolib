from pydantic import BaseModel

from . import enums, repository


class CurrencyModel(BaseModel):
    entity: str
    currency: str
    alphabetic_code: enums.CurrencyCode
    numeric_code: enums.CurrencyNum
    minors_unit: int

    @classmethod
    def get(cls, **kwargs) -> 'CurrencyModel | None':
        obj = repository.get(**kwargs)
        return cls.model_validate(obj) if obj else None

    @classmethod
    def find(cls, **kwargs) -> 'list[CurrencyModel] | None':
        obj = repository.find(**kwargs)
        return [cls.model_validate(o) for o in obj] if obj else None
