"""
Online opponent modelling.

This module keeps a window of recent opponent actions and uses simple
heuristics to infer whether opponents are more aggressive or passive.  It
provides two key functions: `range_estimate()` for constructing an opponent
hand range (unused in this baseline) and `adjust_equity(eq, bucket)` for
scaling our estimated equity up or down according to observed tendencies.
"""
from __future__ import annotations

from collections import deque, defaultdict
from typing import Deque, Dict, Iterable, Tuple


class OpponentModel:
    """Track recent opponent actions and adjust equity estimates."""

    def __init__(self, window: int = 200) -> None:
        self.window: int = window
        # Store tuples of (action, street) for the last `window` events
        self.actions: Deque[Tuple[str, str]] = deque(maxlen=window)
        # Aggregate counts by action and street
        self.freq: Dict[Tuple[str, str], int] = defaultdict(int)

    def observe(self, action: str, street: str) -> None:
        """Record an opponent action for statistical analysis."""
        key = (action.lower(), street.lower())
        self.actions.append(key)
        self.freq[key] += 1

    def range_estimate(self) -> Iterable[Tuple[str, str]]:
        """Return an iterable of opponent hole card combinations.

        In a more advanced model this could return a distribution over
        preflop hand classes based on observed frequencies.  For now it returns
        an empty list to signal that the equity estimator should assume a
        uniform random range.
        """
        return []

    def adjust_equity(self, eq: float, bucket: Tuple[str, str, str]) -> float:
        """Adjust a raw equity estimate based on opponent tendencies.

        Args:
            eq: Raw Monte‑Carlo estimate of our hand's win probability.
            bucket: A tuple (round, position, texture) for context.

        Returns:
            A slightly adjusted equity, bounded between 0 and 1.  Aggressive
            opponents lower our perceived equity to encourage more folds,
            whereas passive opponents raise it.
        """
        # Compute aggression metric: counts of raises vs calls/checks
        raises = self.freq.get(("raise", bucket[0].lower()), 0) + self.freq.get(("bet", bucket[0].lower()), 0)
        calls = self.freq.get(("call", bucket[0].lower()), 0) + self.freq.get(("check", bucket[0].lower()), 0)
        total = raises + calls
        if total > 0:
            aggr_ratio = raises / total
        else:
            aggr_ratio = 0.5  # neutral if no data

        # Heuristic: adjust by up to ±3 percentage points
        if aggr_ratio > 0.6:
            # Opponent is aggressive; reduce our equity slightly
            adj = eq - 0.03
        elif aggr_ratio < 0.4:
            # Opponent is passive; increase our equity slightly
            adj = eq + 0.03
        else:
            adj = eq
        # Clamp to [0,1]
        return max(0.0, min(1.0, adj))