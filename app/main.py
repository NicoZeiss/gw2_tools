# def gw2_get(endpoint: str):
#     api_key = get_api_key()
#     url = f"{GW2_API_ROOT}/{endpoint}"
#     headers = {"Authorization": f"Bearer {api_key}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     return None


# def gw2_chat_module():
#     for role, content in st.session_state.messages:
#         st.chat_message(role).write(content)

#     if prompt := st.chat_input("GW2 API endpoint"):
#         st.session_state.messages.append(("user", prompt))
#         data = gw2_get(prompt)
#         st.session_state.messages.append(("assistant", data))
#         st.rerun()

import streamlit as st

from screens import auth_screen, api_key_screen
from components import app_sidebar, admin_dialog

from state import StateManager, StateKeys


def main_app(state: StateManager):
    if not st.user.is_logged_in:
        auth_screen()

    app_sidebar(state)

    if state.empty(StateKeys.GW2_API_KEY):
        api_key_screen(state)

    st.write("User:")
    st.json(st.user)


if __name__ == "__main__":
    state = StateManager()
    main_app(state)
    # admin_dialog(state)
