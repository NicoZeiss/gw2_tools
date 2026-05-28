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

            with st.container(horizontal=True, horizontal_alignment="right"):
                if st.button("Cancel"):
                    state.set("show_admin_popup", False)
                    st.rerun()
                if not state.get("is_admin", False):
                    if st.button("Login", type="primary"):
                        if password == st.secrets["ADMIN_PASSWORD"]:
                            state.set("is_admin", True)
                            state.set("show_admin_popup", False)
                            st.rerun()
                else:
                    if st.button("Logout", type="primary"):
                        state.set("is_admin", False)
                        state.set("show_admin_popup", False)
                        st.rerun()

        _admin_dialog()
