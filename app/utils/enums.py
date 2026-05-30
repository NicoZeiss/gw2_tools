from enum import Enum


class StateKeys(Enum):
    MESSAGES = "messages"
    GW2_API_KEY = "gw2_api_key"
    DB_USER_ID = "db_user_id"


class SupabaseTables(Enum):
    USERS = "users"
    USER_SETTINGS = "user_settings"


class GW2Endpoints(Enum):
    ACCOUNT = "account"
