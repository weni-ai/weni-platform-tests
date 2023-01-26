from typing import TYPE_CHECKING

import requests

from clients import ClientInterface, ClientBase
from authenticators import OIDCClientCredentialsAuth
from settings import ConnectSettings, FlowsSettings, ChatsSettings


if TYPE_CHECKING:
    from requests import Response


class ConnectFlowsClient(ClientInterface, ClientBase):

    _base_url = FlowsSettings.BASE_URL
    _authenticator = OIDCClientCredentialsAuth(ConnectSettings)

    def create_template_org(self, user_email: str, name: str, timezone: str) -> "Response":
        url = self._get_url("/api/v2/internals/template-orgs/")
        data = dict(user_email=user_email, name=name, timezone=timezone)

        response = requests.post(url, headers=self._authenticator.headers, json=data)

        return response

    def create_flow(self, org_uuid: str, sample_flow: str):
        url = self._get_url("/api/v2/internals/flows/")
        data = dict(org=org_uuid, sample_flow=sample_flow)
        response = requests.post(url, headers=self._authenticator.headers, json=data)

        return response

