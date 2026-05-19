import streamlit as st


class StateManager:

    @staticmethod
    def get(key: str):
        return st.session_state.get(key)

    @staticmethod
    def init_state():
        if "user_email" not in st.session_state:
            st.session_state.user_email = None
        if "messages" not in st.session_state:
            st.session_state.messages = []

    @staticmethod
    def is_logged_in() -> bool:
        return st.session_state.user_email is not None
