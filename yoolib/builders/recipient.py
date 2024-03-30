from ..models.payments.recipient import Recipient


def add_recipient(self, account_id: str, gateway_id: str):
    self.recipient = Recipient(account_id=account_id, gateway_id=gateway_id)
    return self
