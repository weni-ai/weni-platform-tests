from decouple import config, Config, RepositoryEnv


# TODO: Configure default authentication_class to clients
# TODO: Get .env dinamicaly based on ENVIORNMENT

# Environment settings

ENVIRONMENT_LOCAL = "local"
ENVIRONMENT_DEVELOP = "develop"
ENVIRONMENT_STAGING = "staging"
ENVIRONMENT_PRODUCTION = "production"

ENVIRONMENTS = {
    ENVIRONMENT_LOCAL: ".env-local",
    ENVIRONMENT_DEVELOP: ".env-develop",
    ENVIRONMENT_STAGING: ".env-staging",
    ENVIRONMENT_PRODUCTION: ".env-production",
}

ENVIRONMENT = config("ENVIRONMENT", default="develop")

assert (
    ENVIRONMENT in ENVIRONMENTS
), f"The environment `{ENVIRONMENT}` is not included in the list of accepted environmments"

if ENVIRONMENT == ENVIRONMENT_LOCAL:
    config = Config(RepositoryEnv(ENVIRONMENTS[ENVIRONMENT]))


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
