"""
Adapters for translating between server JSON and internal representations.

The tournament API may change field names across versions.  By centralising
all such transformations here the rest of the bot can remain stable.  If the
`adapt_state` or `to_action_payload` functions break due to changed keys,
consult the API documentation and adjust the mappings accordingly.
"""
from __future__ import annotations

from typing import Any, Dict, List


def adapt_state(server_json: Dict[str, Any]) -> Dict[str, Any]:
    """Convert the raw server response into a normalised internal state.

    Args:
        server_json: A dictionary decoded from the server's JSON response.

    Returns:
        A dictionary with consistent keys used by the strategy layer.  Missing
        fields are given default values to simplify downstream logic.
    """
    sj = server_json or {}
    # Map server fields to our canonical representation.  Adjust these keys
    # according to the API's documentation.  If a field is missing, supply a
    # sensible default.
    state = {
        "your_turn": bool(sj.get("your_turn", False)),
        "hole_cards": sj.get("hole_cards", []),
        # The API sometimes calls community cards "community_cards" or "board"
        "board": sj.get("board") or sj.get("community_cards") or [],
        "legal_actions": sj.get("legal_actions", []),
        "to_call": sj.get("to_call", 0),
        "pot": sj.get("pot", 0),
        "stack": sj.get("stack", 0),
        "min_raise": sj.get("min_raise", None),
        "max_raise": sj.get("max_raise", None),
        # Position of this player at the table (e.g., SB, BB, BTN)
        "position": sj.get("position"),
        # Other players' chip counts or summary information
        "players": sj.get("players", []),
        # Stage of the hand: preflop, flop, turn, river
        "round": sj.get("round"),
        # Table parameters (big blind, ante)
        "big_blind": sj.get("big_blind", 100),
        "ante": sj.get("ante", 0),
    }
    return state


def to_action_payload(action: Dict[str, Any]) -> Dict[str, Any]:
    """Translate an internal action dictionary into the server API format.

    The API expects an uppercase action type and uses "amount" for bet/raise
    sizing.  If the action contains no amount (e.g., fold, check, call) the
    amount is omitted.

    Args:
        action: Internal representation like {"type": "raise", "amount": 200}.

    Returns:
        Dictionary ready to send to the `/game/action` endpoint.
    """
    action_type = action.get("type", "fold").upper()
    amount = action.get("amount")
    if amount is None:
        return {"action": action_type}
    return {"action": action_type, "amount": int(amount)}