import unittest
import json
import os

import jsonschema

import schemas
from .clients import ConnectFlowsClient
from settings import FlowsSettings


class CreateFlowTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ConnectFlowsClient()
        self.schema = schemas.load("internal/flows/schemas/flows.json")
        self.sample_flow = self.get_sample_flow()

    def get_sample_flow(self):
        file_path = os.path.join(os.path.dirname(__file__), "sample_flow.json")

        with open(file_path, "r") as sample_flow_file:
            return json.loads(sample_flow_file.read())

    def tests_create_flow_response_contracts(self):
        response = self.client.create_flow(FlowsSettings.ORG_UUID, self.sample_flow)
        jsonschema.validate(response.json(), self.schema)
