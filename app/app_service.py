from managers import (
    StateManager,
    AuthManager,
    SupabaseManager,
)
from utils import StateKeys


class AppService:
    def __init__(self):
        self.state = StateManager()
        self.auth = AuthManager()
        self.db = SupabaseManager()

        self.user = self._load_user()
        self.api_key = self._load_api_key()

    @property
    def user_id(self) -> str | None:
        return self.state.get(StateKeys.DB_USER_ID)

    def _load_user(self):
        if not self.auth.is_authenticated:
            return None

        user = self.db.get_or_create_user(
            auth0_user_id=self.auth.auth0_user_id,
            email=self.auth.email,
        )
        self.state.set(StateKeys.DB_USER_ID, user["id"])
        return user

    def _load_api_key(self):
        if not self.user_id:
            return None

        api_key = self.db.get_gw2_api_key(self.user_id)
        if api_key:
            self.state.set(StateKeys.GW2_API_KEY, api_key)
        return api_key
