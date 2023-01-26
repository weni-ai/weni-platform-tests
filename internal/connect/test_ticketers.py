import unittest

import jsonschema

import settings
import schemas
from .clients import ChatsConnectClient


class CreateTicketerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ChatsConnectClient()
        self.schema = schemas.load("internal/connect/schemas/create_ticketers.json")

    def tests_create_ticketer_response_contracts(self):
        response = self.client.create_ticketer(settings.PROJECT_UUID, "WAC", "FAKE", {})
        jsonschema.validate(response.json(), self.schema)
