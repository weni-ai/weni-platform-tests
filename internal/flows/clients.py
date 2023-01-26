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

    def retrieve_user_api_token(self, user_email: str, org_uuid: str):
        url = self._get_url("/api/v2/internals/users/api-token")
        params = dict(user=user_email, org=org_uuid)
        response = requests.get(url, headers=self._authenticator.headers, params=params)

        return response


class ChatsFlowsClient(ClientInterface, ClientBase):

    _base_url = FlowsSettings.BASE_URL
    _authenticator = OIDCClientCredentialsAuth(ChatsSettings)

    def create_queue(self, sector_uuid: str, name: str, uuid: str) -> "Response":
        url = self._get_url(f"/api/v2/internals/ticketers/{sector_uuid}/queues")
        data = dict(name=name, uuid=uuid)
        response = requests.post(url, headers=self._authenticator.headers, json=data)

        return response

    def update_queue(self, sector_uuid: str, queue_uuid: str, name: str) -> "Response":
        url = self._get_url(f"/api/v2/internals/ticketers/{sector_uuid}/queues/{queue_uuid}")
        data = dict(name=name)
        response = requests.patch(url, headers=self._authenticator.headers, json=data)

        return response

    def destroy_queue(self, sector_uuid: str, queue_uuid: str) -> "Response":
        url = self._get_url(f"/api/v2/internals/ticketers/{sector_uuid}/queues/{queue_uuid}")
        response = requests.delete(url, headers=self._authenticator.headers)

        return response


