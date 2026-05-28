import streamlit as st

from state import StateManager, StateKeys


def logout(state: StateManager):
    state.delete(StateKeys.GW2_API_KEY)
    st.logout()


def sidebar(state: StateManager):
    with st.sidebar:
        st.title("This is a title")

        st.write(f"Welcome, {st.user.nickname}")
        st.write(f"Your GW2 API key: {state.get(StateKeys.GW2_API_KEY)}")

        if st.button("Logout"):
            logout(state)
