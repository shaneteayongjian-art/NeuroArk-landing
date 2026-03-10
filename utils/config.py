"""
Centralised configuration for the poker bot.

These values can be overridden by environment variables or by passing
parameters at runtime.  Having them here makes it easy to locate default
settings used throughout the project.
"""
from __future__ import annotations

import os


# Maximum time in seconds to wait for the API before considering the connection
# dead.  Should be greater than the tournament's `player_action_timeout` (8s)
# plus any grace period.  The API client uses 65 seconds by default.
API_TIMEOUT = int(os.getenv("POKER_API_TIMEOUT", "65"))