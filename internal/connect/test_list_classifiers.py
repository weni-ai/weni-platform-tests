import unittest

import jsonschema

import settings
import schemas
from .clients import AIConnectClient


class ListClassifiersTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = AIConnectClient()
        self.schema = schemas.load("internal/connect/schemas/list_classifiers.json")

    def tests_list_classifiers_response_contracts(self):
        response = self.client.list_classifiers(settings.PROJECT_UUID, settings.PROJECT_ADMIN_USER_EMAIL)
        jsonschema.validate(response.json(), self.schema)
