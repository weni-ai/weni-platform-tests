import unittest

import jsonschema

import settings
import schemas
from .clients import ConnectChatsClient


class ListProjectsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ConnectChatsClient()
        self.schema = schemas.load("internal/chats/schemas/list_projects.json")

    def tests_list_projects_response_contracts(self):
        response = self.client.list_projects()
        jsonschema.validate(response.json(), self.schema)


class RetrieveProjectsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ConnectChatsClient()
        self.schema = schemas.load("internal/chats/schemas/retrieve_project.json")

    def tests_retrieve_project_response_contracts(self):
        response = self.client.retrieve_project(settings.PROJECT_UUID)
        jsonschema.validate(response.json(), self.schema)
