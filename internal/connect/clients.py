from typing import TYPE_CHECKING

import requests

from clients import ClientInterface, ClientBase
from authenticators import OIDCClientCredentialsAuth
from settings import AISettings, ConnectSettings


if TYPE_CHECKING:
    from requests import Response


class AIConnectClient(ClientInterface, ClientBase):

    _base_url = ConnectSettings.BASE_URL
    _authenticator = OIDCClientCredentialsAuth(AISettings)

    def list_classifiers(self, project_uuid: str, user_email: str) -> "Response":
        url = self._get_url("/v1/organization/project/list_classifier/")
        params = dict(project_uuid=project_uuid, user_email=user_email)

        response = requests.get(url, headers=self._authenticator.headers, params=params)
        response.raise_for_status()

        return response
