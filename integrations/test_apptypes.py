import unittest

import jsonschema

import schemas
from .clients import IntegrationsClient


class ListApptypesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = IntegrationsClient()
        self.schema = schemas.load("integrations/schemas/list_apptypes.json")

    def test_list_apptypes_response_contracts(self):
        response = self.client.list_apptypes()
        jsonschema.validate(response.json(), self.schema)


class ListAppTypesFeaturedsTestCase(unittest.TestCase):
    
    def setUp(self):
        self.client = IntegrationsClient()
        self.schema = schemas.load("integrations/schemas/list_apptypes.json")
    
    def test_list_apptypes_featureds_response_contracts(self):
        response = self.client.list_apptypes_featureds()
        jsonschema.validate(response.json(), self.schema)


class RetrieveAppTypeTestCase(unittest.TestCase):
    def setUp(self):
        self.client = IntegrationsClient()
        self.schema = schemas.load("integrations/schemas/retrieve_apptype.json")

    def test_retrieve_apptype_response_contracts(self):
        response = self.client.retrieve_apptype("wwc")
        jsonschema.validate(response.json(), self.schema)
