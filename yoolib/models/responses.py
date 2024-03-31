from typing import Literal, Sequence, TypeAlias

from pydantic import BaseModel

from .common.___common import Amount
from .methods import PAYMENT_METHOD_TYPES


class YooInfoOutModel(BaseModel):
    account_id: str
    status: Literal["enabled", "disabled"]
    test: bool
    fiscalization_enabled: bool | None
    payment_methods: Sequence[PAYMENT_METHOD_TYPES] | None
    itn: str | None
    payout_methods: Sequence[Literal["bank_card", "yoo_money", "sbp"]] | None
    name: str | None
    payout_balance: Amount | None


ErrorCodesType: TypeAlias = Literal[
    "invalid_request",
    "invalid_credentials",
    "forbidden",
    "not_found",
    "too_many_requests",
    "internal_server_error",
]

ErrorCodesMapping = {
    "invalid_request": "Неправильный запрос, например ошибка в значении "
    "параметра или нарушение логики проведения операции",
    "invalid_credentials": "Некорректные данные для аутентификации запросов",
    "forbidden": "Не хватает прав для выполнения операции",
    "not_found": "Запрашиваемый ресурс не найден",
    "too_many_requests": "Превышен лимит запросов в единицу времени",
    "internal_server_error": "Технические неполадки на стороне ЮKassa",
}


class YooErrorModel(BaseModel):
    """
    https://yookassa.ru/developers/using-api/response-handling/response-format#error
    """

    type: str = "error"
    id: str
    code: ErrorCodesType | str
    description: str | None
    parameter: str | None

    def explain(self) -> str:
        # 405, 415 - надо смотреть заголовок Reason-Phrase
        return ErrorCodesMapping.get(self.code, "Нет соответствия коду ошибки")
