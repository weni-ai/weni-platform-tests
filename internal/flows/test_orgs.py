import unittest

import jsonschema

import schemas
import settings
from .clients import ConnectFlowsClient
from authenticators import OIDCPasswordAuth


class CreateTemplateOrgTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ConnectFlowsClient()
        self.schema = schemas.load("internal/flows/schemas/template_orgs.json")

    def tests_create_template_org_response_contracts(self):
        response = self.client.create_template_org(settings.PROJECT_ADMIN_USER_EMAIL, "Projeto de teste", "America/Maceio")
        jsonschema.validate(response.json(), self.schema)

    def test_returns_bad_request_status_when_request_without_permission(self):
        self.client._authenticator = OIDCPasswordAuth()
        response = self.client.create_template_org(settings.PROJECT_ADMIN_USER_EMAIL, "Projeto de teste", "America/Maceio")
        self.assertEqual(response.status_code, 403)
