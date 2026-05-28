import streamlit as st



def sidebar():
    st.sidebar.title("Settings")
    if st.button("Logout"):
        st.logout()
