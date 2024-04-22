from pydantic import BaseModel, Field


class ReceiptIndustryDetails(BaseModel):
    """
    Отраслевой реквизит предмета расчета 54ФЗ.1260
    Обязателен при использовании ФФД 1.2.
    """

    federal_id: str = Field(
        ...,
        pattern=r'(^00[1-9]{1}$)|(^0[1-6]{1}[0-9]{1}$)|(^07[0-3]{1}$)',
        description=(
            'Идентификатор федерального органа исполнительной власти 54ФЗ.1262'
        ),
    )
    document_date: str = Field(
        ...,
        pattern=r'\d{4}-\d{2}-\d{2}',
        description='Дата документа основания 54ФЗ.1263',
    )
    document_number: str = Field(
        ...,
        max_length=32,
        description=(
            'Номер нормативного акта федерального органа исполнительной власти, '
            'регламентирующего порядок заполнения реквизита «значение '
            'отраслевого реквизита» 54ФЗ.1264'
        ),
    )
    value: str = Field(
        ...,
        description='Значение отраслевого реквизита 54ФЗ.1265',
        max_length=256,
    )
