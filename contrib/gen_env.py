"""
Responsible for speeding up the generation of a local '.env' configuration file.
OBS: Run in development environment only
"""

import os

CONFIG_STRING = f"""
# General project settings
ENVIRONMENT="develop"
OIDC_OP_TOKEN_ENDPOINT="You need to configure"

PROJECT_UUID="You need to configure"
PROJECT_ADMIN_USER_EMAIL="You need to configure"
PROJECT_ADMIN_USER_PASSWORD="You need to configure"

# Integrations settings
INTEGRATIONS_BASE_URL=""
INTEGRATIONS_OIDC_RP_CLIENT_ID="You need to configure"
INTEGRATIONS_OIDC_RP_CLIENT_SECRET="You need to configure"

# Connect settings
CONNECT_BASE_URL=""
CONNECT_OIDC_RP_CLIENT_ID="You need to configure"
CONNECT_OIDC_RP_CLIENT_SECRET="You need to configure"

# Artificial intelligence settings
AI_BASE_URL=""
AI_OIDC_RP_CLIENT_ID="You need to configure"
AI_OIDC_RP_CLIENT_SECRET="You need to configure"

# Flows settings
FLOWS_BASE_URL=""
FLOWS_ORG_UUID="You need to configure"

# Chats settings
CHATS_BASE_URL=""
CHATS_OIDC_RP_CLIENT_ID="You need to configure"
CHATS_OIDC_RP_CLIENT_SECRET="You need to configure"

""".strip()


def main():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")

    # TODO: Validate if file already exists

    with open(env_path, "w") as configfile:
        configfile.write(CONFIG_STRING)


if __name__ == "__main__":
    main()
