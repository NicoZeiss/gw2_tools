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
from supabase import create_client, Client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def sign_up(email: str, password: str):
    try:
        user = supabase.auth.sign_up({"email": email, "password": password})
        return user
    except Exception as e:
        st.error(f"Error signing up: {e}")


def sign_in(email: str, password: str):
    try:
        user = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return user
    except Exception as e:
        st.error(f"Error signing in: {e}")


def sign_out():
    try:
        supabase.auth.sign_out()
        st.session_state.user_email = None
        st.rerun()
    except Exception as e:
        st.error(f"Error signing out: {e}")


def main_app(user_email: str):
    st.title("Supabase Auth Example")
    st.success(f"Welcome, {user_email}!")
    if st.button("Sign Out"):
        sign_out()

def auth_screen():
    st.title("Streamlit Supabase Auth App")
    option = st.selectbox("Choose an option", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Sign Up" and st.button("Register"):
        user = sign_up(email, password)
        if user and user.user:
            st.success("Sign up successful! Please log in.")

    if option == "Login" and st.button("Login"):
        user = sign_in(email, password)
        if user and user.user:
            st.session_state.user_email = user.user.email
            st.success(f"Welcome back, {user.user.email}!")
            st.rerun()


if __name__ == "__main__":
    if "user_email" not in st.session_state:
        st.session_state.user_email = None

    if st.session_state.user_email:
        main_app(st.session_state.user_email)
    else:
        auth_screen()