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

