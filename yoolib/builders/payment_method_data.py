from ..models.common import Amount
from ..models.payments.newpayment_method import (
    NewPaymentBankCard,
    get_newpayment_method_data_model,
)
from ..models.payments.payment_method import PaymentMethodType
from ..models.payments.vat import (
    TaxRate,
    VatCalculationMode,
    get_vat_data_model,
)


def add_payment_method_data(
    self,
    payment_method_type: PaymentMethodType,
    # For MobileBalancePaymentMethod and SberPayPaymentMethod
    phone: str | None = None,
    # For CardPayment
    number: str | None = None,
    expiry_year: str | None = None,
    expiry_month: str | None = None,
    cardholder: str | None = None,
    csc: str | None = None,
    # For SberBusinessPaymentMethod
    payment_purpose: str | None = None,
    type_: VatCalculationMode | None = None,
    amount: float | None = None,
    rate: TaxRate | None = None,
):
    # Get PaymentMethodData model
    payment_model = get_newpayment_method_data_model(payment_method_type)
    if not payment_model:
        raise ValueError(f'Неизвестный тип платежа: {payment_method_type}')

    # Common arguments for all payment methods
    _kwargs = {'type': payment_method_type}

    # Presise arguments for some payment methods

    if payment_method_type in (
        PaymentMethodType.MOBILE_BALANCE,
        PaymentMethodType.SBERBANK,
    ):
        _kwargs |= {'phone': phone}

    if payment_method_type == PaymentMethodType.BANK_CARD:
        _kwargs |= {
            'card': NewPaymentBankCard(
                # Validation will be done with pydantic, so 'type ignore'
                number=number,  # type: ignore
                expiry_year=expiry_year,  # type: ignore
                expiry_month=expiry_month,  # type: ignore
                cardholder=cardholder,
                csc=csc,
            )
        }

    if payment_method_type == PaymentMethodType.SBER_B2B:
        # For B2B we also need VAT data
        vat_data_model = get_vat_data_model(payment_method_type=type_)  # type: ignore
        if not vat_data_model:
            raise ValueError(f'Неизвестный тип расчета НДС: {type_}')
        vat_kwargs = {
            'type': type_,
            # In Russian Tax Systems, the value is always in rubles
            'amount': Amount(value=amount) if amount else None,
            'rate': rate,
        }
        _kwargs |= {
            'payment_purpose': payment_purpose,
            'vat_data': vat_data_model(**vat_kwargs),
        }

    self.payment_method_data = payment_model(**_kwargs)  # type: ignore
    return self
