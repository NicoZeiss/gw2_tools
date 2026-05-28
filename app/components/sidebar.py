import streamlit as st

from state import StateManager, StateKeys


def logout_btn(state: StateManager):
    if st.button("Logout"):
        state.delete(StateKeys.GW2_API_KEY)
        st.logout()


def del_api_key_btn(state: StateManager):
    if state.not_empty(StateKeys.GW2_API_KEY):
        if st.button("Delete API Key"):
            state.delete(StateKeys.GW2_API_KEY)
            st.rerun()


def _app_sidebar(state: StateManager):
    st.title(f"Welcome, {st.user.nickname}")

    with st.container(horizontal=True):
        del_api_key_btn(state)
        logout_btn(state)

    if state.get("is_admin", False):
        st.json(state._state)


def app_sidebar(state: StateManager):
    with st.sidebar:
        _app_sidebar(state)
