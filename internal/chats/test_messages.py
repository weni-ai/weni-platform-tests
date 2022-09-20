import unittest

import jsonschema

import settings
import schemas
from .clients import FlowsChatsClient

class ListMessagesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = FlowsChatsClient()
        self.schema = schemas.load("internal/chats/schemas/list_message.json")

    def tests_retrieve_rooms_response_contracts(self):
        response = self.client.list_external_msgs(settings.ChatsSettings.ROOM_UUID)
        jsonschema.validate(response.json(), self.schema)

class CreateMessageTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = FlowsChatsClient()
        self.schema = schemas.load("internal/chats/schemas/create_message.json")

    def tests_create_rooms_response_contracts(self):
        response = self.client.create_external_msgs()
        jsonschema.validate(response.json(), self.schema)

class CreateMessageMediaTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = FlowsChatsClient()
        self.schema = schemas.load("internal/chats/schemas/create_message_media.json")

    def tests_create_rooms_response_contracts(self):
        response = self.client.create_external_msgs_media(settings.PROJECT_UUID)
        jsonschema.validate(response.json(), self.schema)


