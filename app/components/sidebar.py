import streamlit as st

from app_service import AppService
from managers import StateManager
from utils import StateKeys


def logout_btn(state: StateManager):
    if st.button("Logout"):
        state.delete(StateKeys.GW2_API_KEY)
        st.logout()


def del_api_key_btn(service: AppService, type="secondary"):
    if bool(service.api_key):
        if st.button("Delete API Key", type=type):
            service.delete_api_key()
            st.rerun()


gw2_permissions = set([
    "account",
    "characters",
    "inventories",
    "progression",
    "pvp",
    "tradingpost",
    "wvw",
    "wallet",
    "guilds",
    "unlocks",
    "builds",
])


def _app_sidebar(service: AppService):
    st.title(f"Welcome, {st.user.nickname.capitalize()}!")
    logout_btn(service.state)

    if service.api_key:
        st.divider()
        st.text_input(
            "GW2 API Key",
            value=service.api_key,
            disabled=True,
            type="password",
        )
        permissions = service.gw2.get("tokeninfo")["permissions"]
        with st.container(horizontal=True, gap="xxsmall"):
            for perm in gw2_permissions:
                st.badge(
                    perm,
                    color=("green" if perm in permissions else "red"),
                )
        del_api_key_btn(service)
        st.divider()

    if service.state.get("is_admin", False):
        st.json(service.state._state)


def app_sidebar(service: AppService):
    with st.sidebar:
        _app_sidebar(service)
