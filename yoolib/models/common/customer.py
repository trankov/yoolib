from pydantic import BaseModel, EmailStr, Field


class Customer(BaseModel):
    """
    Информация о пользователе
    https://yookassa.ru/developers/api#create_payment_receipt_customer

    """

    email: EmailStr | str | None = None
    full_name: str | None = Field(None, max_length=256)
    inn: str | None = None  # = Field(hint='If None, put passport in `full_name`')
    phone: str | None = None
