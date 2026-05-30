# def gw2_get(endpoint: str):
#     api_key = get_api_key()
#     url = f"{GW2_API_ROOT}/{endpoint}"
#     headers = {"Authorization": f"Bearer {api_key}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     return None


import streamlit as st

from app_service import AppService
from components import app_sidebar, admin_dialog
from screens import auth_screen, api_key_screen
from utils import StateKeys


def gw2_chat_module(service: AppService):
    messages = service.state.get(
        StateKeys.MESSAGES,
        default_factory=list,
    )

    for role, content in messages:
        st.chat_message(role).write(content)

    if prompt := st.chat_input("GW2 API endpoint"):
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


def main_app(service: AppService):

    if not service.user:
        auth_screen()

    app_sidebar(service)

    if not service.api_key:
        api_key_screen(service)

    gw2_chat_module(service)


if __name__ == "__main__":
    service = AppService()
    # admin_dialog(service.state)

    main_app(service)
