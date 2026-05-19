import streamlit as st

from .supabase_client import sign_up, sign_in

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
