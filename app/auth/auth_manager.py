import streamlit as st
from supabase import create_client, Client


SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]


@st.cache_resource
def get_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)


class AuthManager:

    def __init__(self):
        self.supabase: Client = get_supabase()

        self._load_session()

    def _load_session(self):
        session = self.supabase.auth.get_session()

        if session and session.user:
            self._set_session(session.user, session)
        else:
            self._clear_session()

    def _set_session(self, user, session):
        st.session_state.authenticated = True
        st.session_state.user = user
        st.session_state.session = session

    def _clear_session(self):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.session_state.session = None

    def sign_up(self, email: str, password: str):
        try:
            response = self.supabase.auth.sign_up(
                {"email": email, "password": password})
            return response
        except Exception as e:
            st.error(f"Error signing up: {e}")
            return None

    def sign_in(self, email: str, password: str):
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password,
            })
            session = response.session
            user = response.user

            self._set_session(user, session)
            return True

        except Exception as e:
            st.error(f"Error signing in: {e}")
            return False

    def sign_out(self):
        try:
            self.supabase.auth.sign_out()
        except Exception as e:
            pass

        self._clear_session()
        st.rerun()

    @property
    def is_authenticated(self) -> bool:
        return st.session_state.get(
            "authenticated",
            False
        )

    @property
    def user(self):
        return st.session_state.get("user")

    @property
    def email(self):
        user = self.user
        return getattr(user, "email", None)
