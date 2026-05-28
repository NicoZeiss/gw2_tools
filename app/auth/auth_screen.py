import streamlit as st


def auth_screen():
    with st.container(horizontal_alignment="center"):
        st.title("Welcome on GW2-Tools App",
                 text_alignment="center", anchor=False)
        if st.button("Please, login to continue", type="primary"):
            st.login("auth0")
    st.stop()
