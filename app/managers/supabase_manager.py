import streamlit as st

from supabase import create_client, Client

from utils import SupabaseTables


class SupabaseManager:
    def __init__(self):
        self.client: Client = create_client(
            st.secrets.supabase["SUPABASE_URL"],
            st.secrets.supabase["SUPABASE_SERVICE_ROLE_SECRET"],
        )

    def _create_user(self, auth0_user_id: str, email: str | None = None):
        created = (
            self.client
            .table(SupabaseTables.USERS.value)
            .insert({
                "auth0_user_id": auth0_user_id,
                "email": email,
            })
            .execute()
        )
        return created.data[0]

    def get_or_create_user(
        self,
        auth0_user_id: str,
        email: str | None = None,
    ):
        existing = (
            self.client
            .table(SupabaseTables.USERS.value)
            .select("*")
            .eq("auth0_user_id", auth0_user_id)
            .execute()
        )

        if existing.data:
            return existing.data[0]

        return self._create_user(auth0_user_id, email)

    def get_gw2_api_key(self, user_id: str) -> str | None:
        result = (
            self.client
            .table(SupabaseTables.USER_SETTINGS.value)
            .select("gw2_api_key")
            .eq("user_id", user_id)
            .execute()
        )

        if not result.data:
            return None

        return result.data[0]["gw2_api_key"]

    def set_gw2_api_key(self, user_id: str, api_key: str) -> None:
        (
            self.client
            .table(SupabaseTables.USER_SETTINGS.value)
            .upsert({"user_id": user_id, "gw2_api_key": api_key})
            .execute()
        )

    def delete_gw2_api_key(self, user_id: str) -> None:
        (
            self.client
            .table(SupabaseTables.USER_SETTINGS.value)
            .update({"gw2_api_key": None})
            .eq("user_id", user_id)
            .execute()
        )
