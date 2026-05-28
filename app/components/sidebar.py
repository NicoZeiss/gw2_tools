import streamlit as st

from state import StateManager, StateKeys


def logout(state: StateManager):
    state.delete(StateKeys.GW2_API_KEY)
    st.logout()


def sidebar(state: StateManager):
    with st.sidebar:
        st.title("This is a title")

        st.write(f"User: {st.user.nickname}")

        if st.button("Logout"):
            logout(state)
