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
