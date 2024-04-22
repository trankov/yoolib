from pydantic import BaseModel, Field


class ReceiptMarkCodeInfo(BaseModel):
    """
    Код товара 54ФЗ.1163.

    Обязательный параметр, если одновременно выполняются эти условия:
      - вы используете Чеки от ЮKassa или онлайн-кассу, обновленную до ФФД 1.2;
      - товар нужно маркировать.
    Должно быть заполнено хотя бы одно поле.

    https://yookassa.ru/developers/api#receipt_object_items_mark_code_info
    """

    mark_code_raw: str | None = Field(
        None,
        description=(
            'Код товара в виде, котором был прочитан сканером 54ФЗ.2000.'
            'Нужно передавать, если используете онлайн-кассу Orange Data. '
            'https://clck.ru/39nLGt'
        ),
    )
    unknown: str | None = Field(None, max_length=32, min_length=1)
    ean_8: str | None = Field(None, max_length=8, min_length=8)
    ean_13: str | None = Field(None, max_length=13, min_length=13)
    itf_14: str | None = Field(None, max_length=14, min_length=14)
    gs_10: str | None = Field(None, max_length=38, min_length=1)
    gs_1m: str | None = Field(None, max_length=200, min_length=1)
    short: str | None = Field(None, max_length=38, min_length=1)
    fur: str | None = Field(
        None,
        max_length=20,
        min_length=20,
        description='Контрольно-идентификационный знак мехового изделия 54ФЗ.1307.',
    )
    egais_20: str | None = Field(None, max_length=33, min_length=33)
    egais_30: str | None = Field(None, max_length=14, min_length=14)
