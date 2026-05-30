import streamlit as st

from app_service import AppService
from managers import StateManager
from utils import StateKeys


def logout_btn(state: StateManager):
    if st.button("Logout"):
        state.delete(StateKeys.GW2_API_KEY)
        st.logout()


def del_api_key_btn(service: AppService):
    if bool(service.api_key):
        if st.button("Delete API Key"):
            service.delete_api_key()
            st.rerun()


def _app_sidebar(service: AppService):
    st.title(f"Welcome, {st.user.nickname}")

    with st.container(horizontal=True):
        del_api_key_btn(service)
        logout_btn(service.state)

    if service.state.get("is_admin", False):
        st.json(service.state._state)


def app_sidebar(service: AppService):
    with st.sidebar:
        _app_sidebar(service)
