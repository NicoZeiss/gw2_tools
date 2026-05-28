import streamlit as st


def sidebar():
    st.sidebar.title("Settings")
    with st.sidebar:
        if st.button("Logout"):
            st.logout()
