"""
State abstraction for simplified decision making.

In large imperfect information games like Texas Hold'em, storing a unique
strategy for every possible state is infeasible.  Instead, similar states are
grouped into "buckets" based on hand strength, board texture, position and
action history.  This module provides a minimal abstraction that classifies
states into coarse categories used by the policy and training components.
"""
from __future__ import annotations

from typing import Dict, Tuple


def bucket_state(state: Dict[str, any]) -> Tuple[str, str, str]:
    """Categorise the current state into a coarse bucket.

    This function examines the stage of the hand, player's position and
    properties of the community cards to produce a tuple.  The policy uses
    these buckets to adjust its equity thresholds.  Feel free to refine this
    logic; more granular buckets can improve performance at the cost of a
    larger strategy space.

    Args:
        state: Normalised state dictionary returned from `adapter.adapt_state`.

    Returns:
        A tuple (round, position, texture) describing the state.
    """
    street = state.get("round", "preflop") or "preflop"
    position = state.get("position", "") or ""
    board = state.get("board", [])

    # Compute a rough texture classification for the board
    texture = classify_texture(board)

    return (street, position, texture)


def classify_texture(board: list) -> str:
    """Classify board texture by suit distribution and connectivity.

    A very coarse classifier that only uses the number of cards and whether
    there is a potential flush draw or straight draw present.  Returns one of
    "empty", "dry", "semi", "wet".
    """
    if not board or len(board) == 0:
        return "empty"

    suits = [card[1] if isinstance(card, str) else str(card)[1] for card in board]
    ranks = [card[0] if isinstance(card, str) else str(card)[0] for card in board]
    # Count of each suit
    suit_counts = {}
    for s in suits:
        suit_counts[s] = suit_counts.get(s, 0) + 1
    max_suit = max(suit_counts.values())

    # Simple straight draw check: if ranks are sequential or have gaps of 1
    values = []
    rank_map = {r: i for i, r in enumerate("23456789TJQKA", start=2)}
    for r in ranks:
        values.append(rank_map.get(r.upper(), 0))
    values.sort()
    straight_draw = False
    if len(values) >= 3:
        # look for sequences of consecutive or one gap
        gaps = [values[i+1] - values[i] for i in range(len(values) - 1)]
        # A run with small gaps indicates connectivity
        if gaps.count(1) >= 2 or (gaps.count(2) >= 1 and gaps.count(1) >= 1):
            straight_draw = True

    # Determine texture category
    if max_suit >= 3 or straight_draw:
        return "wet"
    elif max_suit == 2:
        return "semi"
    else:
        return "dry"