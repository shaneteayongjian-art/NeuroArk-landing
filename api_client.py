"""
Thin HTTP client for the poker tournament API.

Encapsulates authentication and request logic for joining a game and submitting
actions.  The server uses Basic Auth and a blocking API design; these
functions mirror that behaviour by waiting until the server responds.  Timeouts
are set slightly above the tournament timeout to avoid early termination.
"""
from __future__ import annotations

import json
from typing import Any, Dict

import requests
from requests.auth import HTTPBasicAuth

from utils.logger import log


class APIClient:
    """Wrapper around the tournament's REST API."""

    def __init__(self, base_url: str, username: str, password: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, password)
        self.session.headers.update({"Content-Type": "application/json"})

    def join(self, token: str | None) -> Dict[str, Any]:
        """Join a game. If token is provided, use /game/join/{token}; else /game/join."""
        # 允许无 token：无 token 走 /game/join；有 token 走 /game/join/{token}
        path = f"/game/join/{token}" if token else "/game/join"
        url  = f"{self.base_url}{path}"

        # 如果你的构造函数里已经设置了 self.session.auth，就不需要额外传 auth
        # 这里保持和你原来代码一致的调用方式
        resp = self.session.get(url, timeout=65)
        resp.raise_for_status()
        return resp.json()

    path = f"/game/join/{token}" if token else "/game/join"
    url  = f"{self.base_url}{path}"
    # 65s > 60s grace period
    response = self.session.get(url, timeout=65)
    response.raise_for_status()
    return response.json()

        """Join a game or rejoin after each action.

        Uses a blocking GET request which returns only when the game state
        requires the player's attention (i.e., when it is this bot's turn).

        Args:
            token: The one‑time registration token for the tournament.

        Returns:
            Parsed JSON dictionary of the server response.
        """
        url = f"{self.base_url}/game/join/{token}"
        # The timeout must exceed the server's blocking duration; 65 seconds is
        # chosen to be above the typical 60 second grace period.
        response = self.session.get(url, timeout=65)
        response.raise_for_status()
        return response.json()

    def act(self, action_payload: Dict[str, Any]) -> Dict[str, Any]:
        """Submit an action to the server and wait for the next state.

        This call blocks until the server has processed the action and either
        the game ends or it is our turn again.

        Args:
            action_payload: Dictionary representing the action, e.g.,
                {"action": "RAISE", "amount": 200}

        Returns:
            Parsed JSON dictionary of the server response.
        """
        url = f"{self.base_url}/game/action"
        response = self.session.post(url, data=json.dumps(action_payload), timeout=65)
        response.raise_for_status()
        return response.json()