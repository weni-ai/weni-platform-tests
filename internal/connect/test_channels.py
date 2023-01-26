import unittest

import jsonschema

import schemas
from .clients import IntegrationsConnectClient


class ListChannelsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = IntegrationsConnectClient()
        self.schema = schemas.load("internal/connect/schemas/list_channels.json")

    def tests_list_channels_response_contracts(self):
        response = self.client.list_channels("WAC")
        jsonschema.validate(response.json(), self.schema)
