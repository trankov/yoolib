import platform
import sys
from collections.abc import Callable
from dataclasses import dataclass
from typing import NamedTuple
from uuid import UUID, uuid4

import niquests as requests
from niquests.adapters import HTTPAdapter
from niquests.auth import _basic_auth_str
from urllib3_future import Retry

from . import models
from .exceptions import YooError


class YooPoints(NamedTuple):
    """
    Constants for YooEndoints
    """

    BASE: str = "https://api.yookassa.ru/v3/"
    INFO: str = "me/"

    PAY: str = "payments/"
    PAYMENT: str = "payments/{payment_id}"
    CAPTURE: str = "payments/{payment_id}/capture/"
    CANCEL: str = "payments/{payment_id}/cancel/"

    REFUNDS: str = "refunds/"
    REFUND: str = "refunds/"
    REFUND_STATUS: str = "refunds/{refund_id}"

    RECEIPTS: str = "receipts/"
    RECEIPT: str = "receipts/{receipt_id}"

    PAYOUTS: str = "payouts/"
    PAYOUT: str = "payouts/{payout_id}"

    SELF_EMPLOYED: str = "self_employed"
    SELF_EMPLOYED_INFO: str = "self_employed/{self_employed_id}"

    SBP: str = "sbp_banks/"

    PERSONAL_DATA: str = "personal_data/"
    PERSONAL_DATA_INFO: str = "personal_data/{personal_data_id}"

    DEALS: str = "deals/"
    DEAL: str = "deal/{deal_id}"


class YooEndpoints:
    """
    Generates endpoint strings for YooClient methods
    """

    def __init__(self, endpoints: YooPoints | None = None) -> None:
        self.points = endpoints or YooPoints()

    def info(self) -> str:
        return f"{self.points.BASE}{self.points.INFO}"

    def payments(self) -> str:
        return self._build_url(self.points.PAY)

    def pay(self) -> str:
        return self._build_url(self.points.PAY)

    def payment(self, payment_id: str | UUID) -> str:
        return self._build_url(self.points.PAYMENT, payment_id=payment_id)

    def capture(self, payment_id: str | UUID) -> str:
        return self._build_url(self.points.CAPTURE, payment_id=payment_id)

    def cancel(self, payment_id: str | UUID) -> str:
        return self._build_url(self.points.CANCEL, payment_id=payment_id)

    def refunds(self) -> str:
        return self._build_url(self.points.REFUNDS)

    def refund(self) -> str:
        return self._build_url(self.points.REFUND)

    def refund_status(self, refund_id: str | UUID) -> str:
        return self._build_url(self.points.REFUND_STATUS, refund_id=refund_id)

    def payouts(self) -> str:
        return self._build_url(self.points.PAYOUTS)

    def payout(self, payout_id: str | UUID) -> str:
        return self._build_url(self.points.PAYOUT, payout_id=payout_id)

    def self_employed(self) -> str:
        return self._build_url(self.points.SELF_EMPLOYED)

    def self_employed_info(self, self_employed_id: str | UUID) -> str:
        return self._build_url(
            self.points.SELF_EMPLOYED_INFO, self_employed_id=self_employed_id
        )

    def sbp_banks(self) -> str:
        return self._build_url(self.points.SBP)

    def personal_data(self) -> str:
        return self._build_url(self.points.PERSONAL_DATA)

    def personal_data_info(self, personal_data_id: str | UUID) -> str:
        return self._build_url(
            self.points.PERSONAL_DATA_INFO, personal_data_id=personal_data_id
        )

    def deals(self) -> str:
        return self._build_url(self.points.DEALS)

    def deal(self, deal_id: str | UUID) -> str:
        return self._build_url(self.points.DEAL, deal_id=deal_id)

    def _build_url(self, url_pattern, **kwargs) -> str:
        return f"{self.points.BASE}{url_pattern.format(**kwargs)}"


class YooClientConnection:
    """
    Provides low level HTTPS connection to API requests, as well as
    authentication headers and idempotency key (sending as part of headers
    parameter).

    Provides POST, GET and DELETE methods: `post()`, `get()`, `delete()`.
    """

    session: requests.Session
    headers: dict
    max_attempts: int
    timeout: int
    shop_id: str
    api_key: str

    @property
    def python_version_signature(self):
        return "{}.{}.{} ({})".format(*sys.implementation.version)

    @property
    def headers_ua(self):
        return (
            f"{platform.uname().system}/{platform.uname().release} ({platform.uname().machine}) "
            f"Python/{self.python_version_signature} "
            # f"Django/{django_version()} "
            # f"Ninja/{ninja_version} "
            f"YooLib/0.0.1 (development)"
        )

    def __init__(self, headers: dict[str, str] | None = None, **kwargs):
        for k, v in kwargs.items():
            if k in self.__annotations__:
                setattr(self, k, v)

        self._init_headers(headers=headers)

        self._check_mandatory_params("max_attempts", lambda: 5)
        self._check_mandatory_params("timeout", lambda: 10)
        self._check_mandatory_params("session", self._session)

    def __del__(self):
        if hasattr(self, "session"):
            self.session.close()

    def _check_mandatory_params(self, param: str, default: Callable) -> None:
        """
        Set default value if param is not set. For a lazy initialization,
        the default value have to be a function or any callable.
        """
        if not hasattr(self, param):
            setattr(self, param, default())

    def _init_headers(self, headers: dict[str, str] | None = None) -> None:
        if not self.base_auth_data:
            raise YooError("You must specify both an api_key and a shop_id")
        self.headers = {
            "Content-type": "application/json",
            "Authorization": _basic_auth_str(self.shop_id, self.api_key),
            "YM-User-Agent": self.headers_ua,
        } | (headers or {})

    def _session(self) -> requests.Session:
        retries = Retry(
            backoff_factor=int(self.timeout * 1e-3),
            allowed_methods=("POST", "GET", "DELETE"),
            status_forcelist=(202,),
            total=self.max_attempts,
        )
        session = requests.Session()
        session.mount(
            "https://",
            HTTPAdapter(
                max_retries=retries,  # type:ignore
            ),
        )
        return session

    @property
    def base_auth_data(self) -> bool:
        return hasattr(self, "api_key") and hasattr(self, "shop_id")

    def post(self, endpoint="", body=None, **kwargs) -> requests.Response:
        return self._execute("POST", endpoint=endpoint, body=body or {}, **kwargs)

    def get(self, endpoint="", query=None, **kwargs) -> requests.Response:
        return self._execute("GET", endpoint=endpoint, query=query or {}, **kwargs)

    def delete(self, endpoint="", query=None, **kwargs) -> requests.Response:
        return self._execute("DELETE", endpoint=endpoint, query=query or {}, **kwargs)

    def _execute(
        self,
        method: str,
        endpoint: str = "",
        query: dict | None = None,
        body: dict | None = None,
        **kwargs,
    ) -> requests.Response:
        return self.session.request(
            method,
            endpoint,
            params=query or {},
            headers=self.headers,
            data=body or {},
            **kwargs,
        )


@dataclass(slots=True)
class YooClient:
    connection: YooClientConnection
    endpoints: YooEndpoints
    idempotence_key: UUID

    def _process_response(self, response: requests.Response) -> dict:
        if response.status_code not in (200, 201, 204):
            raise YooError(f"{response.status_code}, {response.text}")
        # .as_status(
        #         response.status_code or 500
        #     ) from None
        return response.json()

    # def info(self) -> models.YooInfoOutModel:
    #     endpoint = self.endpoints.info()
    #     response = self.connection.get(endpoint)
    #     verified_response = self._process_response(response)
    #     return models.YooInfoOutModel(**verified_response)

    # def pay(self, payment: models.NewPayment) -> models.Payment:
    #     endpoint = self.endpoints.pay()
    #     response = self.connection.post(endpoint, body=payment.json())
    #     verified_response = self._process_response(response)
    #     return models.Payment(**verified_response)

    def payments(self) -> dict:
        return self.connection.get(self.endpoints.payments()).json()

    # def payment(self, payment_id: str | UUID) -> models.Payment:
    #     endpoint = self.endpoints.payment(payment_id)
    #     response = self.connection.get(endpoint)
    #     verified_response = self._process_response(response)
    #     return models.Payment(**verified_response)

    # def capture(
    #     self, payment_id: str | UUID, amount: models.Amount | None = None
    # ) -> models.Payment:
    #     endpoint = self.endpoints.capture(payment_id)
    #     response = self.connection.post(
    #         endpoint, body=amount.json() if amount else None
    #     )
    #     verified_response = self._process_response(response)
    #     return models.Payment(**verified_response)

    # def cancel(self, payment_id: str | UUID) -> models.Payment:
    #     endpoint = self.endpoints.cancel(payment_id)
    #     response = self.connection.post(endpoint)
    #     verified_response = self._process_response(response)
    #     return models.Payment(**verified_response)

    def refunds(self, **kwargs):
        # https://yookassa.ru/developers/api?codeLang=bash#get_refunds_list
        raise NotImplementedError

    # def refund(self, refund_request: models.RefundRequest) -> models.RefundModel:
    #     endpoint = self.endpoints.refund()
    #     response = self.connection.post(endpoint, body=refund_request.json())
    #     verified_response = self._process_response(response)
    #     return models.RefundModel(**verified_response)

    # def refund_status(self, refund_id: str | UUID) -> models.RefundModel:
    #     endpoint = self.endpoints.refund_status(refund_id)
    #     response = self.connection.get(endpoint)
    #     verified_response = self._process_response(response)
    #     return models.RefundModel(**verified_response)

    # def payouts(self):
    #     raise NotImplementedError

    # def payout(self):
    #     raise NotImplementedError

    # def self_employed(self):
    #     raise NotImplementedError

    # def self_employed_info(self):
    #     raise NotImplementedError

    # def sbp_banks(self):
    #     raise NotImplementedError

    # def personal_data(self):
    #     raise NotImplementedError

    # def personal_data_info(self):
    #     raise NotImplementedError

    # def deals(self):
    #     raise NotImplementedError

    # def deal(self):
    #     raise NotImplementedError



def yoo_client(
    idempotence_key: UUID | None = None,
    api_key: str | None = None,
    shop_id: str | None = None,
) -> YooClient:
    idp_key = idempotence_key or uuid4()
    return YooClient(
        idempotence_key=idp_key,
        endpoints=YooEndpoints(),
        connection=YooClientConnection(
            headers={"Idempotence-Key": str(idp_key)},
            api_key=api_key, #or yoosecrets.platform_api_key,
            shop_id=shop_id, # or yoosecrets.platform_id,
        ),
    )
