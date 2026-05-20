import streamlit as st
from .auth_manager import AuthManager


def auth_screen(auth: AuthManager):
    st.title("Streamlit Supabase Auth App")

    option = st.selectbox("Choose an option", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Sign Up" and st.button("Register"):
        response = auth.sign_up(email, password)
        if response and response.user:
            st.success("Sign up successful! Please log in.")

    if option == "Login" and st.button("Login"):
        success = auth.sign_in(email, password)
        if success:
            st.rerun()
