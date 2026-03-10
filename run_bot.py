"""
Main entry point for the poker bot.

This script reads configuration from environment variables, joins the game via
the tournament API and loops: waiting until it is our turn, computing an
action using the strategy module and sending that action back to the server.

The API is blocking, so the client waits for the server to respond when it is
our turn.  If the connection drops the script will attempt to re‑join using
the same token.  Invalid or missing fields in the server response are
normalised via the adapter before being passed to the strategy layer.
"""
from __future__ import annotations

import os
import signal
import sys
import time
from typing import Any, Dict

from dotenv import load_dotenv

from api_client import APIClient
from adapter import adapt_state, to_action_payload
from strategy.policy import Policy
from utils.logger import log


def main() -> None:
    """Launch the bot and handle reconnections.

    This function loads environment variables, constructs the API client and
    strategy, then enters an infinite loop to process turns.  It catches
    keyboard interrupts to exit gracefully.
    """
    # Load configuration from .env
    load_dotenv()
    base_url = os.getenv("POKER_BASE_URL")
    username = os.getenv("POKER_USERNAME")
    password = os.getenv("POKER_PASSWORD")
    token = os.getenv("POKER_JOIN_TOKEN")
    bot_name = os.getenv("BOT_NAME", "UnnamedBot")

    if not all([base_url, username, password, token]):
        log(
            "Missing configuration; ensure POKER_BASE_URL, POKER_USERNAME, "
            "POKER_PASSWORD and POKER_JOIN_TOKEN are set in your .env file."
        )
        sys.exit(1)

    # Instantiate API client and strategy
    api = APIClient(base_url=base_url, username=username, password=password)
    policy = Policy(bot_name=bot_name)

    def handle_exit(signum, frame):
        log("Received termination signal; exiting...")
        sys.exit(0)

    # Register signal handlers for graceful shutdown
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            signal.signal(sig, handle_exit)
        except Exception:
            # signals may not be available on all platforms
            pass

    log(f"Bot '{bot_name}' starting up...")

    # Reconnection loop
    while True:
        try:
            # Blocking call: wait until our turn or game state update
            server_state: Dict[str, Any] = api.join(token)
            internal_state = adapt_state(server_state)

            if not internal_state.get("your_turn"):
                # Not our turn yet; continue waiting
                continue

            # Compute an action using our policy
            action = policy.act(internal_state)
            payload = to_action_payload(action)

            # Send the action and wait for next state
            api.act(payload)

        except Exception as exc:
            # Log the error and attempt to reconnect after a short delay
            log(f"Encountered error: {exc}; retrying in 1 second...")
            time.sleep(1)
            continue


if __name__ == "__main__":
    main()