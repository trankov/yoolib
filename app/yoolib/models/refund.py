from datetime import datetime
from typing import Literal, Sequence

from pydantic import BaseModel, Field

import payments.yoolib2.schemas.common as common


class RefundSource(BaseModel):
    """
    Данные о том, с какого магазина и какую сумму нужно удержать
    для проведения возврата. Необходимо передавать, если вы используете
    Сплитование платежей. Сейчас в этом параметре можно передать данные
    только одного магазина.

    https://yookassa.ru/developers/api?codeLang=python#create_refund_sources

    """
    account_id: str = Field(
        ...,
        description="Идентификатор магазина, для которого вы хотите провести "
        "возврат. Выдается ЮKassa, отображается в разделе Продавцы личного "
        "кабинета (столбец shopId).",
    )
    amount: common.Amount = Field(
        ...,
        description="Сумма возврата.",
    )
    platform_fee_amount: common.Amount | None = Field(
        default=None,
        description="Комиссия, которую вы удержали при оплате, и хотите вернуть.",
    )


class RefundSettlements(BaseModel):
    """
    Данные о распределении денег.

    Тип данных для `RefundRequest.deal`:
    - Данные о сделке, в составе которой проходит возврат.
    - Необходимо передавать, если вы проводите Безопасную сделку .

    https://yookassa.ru/developers/api?codeLang=python#create_refund_deal_refund_settlements

    """

    type: Literal["payout"] = Field(
        default="payout",
        description="Тип операции. Фиксированное значение: "
        "'payout' — выплата продавцу.",
    )
    amount: common.Amount = Field(
        ...,
        description="Сумма, на которую необходимо уменьшить вознаграждение "
        "продавца. Должна быть меньше суммы возврата или равна ей.",
    )


class RefundDeal(BaseModel):
    id: str
    refund_settlements: Sequence[RefundSettlements]


class RefundBaseModel(BaseModel):
    payment_id: str = Field(..., min_length=36, max_length=36)
    amount: common.Amount
    description: str | None = None
    sources: Sequence[RefundSource] | None = None


class RefundRequest(RefundBaseModel):
    receipt: common.Receipt | None = None
    deal: Sequence[RefundSettlements] | None = None


class RefundModel(RefundBaseModel):
    id: str
    status: common.PAYMENT_STATUS_TYPES
    created_at: datetime
    cancellation_details: common.CancellationDetails | None
    receipt_registration: common.PAYMENT_STATUS_TYPES | None
    deal: Sequence[RefundDeal] | None
