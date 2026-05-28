import streamlit as st
from streamlit_shortcuts import shortcut_button

from state import StateManager


def _action_btn(state: StateManager, valid_password=False):
    if not state.get("is_admin", False):
        if st.button("Login", type="primary"):
            if valid_password:
                state.set("is_admin", True)
                state.set("show_admin_popup", False)
                st.rerun()
    else:
        if st.button("Logout", type="primary"):
            state.set("is_admin", False)
            state.set("show_admin_popup", False)
            st.rerun()


@st.dialog("Admin Access")
def _admin_dialog(state: StateManager):
    valid_password = False
    if not state.get("is_admin", False):
        password = st.text_input(
            "Password",
            type="password"
        )
        valid_password = password == st.secrets["ADMIN_PASSWORD"]

    with st.container(horizontal=True, horizontal_alignment="right"):
        if st.button("Cancel"):
            state.set("show_admin_popup", False)
            st.rerun()
        _action_btn(state, valid_password)


def admin_dialog(state: StateManager):
    if shortcut_button(
        "",
        shortcut="ctrl+alt+t",
        key="admin_shortcut"
    ):
        state.set("show_admin_popup", True)

    if state.get("show_admin_popup", False):
        _admin_dialog(state)
