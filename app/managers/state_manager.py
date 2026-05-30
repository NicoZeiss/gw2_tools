import streamlit as st

from typing import Any, Callable

from utils import StateKeys


class StateManager:
    def __init__(self):
        self._state = st.session_state

    @staticmethod
    def _ensure_key(key: StateKeys | str) -> str:
        return key.value if isinstance(key, StateKeys) else key

    def get(
        self,
        key: StateKeys | str,
        default: Any = None,
        default_factory: Callable[[], Any] = None
    ) -> Any:
        key = self._ensure_key(key)
        if key not in self._state:
            if default_factory is not None:
                self._state[key] = default_factory()
            else:
                self._state[key] = default

        return self._state[key]

    def set(self, key: StateKeys | str, value: Any) -> None:
        key = self._ensure_key(key)
        self._state[key] = value

    def delete(self, key: StateKeys | str) -> None:
        key = self._ensure_key(key)
        if key in self._state:
            del self._state[key]

    def exists(self, key: StateKeys | str) -> bool:
        key = self._ensure_key(key)
        return key in self._state

    def not_empty(self, key: StateKeys | str) -> bool:
        key = self._ensure_key(key)
        return bool(self._state.get(key))

    def empty(self, key: StateKeys | str) -> bool:
        return not self.not_empty(key)

    def append(self, key: StateKeys | str, value: Any) -> None:
        key = self._ensure_key(key)
        lst = self.get(key, default_factory=list)
        lst.append(value)

    def update_dict(self, key: StateKeys | str, values: dict) -> None:
        key = self._ensure_key(key)
        d = self.get(key, default_factory=dict)
        d.update(values)

    def clear(self) -> None:
        self._state.clear()

    def show(self) -> None:
        st.json(self._state)
