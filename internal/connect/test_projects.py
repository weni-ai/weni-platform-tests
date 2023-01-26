import unittest

import schemas
import jsonschema

import settings
from .clients import IntegrationsConnectClient


class RetrieveUserAPITokenTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = IntegrationsConnectClient()
        self.schema = schemas.load("internal/connect/schemas/retrieve_user_api_token.json")
    
    def tests_retrieve_user_api_token_response_contracts(self):
        response = self.client.retrieve_user_api_token(settings.PROJECT_UUID, settings.PROJECT_ADMIN_USER_EMAIL)
        print(response.request.url)
        jsonschema.validate(response.json(), self.schema)
