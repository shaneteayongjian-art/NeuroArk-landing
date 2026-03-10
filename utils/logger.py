"""
Simple logger utility.

Provides a `log` function that prints messages to stdout with a timestamp
prefix.  This can be replaced with a more sophisticated logging framework
without changing the rest of the codebase.
"""
from __future__ import annotations

import datetime
import sys


def log(message: str) -> None:
    """Print a timestamped message to standard output."""
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    sys.stdout.write(f"[{ts}] {message}\n")
    sys.stdout.flush()