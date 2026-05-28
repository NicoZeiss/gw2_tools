import streamlit as st


def sidebar():
    with st.sidebar:
        st.title("This is a title")
        if st.button("Logout"):
            st.logout()
