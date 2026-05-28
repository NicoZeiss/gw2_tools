import streamlit as st

from state import StateManager, StateKeys


def logout(state: StateManager):
    state.delete(StateKeys.GW2_API_KEY)
    st.logout()


def sidebar(state: StateManager):
    with st.sidebar:
        st.title(f"Welcome, {st.user.nickname}")

        if not state.exists(StateKeys.GW2_API_KEY):
            key = st.text_input(
                "Enter your GW2 API key",
                type="password",
            )
            if key:
                state.set(StateKeys.GW2_API_KEY, key)
                st.rerun()
        else:
            st.success("GW2 API key is set.")

        if st.button("Logout"):
            logout(state)
