from enum import StrEnum
from typing import TypeAlias

from pydantic import BaseModel, Field

from ..common import Amount


class VatCalculationMode(StrEnum):
    """
    Код способа расчета НДС.
    """

    UNTAXED = 'untaxed'
    CALCULATED = 'calculated'
    MIXED = 'mixed'


class TaxRate(StrEnum):
    """
    Ставка НДС.
    """

    VAT7 = '7'
    VAT10 = '10'
    VAT18 = '18'
    VAT20 = '20'


class AbstractVatData(BaseModel):
    """
    Данные о налоге на добавленную стоимость (НДС).
    Платеж может облагаться или не облагаться НДС. Товары могут облагаться
    по одной ставке НДС или по разным.
    """

    type: VatCalculationMode


class UntaxedVatData(AbstractVatData):
    """
    НДС не облагается.
    """

    type: VatCalculationMode = VatCalculationMode.UNTAXED


class CalculatedVatData(AbstractVatData):
    """
    НДС по единой ставке для всех товаров.
    """

    type: VatCalculationMode = VatCalculationMode.CALCULATED
    amount: Amount
    rate: TaxRate


class MixedVatData(AbstractVatData):
    """
    НДС облагается по разным ставкам НДС.
    """

    type: VatCalculationMode = VatCalculationMode.MIXED
    amount: Amount


VatData: TypeAlias = UntaxedVatData | MixedVatData | CalculatedVatData


def get_vat_data_model(
    payment_method_type: VatCalculationMode,
) -> type[AbstractVatData] | None:
    return next(
        (
            i
            for i in AbstractVatData.__subclasses__()
            if i.model_fields['type'].default == payment_method_type
        ),
        None,
    )
