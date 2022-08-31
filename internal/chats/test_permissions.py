import unittest

import jsonschema

import settings
import schemas
from .clients import ConnectChatsClient


class RetrievePermissionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ConnectChatsClient()
        self.schema = schemas.load("internal/chats/schemas/retrieve_permission.json")

    def tests_retrieve_project_response_contracts(self):
        response = self.client.retrieve_permissions(settings.ChatsSettings.PROJECT_PERMISSION_UUID)
        jsonschema.validate(response.json(), self.schema)


class ListPermissionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ConnectChatsClient()
        self.schema = schemas.load("internal/chats/schemas/list_permission.json")

    def tests_retrieve_project_response_contracts(self):
        response = self.client.list_permissions(settings.PROJECT_UUID)
        jsonschema.validate(response.json(), self.schema)
