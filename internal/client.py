from abc import ABCMeta, abstractproperty

import requests

import settings


class ClientBase(metaclass=ABCMeta):
    def __init__(self, settings_class) -> None:
        self.settings = settings_class

    @abstractproperty
    def _base_url(self) -> str:
        pass

    @property
    def _headers(self) -> dict:
        return {
            "Content-Type": "application/json; charset: utf-8",
            "Authorization": self._get_auth_token(),
        }

    def _get_url(self, endpoint: str) -> str:
        assert endpoint.startswith("/"), f"The endpoint must contain a leading slash: /{endpoint}"
        return self._base_url + endpoint

    def _get_auth_token(self) -> str:
        response = requests.post(
            url=settings.OIDC_OP_TOKEN_ENDPOINT,
            data=dict(
                client_id=self.settings.OIDC_RP_CLIENT_ID,
                client_secret=self.settings.OIDC_RP_CLIENT_SECRET,
                grant_type="client_credentials",
            ),
        )

        response.raise_for_status()
        token = response.json().get("access_token")

        return f"Bearer {token}"
