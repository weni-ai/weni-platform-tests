import unittest

import jsonschema

import schemas
from .clients import ChatsFlowsClient
import settings


class BaseQueueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ChatsFlowsClient()

    def _create_queue(self):
        return self.client.create_queue(settings.ChatsSettings.SECTOR_UUID, "Fake name", settings.ChatsSettings.QUEUE_UUID)


class CreateQueueTestCase(BaseQueueTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.schema = schemas.load("internal/flows/schemas/queues.json")

    def tests_create_queue_response_contracts(self):
        response = self._create_queue()
        self.assertEqual(response.status_code, 201)
        jsonschema.validate(response.json(), self.schema)


class UpdateQueueTestCase(BaseQueueTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.schema = schemas.load("internal/flows/schemas/queues.json")

    def tests_update_queue_response_contracts(self):
        self._create_queue()

        response = self.client.update_queue(settings.ChatsSettings.SECTOR_UUID, settings.ChatsSettings.QUEUE_UUID, "Changed name")
        self.assertEqual(response.status_code, 206)
        jsonschema.validate(response.json(), self.schema)


class DestroyQueueTestCase(BaseQueueTestCase):
    def setUp(self) -> None:
        super().setUp()

    def tests_update_queue_response_contracts(self):
        self._create_queue()

        response = self.client.destroy_queue(settings.ChatsSettings.SECTOR_UUID, settings.ChatsSettings.QUEUE_UUID)
        self.assertEqual(response.status_code, 204)
