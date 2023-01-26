import unittest

import jsonschema

import schemas
from .clients import ConnectFlowsClient
from authenticators import OIDCPasswordAuth
import settings


class UserAPITokenTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ConnectFlowsClient()
        self.schema = schemas.load("internal/flows/schemas/users.json")

    def tests_retrieve_user_api_token_response_contracts(self):
        response = self.client.retrieve_user_api_token("sandro.meireles@weni.ai", settings.FlowsSettings.ORG_UUID)
        self.assertEqual(response.status_code, 200)
        jsonschema.validate(response.json(), self.schema)
