from decouple import config


ENVIRONMENT = config("ENVIRONMENT", default="develop")

OIDC_OP_TOKEN_ENDPOINT = config("OIDC_OP_TOKEN_ENDPOINT")


# Project settings
PROJECT_UUID = config("PROJECT_UUID")
PROJECT_CLIENT_ID = config("PROJECT_CLIENT_ID")
PROJECT_ADMIN_USER_EMAIL = config("PROJECT_ADMIN_USER_EMAIL")
PROJECT_ADMIN_USER_PASSWORD = config("PROJECT_ADMIN_USER_PASSWORD")


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


class FlowsSettings(object):

    BASE_URL = config("FLOWS_BASE_URL")
    ORG_UUID = config("FLOWS_ORG_UUID")


class ChatsSettings(object):

    BASE_URL = config("CHATS_BASE_URL")
    OIDC_RP_CLIENT_ID = config("CHATS_OIDC_RP_CLIENT_ID")
    OIDC_RP_CLIENT_SECRET = config("CHATS_OIDC_RP_CLIENT_SECRET")
    SECTOR_UUID = config("CHATS_SECTOR_UUID")
    QUEUE_UUID = config("CHATS_QUEUE_UUID")
