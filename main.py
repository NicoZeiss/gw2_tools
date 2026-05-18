import streamlit as st
import requests
from supabase import create_client


GW2_API_ROOT = st.secrets["GW2_API_ROOT"]


def init_state():
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = None

    if "messages" not in st.session_state:
        st.session_state.messages = []


def gw2_get(endpoint: str):
    url = f"{GW2_API_ROOT}/{endpoint}"
    headers = {"Authorization": f"Bearer {st.session_state.api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def load_gw2_api_key():
    key = st.text_input(
        "Enter your GW2 API key",
        type="password",
    )
    if key:
        st.session_state.api_key = key
        st.rerun()


def gw2_chat_module():
    for role, content in st.session_state.messages:
        st.chat_message(role).write(content)

    # Input utilisateur
    if prompt := st.chat_input("GW2 API endpoint"):

        st.session_state.messages.append(("user", prompt))

        data = gw2_get(prompt)

        st.session_state.messages.append(("assistant", data))

        st.rerun()


def main():
    if st.session_state.api_key is None:
        load_gw2_api_key()
    else:
        gw2_chat_module()


def navbar():
    if st.sidebar.button("Reset API Key"):
        st.session_state.api_key = None
        st.rerun()
    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()


if __name__ == "__main__":
    init_state()
    main()
    navbar()
