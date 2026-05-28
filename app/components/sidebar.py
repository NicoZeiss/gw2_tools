import streamlit as st

from state import StateManager, StateKeys


def logout(state: StateManager):
    state.delete(StateKeys.GW2_API_KEY)
    st.logout()


def set_api_key(state: StateManager):
    key = st.text_input(
        "Enter your GW2 API key",
        type="password",
    )
    if key:
        state.set(StateKeys.GW2_API_KEY, key)
        st.rerun()


def delete_api_key(state: StateManager):
    state.delete(StateKeys.GW2_API_KEY)
    st.rerun()


def sidebar(state: StateManager):
    with st.sidebar:
        st.title(f"Welcome, {st.user.nickname}")
        state.show()

        if state.not_empty(StateKeys.GW2_API_KEY):
            st.success("GW2 API key is set.")
        else:
            st.error("GW2 API key is not set.")
            set_api_key(state)
        
        with st.container(horizontal=True):
            if state.not_empty(StateKeys.GW2_API_KEY):
                if st.button("Delete API Key"):
                    delete_api_key(state)
            if st.button("Logout"):
                logout(state)
