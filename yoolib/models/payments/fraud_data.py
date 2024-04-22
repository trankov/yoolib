from pydantic import BaseModel, Field


class BankAccount(BaseModel):
    """
    Данные банковского счета, открытого в вашей системе.
    Необходимо передавать, если пользователь пополняет свой счет
    """

    account_number: str | None = Field(None, pattern=r'\d{20}')
    bic: str | None = Field(None, pattern=r'\d{9}')


class FraudData(BaseModel):
    """
    Информация для проверки операции на мошенничество.
    """

    topped_up_phone: str | None = Field(None, pattern=r'\d{4,15}')
    merchant_customer_bank_account: BankAccount | None = None
