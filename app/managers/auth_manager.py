import streamlit as st


class AuthManager:

    def __init__(self):
        self.user = st.user

    @property
    def is_authenticated(self) -> bool:
        return self.user.is_logged_in

    @property
    def auth0_user_id(self) -> str | None:
        if not self.is_authenticated:
            return None
        return self.user.get("sub")

    @property
    def email(self) -> str | None:
        if not self.is_authenticated:
            return None
        return self.user.get("email")
