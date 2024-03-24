from pydantic import BaseModel

from . import enums, repository


class CurrencyModel(BaseModel):
    entity: str
    currency: str
    code: enums.CurrencyCode
    num: enums.CurrencyNum
    minors: int

    @classmethod
    def get(cls, **kwargs) -> 'CurrencyModel | None':
        obj = repository.get(**kwargs)
        return cls.model_validate(obj) if obj else None

    @classmethod
    def find(cls, **kwargs) -> 'list[CurrencyModel] | None':
        obj = repository.find(**kwargs)
        return [cls.model_validate(o) for o in obj] if obj else None
