from typing import TYPE_CHECKING

import requests

from clients import ClientInterface, ClientBase
from authenticators import OIDCClientCredentialsAuth
from settings import ChatsSettings, ConnectSettings


if TYPE_CHECKING:
    from requests import Response


class ConnectChatsClient(ClientInterface, ClientBase):

    _base_url = ChatsSettings.BASE_URL
    _authenticator = OIDCClientCredentialsAuth(ConnectSettings)

    def list_projects(self) -> "Response":
        url = self._get_url("/v1/internal/project")
        return requests.get(url, headers=self._authenticator.headers)

    def retrieve_project(self, uuid: str) -> "Response":
        url = self._get_url(f"/v1/internal/project/{uuid}")
        return requests.get(url, headers=self._authenticator.headers)
