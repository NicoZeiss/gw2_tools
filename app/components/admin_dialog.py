import streamlit as st
from streamlit_shortcuts import shortcut_button

from state import StateManager


def admin_dialog(state: StateManager):
    if shortcut_button(
        "",
        shortcut="ctrl+alt+t",
        key="admin_shortcut"
    ):
        state.set("show_admin_popup", True)


    if state.get("show_admin_popup", False):
        @st.dialog("Admin Access")
        def _admin_dialog():

            password = st.text_input(
                "Password",
                type="password"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Login"):

                    if password == st.secrets["ADMIN_PASSWORD"]:
                        state.set("is_admin", True)
                        state.set("show_admin_popup", False)
                        st.rerun()

                    else:
                        st.error("Invalid password")

            with col2:
                if st.button("Cancel"):
                    state.set("show_admin_popup", False)
                    st.rerun()

        _admin_dialog()
