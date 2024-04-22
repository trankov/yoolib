import os
from dataclasses import dataclass

from niquests.auth import _basic_auth_str


@dataclass
class YooClientAuth:
    shop_id: str = ''
    secret_key: str = ''
    agent_id: str = ''
    agent_secret_key: str = ''
    oauth_token: str = ''

    def payment_header(self):
        return {'Authorization': _basic_auth_str(self.shop_id, self.secret_key)}

    def payout_header(self):
        return {'Authorization': _basic_auth_str(self.agent_id, self.agent_secret_key)}

    def oauth_header(self):
        return {'Authorization': f'Bearer {self.oauth_token}'}

    @classmethod
    def from_env(cls):
        return cls(
            shop_id=os.getenv('YOO_SHOP_ID') or '',
            secret_key=os.getenv('YOO_SECRET_KEY') or '',
            agent_id=os.getenv('YOO_AGENT_ID') or '',
            agent_secret_key=os.getenv('YOO_AGENT_SECRET_KEY') or '',
            oauth_token=os.getenv('YOO_OAUTH_TOKEN') or '',
        )

    @classmethod
    def from_secrets(cls, secrets_dict: dict[str, str]):
        return cls(
            shop_id=secrets_dict['shop_id'],
            secret_key=secrets_dict['secret_key'],
            agent_id=secrets_dict['agent_id'],
            agent_secret_key=secrets_dict['agent_secret_key'],
            oauth_token=secrets_dict['oauth_token'],
        )

yoo_client_auth = YooClientAuth()
yoo_client_auth.payment_header()
