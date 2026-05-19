import streamlit as st

from app.auth import sign_out

from app.state import StateManager


def sidebar():
    st.sidebar.title("Settings")

    if StateManager.is_logged_in():
        if st.sidebar.button("Sign Out"):
            sign_out()