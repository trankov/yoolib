from ..models.confirmations import (
    PaymentConfirmationTypes,
    get_confirmation_in_model,
)


class AddConfirmation:
    """
    Обязательный параметр:
    `confirmation_type: models.confirmations.PaymentConfirmationTypes`

    kwargs:
    - Для всех — `locale: models.confirmations.Locales = 'RU_ru'`
    - Для `mobile_application` — `return_url: str`
    - Для `redirect` — `enforce: bool = False`, `return_url: str`

    В общем случае, только для `mobile_application` и `redirect` обязательно
    требуется `return_url`, остальное сформируется автоматически.
    """

    def __init__(self, confirmation_type: PaymentConfirmationTypes, **kwargs):
        self.confirmation_type = confirmation_type
        self.kwargs = kwargs
        self.confirmation_model = get_confirmation_in_model(confirmation_type)

    def __get__(self, instance, owner):
        if not self.confirmation_model:
            raise ValueError(
                f'Неизвестный тип подтверждения: {self.confirmation_type}'
            )

        return self.confirmation_model(**self.kwargs)
