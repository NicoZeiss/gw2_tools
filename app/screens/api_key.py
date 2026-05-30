import streamlit as st

from app_service import AppService
from state import StateKeys


def api_key_screen(service: AppService):
    key = st.text_input(
        "Enter your GW2 API key",
        type="password",
    )
    if key:
        service.db.set_gw2_api_key(service.user_id, key)
        st.rerun()
    st.stop()
