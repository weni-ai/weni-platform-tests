import unittest

import jsonschema

import settings
import schemas
from .clients import FlowsChatsClient

class RetrieveRoomsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = FlowsChatsClient()
        self.schema = schemas.load("internal/chats/schemas/retrieve_room.json")

    def tests_retrieve_rooms_response_contracts(self):
        response = self.client.retrieve_external_room(settings.PROJECT_UUID)
        jsonschema.validate(response.json(), self.schema)

class CreateRoomsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = FlowsChatsClient()
        self.schema = schemas.load("internal/chats/schemas/create_room.json")

    def tests_create_rooms_response_contracts(self):
        response = self.client.create_external_room()
        jsonschema.validate(response.json(), self.schema)

class UpdateRoomsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = FlowsChatsClient()
        self.schema = schemas.load("internal/chats/schemas/update_room.json")

    def tests_update_rooms_response_contracts(self):
        response = self.client.update_external_room(settings.PROJECT_UUID)
        jsonschema.validate(response.json(), self.schema)

class CloseRoomsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = FlowsChatsClient()
        self.schema = schemas.load("internal/chats/schemas/close_room.json")

    def tests_update_rooms_response_contracts(self):
        response = self.client.close_external_room(settings.PROJECT_UUID)
        jsonschema.validate(response.json(), self.schema)