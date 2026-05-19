import streamlit as st
from .auth_manager import AuthManager


def get_auth():
    if "auth" not in st.session_state:
        st.session_state.auth = AuthManager()

    return st.session_state.auth
