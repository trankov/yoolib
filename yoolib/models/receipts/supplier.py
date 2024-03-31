from pydantic import BaseModel, Field


class ReceiptSupplier(BaseModel):
    """
    Информация о поставщике товара или услуги (тег в 54 ФЗ — 1224). Можно
    передавать, если вы отправляете данные для формирования чека по сценарию
    Сначала платеж, потом чек (https://clck.ru/39nKTn).

    https://yookassa.ru/developers/api#receipt_object_items_supplier
    """

    name: str | None
    phone: str | None
    inn: str | None
