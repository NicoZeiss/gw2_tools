import streamlit as st

from state import StateManager, StateKeys


def api_key_screen(state: StateManager):
    key = st.text_input(
        "Enter your GW2 API key",
        type="password",
    )
    if key:
        state.set(StateKeys.GW2_API_KEY, key)
        st.rerun()
    st.stop()
