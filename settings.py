from decouple import config


ENVIRONMENT = config("ENVIRONMENT", default="develop")

OIDC_OP_TOKEN_ENDPOINT = config("OIDC_OP_TOKEN_ENDPOINT")

PROJECT_UUID = config("PROJECT_UUID")


class IntegrationsSettings(object):
    BASE_URL = config("INTEGRATIONS_BASE_URL")
    OIDC_RP_CLIENT_ID = config("INTEGRATIONS_OIDC_RP_CLIENT_ID")
    OIDC_RP_CLIENT_SECRET = config("INTEGRATIONS_OIDC_RP_CLIENT_SECRET")


class ConnectSettings(object):
    BASE_URL = config("CONNECT_BASE_URL")
    OIDC_RP_CLIENT_ID = config("CONNECT_OIDC_RP_CLIENT_ID")
    OIDC_RP_CLIENT_SECRET = config("CONNECT_OIDC_RP_CLIENT_SECRET")


class AISettings(object):

    BASE_URL = config("AI_BASE_URL")
    OIDC_RP_CLIENT_ID = config("AI_OIDC_RP_CLIENT_ID")
    OIDC_RP_CLIENT_SECRET = config("AI_OIDC_RP_CLIENT_SECRET")
