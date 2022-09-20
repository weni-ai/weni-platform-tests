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

    def list_permissions(self, project_uuid: str):
        url = self._get_url(f"/v1/internal/permission/project/?project={project_uuid}")
        return requests.get(url, headers=self._authenticator.headers)

    def retrieve_permissions(self, uuid: str):
        url = self._get_url(f"/v1/internal/permission/project/{uuid}")
        return requests.get(url, headers=self._authenticator.headers)


class FlowsChatsClient(ClientInterface, ClientBase):

    _base_url = ChatsSettings.BASE_URL
    _authenticator = OIDCClientCredentialsAuth(ConnectSettings)
    _header = {
        "Content-Type": "application/json; charset: utf-8",
        "Authorization": f"Bearer {ChatsSettings.EXTERNAL_TOKEN}"  
    }

    def list_external_queue(self, sector: str, name: str=None):
        url = self._get_url(f"/v1/external/queues/?sector={sector}&name={name}")
        return requests.get(url, headers=self._header)

    def retrieve_external_queue(self, queue_uuid: str):
        url = self._get_url(f"/v1/external/queues/{queue_uuid}/")
        return requests.get(url, headers=self._header)
    
    def list_external_room(self):
        url = self._get_url(f"/v1/external/rooms/")
        return requests.get(url, headers=self._header)

    def create_external_room(self):
        url = self._get_url(f"/v1/external/rooms/")
        return requests.post(url, headers=self._header)

    def retrieve_external_room(self, room_uuid: str):
        url = self._get_url(f"/v1/external/rooms/{room_uuid}/")
        return requests.get(url, headers=self._header)

    def update_external_room(self, room_uuid: str):
        url = self._get_url(f"/v1/external/rooms/{room_uuid}/")
        return requests.patch(url, headers=self._header)

    def delete_external_room(self, room_uuid: str):
        url = self._get_url(f"/v1/external/rooms/{room_uuid}/")
        return requests.delete(url, headers=self._header)

    def close_external_room(self, room_uuid: str):
        url = self._get_url(f"/v1/external/rooms/{room_uuid}/close")
        return requests.patch(url, headers=self._header)

    def list_external_agents(self, user: str, role: str, queue: str, sector: str):
        url = self._get_url(f"/v1/external/agents/?user={user}&role={role}&queue={queue}&sector={sector}")
        return requests.get(url, headers=self._header)

    def retrieve_external_agents(self, agent_uuid: str):
        url = self._get_url(f"/v1/external/agents/{agent_uuid}/")
        return requests.get(url, headers=self._header)

    def list_external_msgs(self, room: str):
        url = self._get_url(f"/v1/external/msgs/?room={room}")
        return requests.get(url, headers=self._header)

    def create_external_msgs(self):
        url = self._get_url(f"/v1/external/msgs/")
        return requests.post(url, data={
        "room": "2fa2a266-7d97-4147-8f17-1e57105c70ea",
        "text": "hey",
        "direction":"incoming"}, 
        headers=self._header)

    def create_external_msgs_media(self, message_uuid: str):
        url = self._get_url(f"/v1/external/msgs/{message_uuid}/media/")
        return requests.post(url, headers=self._header)

    def update_external_msgs(self, message_uuid):
        url = self._get_url(f"/v1/external/msgs/{message_uuid}")
        return requests.patch(url, headers=self._header)