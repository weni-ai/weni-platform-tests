from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

import requests

import settings


if TYPE_CHECKING:
    from requests import Response


class OIDCAuth(metaclass=ABCMeta):
    def _request(self, data: dict) -> "Response":
        response = requests.post(url=settings.OIDC_OP_TOKEN_ENDPOINT, data=data)
        response.raise_for_status()

        return response

    @abstractmethod
    def _get_auth_token(self) -> str:
        pass

    @property
    def headers(self) -> dict:
        return {
            "Content-Type": "application/json; charset: utf-8",
            "Authorization": self._get_auth_token(),
        }


class OIDCPasswordAuth(OIDCAuth):
    def _get_auth_token(self) -> str:
        data = dict(
            client_id=settings.PROJECT_CLIENT_ID,
            username=settings.PROJECT_ADMIN_USER_EMAIL,
            password=settings.PROJECT_ADMIN_USER_PASSWORD,
            grant_type="password",
        )

        response = self._request(data)
        token = response.json().get("access_token")

        return f"Bearer {token}"


class OIDCClientCredentialsAuth(OIDCAuth):
    def __init__(self, settings_class) -> None:
        self.settings = settings_class

    def _get_auth_token(self) -> str:
        data = dict(
            client_id=self.settings.OIDC_RP_CLIENT_ID,
            client_secret=self.settings.OIDC_RP_CLIENT_SECRET,
            grant_type="client_credentials",
        )

        response = self._request(data)
        token = response.json().get("access_token")

        return f"Bearer {token}"
