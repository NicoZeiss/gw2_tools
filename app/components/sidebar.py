import streamlit as st

from auth import sign_out

from state import StateManager


def sidebar():
    st.sidebar.title("Settings")

    if StateManager.is_logged_in():
        if st.sidebar.button("Sign Out"):
            sign_out()
