import streamlit as st


class StateManager:

    @staticmethod
    def get(key: str):
        return st.session_state.get(key)

    @staticmethod
    def init_state():
        if "messages" not in st.session_state:
            st.session_state.messages = []
