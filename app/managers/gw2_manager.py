import streamlit as st
import requests

from utils import GW2Endpoints


class GW2Manager:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = st.secrets.gw2["GW2_API_ROOT"]

    @property
    def _headers(self):
        return {"Authorization": f"Bearer {self.api_key}"}

    @staticmethod
    def _parse_endpoint(endpoint: GW2Endpoints | str):
        if isinstance(endpoint, GW2Endpoints):
            return endpoint.value
        return endpoint[1:] if endpoint.startswith("/") else endpoint

    def _get_url(self, endpoint: GW2Endpoints | str):
        endpoint = self._parse_endpoint(endpoint)
        return f"{self.base_url}/{endpoint}"

    def get(self, endpoint: GW2Endpoints | str):
        url = self._get_url(endpoint)
        response = requests.get(url, headers=self._headers)
        if response.status_code == 200:
            return response.json()
        return None
