import streamlit as st
import requests
from supabase import create_client


GW2_API_ROOT = st.secrets["GW2_API_ROOT"]


def init_state():
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = None


def gw2_get(endpoint: str):
    url = f"{GW2_API_ROOT}/{endpoint}"
    headers = {"Authorization": f"Bearer {st.session_state['api_key']}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def load_gw2_api_key():
    st.session_state["api_key"] = st.text_input(
        "Enter your GW2 API key",
        type="password",
        key="api_key_input",
    )


def gw2_chat_module():
    messages = st.container(height="stretch")
    if prompt := st.chat_input("GW2 API endpoint"):
        messages.chat_message("user").write(prompt)
        data = gw2_get(prompt)
        messages.chat_message("assistant").write(data)


def main():
    if st.session_state["api_key"] is None:
        load_gw2_api_key()
    else:
        gw2_chat_module()


if __name__ == "__main__":
    init_state()
    main()
