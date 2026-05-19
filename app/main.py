# import streamlit as st
# import requests
# from streamlit_cookies_manager import EncryptedCookieManager



# GW2_API_ROOT = st.secrets["GW2_API_ROOT"]
# COOKIE_PASSWORD = st.secrets["COOKIE_PASSWORD"]

# cookies = EncryptedCookieManager(
#     prefix="gw2_app",
#     password=COOKIE_PASSWORD,
# )

# if not cookies.ready():
#     st.stop()


# def init_state():
#     # if "api_key" not in st.session_state:
#     #     st.session_state["api_key"] = None

#     if "messages" not in st.session_state:
#         st.session_state.messages = []


# def gw2_get(endpoint: str):
#     api_key = get_api_key()
#     url = f"{GW2_API_ROOT}/{endpoint}"
#     headers = {"Authorization": f"Bearer {api_key}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     return None


# def get_api_key():
#     return cookies.get("gw2_api_key")

# def set_api_key(key: str):
#     cookies["gw2_api_key"] = key
#     cookies.save()

# def clear_api_key():
#     if "gw2_api_key" in cookies:
#         del cookies["gw2_api_key"]
#         cookies.save()

# def load_gw2_api_key():
#     key = st.text_input(
#         "Enter your GW2 API key",
#         type="password",
#     )

#     if key:
#         set_api_key(key)
#         st.rerun()


# def gw2_chat_module():
#     for role, content in st.session_state.messages:
#         st.chat_message(role).write(content)

#     if prompt := st.chat_input("GW2 API endpoint"):
#         st.session_state.messages.append(("user", prompt))
#         data = gw2_get(prompt)
#         st.session_state.messages.append(("assistant", data))
#         st.rerun()


# def main():
#     api_key = get_api_key()

#     if not api_key:
#         load_gw2_api_key()
#     else:
#         gw2_chat_module()


# def navbar():
#     st.sidebar.title("Settings")

#     if st.sidebar.button("Reset API Key"):
#         clear_api_key()
#         st.rerun()

#     if st.sidebar.button("Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()


# if __name__ == "__main__":
#     init_state()
#     main()
#     navbar()




import streamlit as st

from app.auth import auth_screen, sign_out

from app.state import StateManager


def main_app(user_email: str):
    st.title("Supabase Auth Example")
    st.success(f"Welcome, {user_email}!")
    if st.button("Sign Out"):
        sign_out()


if __name__ == "__main__":
    StateManager.init_state()

    if StateManager.is_logged_in():
        main_app(StateManager.get("user_email"))
    else:
        auth_screen()