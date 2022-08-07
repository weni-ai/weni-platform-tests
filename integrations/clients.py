from typing import TYPE_CHECKING

import requests

from authenticators import OIDCPasswordAuth
from clients import ClientInterface, ClientBase
import settings
from settings import IntegrationsSettings


if TYPE_CHECKING:
    from requests import Response


class IntegrationsClient(ClientInterface, ClientBase):

    _base_url = IntegrationsSettings.BASE_URL
    _authenticator = OIDCPasswordAuth()

    def list_apptypes(self, category: str = "channel") -> "Response":
        url = self._get_url("/api/v1/apptypes/")
        response = requests.get(url, headers=self._authenticator.headers, params=dict(category=category))
        response.raise_for_status()

        return response

    def list_apptypes_featureds(self) -> "Response":
        url = self._get_url("/api/v1/apptypes/featureds/")
        response = requests.get(url, headers=self._authenticator.headers)
        response.raise_for_status()

        return response

    def retrieve_apptype(self, apptype_code: str) -> "Response":
        url = self._get_url(f"/api/v1/apptypes/{apptype_code}/")
        response = requests.get(url, headers=self._authenticator.headers)
        response.raise_for_status()

        return response
