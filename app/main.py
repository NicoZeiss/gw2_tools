# def gw2_get(endpoint: str):
#     api_key = get_api_key()
#     url = f"{GW2_API_ROOT}/{endpoint}"
#     headers = {"Authorization": f"Bearer {api_key}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     return None


import streamlit as st
from typing import NamedTuple

from app_service import AppService
from components import app_sidebar, admin_dialog
from screens import auth_screen, api_key_screen
from utils import StateKeys


def handle_prompt(service: AppService, prompt: str):
    messages = service.state.get(
        StateKeys.MESSAGES,
        default_factory=list,
    )

    service.state.set(
        StateKeys.MESSAGES,
        messages + [("user", prompt)],
    )
    data = service.gw2.get(prompt)
    service.state.set(
        StateKeys.MESSAGES,
        messages + [("user", prompt), ("assistant", data)],
    )
    st.rerun()


def gw2_chat_module(service: AppService):
    messages = service.state.get(
        StateKeys.MESSAGES,
        default_factory=list,
    )
    for role, content in messages:
        st.chat_message(role).write(content)


class EndpointParam(NamedTuple):
    param: str
    separator: str = "/"


def endpoint_example(endpoint: str, params: list[EndpointParam] | None = None, icon: str = "⚙️"):
    with st.container(horizontal=True, gap="xxsmall", vertical_alignment="center"):
        st.write(icon)
        st.badge("/", color="green")
        st.badge(endpoint, color="green")

        if params:
            for param in params:
                st.badge(param.separator, color="orange")
                st.badge(param.param, color="orange")


def main_app(service: AppService):

    if not service.user:
        auth_screen()

    app_sidebar(service)

    if not service.api_key:
        api_key_screen(service)

    col1, col2 = st.columns([2, 5])
    with col1:
        with st.container(gap="xxsmall"):
            endpoint_example("account", icon="⚙️")
            endpoint_example("characters", icon="🧙")
            endpoint_example(
                "characters",
                icon="🧙",
                params=[EndpointParam(param="{CHARACTER_NAME}")],
            )
    with col2:
        chat_area = st.container(height=600)

        with chat_area:
            gw2_chat_module(service)

    if prompt := st.chat_input("GW2 API endpoint"):
        handle_prompt(service, prompt)


if __name__ == "__main__":
    st.set_page_config(layout="wide")

    service = AppService()
    # admin_dialog(service.state)

    main_app(service)
