"""
Baseline decision policy for the poker bot.

This module implements a simple but reasonably robust decision maker that
combines estimated equity, pot odds and a few discretised bet sizes.  It also
tracks opponent tendencies and adjusts decision thresholds accordingly.  The
policy is stateless across hands but can be extended to incorporate learned
strategies from self‑play via the training modules.
"""
from __future__ import annotations

import random
from typing import Dict, List, Optional

from .equity import est_equity
from .abstraction import bucket_state
from .opponent import OpponentModel


class Policy:
    """Encapsulate decision logic for the bot."""

    def __init__(self, bot_name: str = "Bot") -> None:
        # Store a friendly name for logging or debugging
        self.bot_name = bot_name
        # Track opponents' tendencies to adjust our thresholds
        self.opp = OpponentModel()
        # Configurable bet sizes as multipliers of the current pot size
        self.bet_sizes = [0.5, 1.0]

    def act(self, state: Dict[str, any]) -> Dict[str, any]:
        """Choose an action based on the current game state.

        The policy attempts to balance value betting, bluffing and folding
        according to estimated equity and pot odds.  It returns a dictionary
        with keys "type" (fold/call/check/bet/raise) and optionally
        "amount" for bet/raise actions.
        """
        # Extract relevant fields
        hole = state.get("hole_cards", [])
        board = state.get("board", [])
        legal = set(a.lower() for a in state.get("legal_actions", []))
        pot = state.get("pot", 0)
        to_call = state.get("to_call", 0)
        stack = state.get("stack", 0)
        min_raise = state.get("min_raise")
        max_raise = state.get("max_raise")

        # Estimate our hand equity vs an opponent's range.  When opponent
        # modelling is available, pass the estimated range; otherwise use a
        # default empty list to indicate a random range.
        eq = est_equity(hole, board, self.opp.range_estimate())

        # Adjust equity based on opponent tendencies and the current abstracted state
        bucket = bucket_state(state)
        eq_adj = self.opp.adjust_equity(eq, bucket)

        # Compute pot odds: the fraction of the pot we must invest to call
        cost = float(to_call)
        pot_total = float(pot) + cost
        call_odds = cost / pot_total if pot_total > 0 else 0.0
        # Add a small buffer to require better equity than strictly necessary
        min_eq_to_call = call_odds + 0.05

        # Preflop: simple heuristics can override later logic if desired
        # (for example, raising with premium hands when first to act).  Here we
        # stick to the generic logic but you could insert preflop ranges.

        # If nothing to call (i.e., we can check), decide between checking and betting
        if to_call == 0 and "check" in legal:
            if eq_adj < 0.5:
                # Weak or mediocre hand: prefer to check behind
                return {"type": "check"}
            # With stronger hands, put out a bet to build the pot or deny equity
            if ("bet" in legal) or ("raise" in legal):
                # Determine an amount within min_raise/max_raise
                size = int(pot * self.bet_sizes[0])
                if min_raise is not None:
                    size = max(size, int(min_raise))
                if max_raise is not None:
                    size = min(size, int(max_raise))
                size = max(size, 1)
                size = min(size, stack)
                if size > 0:
                    # With very strong hands we occasionally bet pot
                    if eq_adj > 0.8 and random.random() < 0.25:
                        pot_size = int(pot * self.bet_sizes[1])
                        pot_size = max(pot_size, min_raise or pot_size)
                        pot_size = min(pot_size, max_raise or pot_size, stack)
                        return {"type": "bet", "amount": pot_size}
                    return {"type": "bet", "amount": size}
            # Fallback: check
            return {"type": "check"}

        # If faced with a bet/raise
        if to_call > 0:
            # Consider folding if our adjusted equity is below the threshold
            if eq_adj < min_eq_to_call and "fold" in legal:
                return {"type": "fold"}
            # Default action: call
            if "call" in legal:
                # Occasionally raise with strong hands to maintain aggression
                if eq_adj > 0.6 and ("raise" in legal or "bet" in legal):
                    # Choose between half‑pot and pot sized raises
                    chosen_mult = random.choice(self.bet_sizes)
                    amount = int(pot * chosen_mult)
                    if min_raise is not None:
                        amount = max(amount, int(min_raise))
                    if max_raise is not None:
                        amount = min(amount, int(max_raise))
                    amount = max(amount, to_call)  # must at least call
                    amount = min(amount, stack)
                    # Occasionally shove when extremely strong
                    if eq_adj > 0.8 and random.random() < 0.2:
                        amount = stack
                    return {"type": "raise", "amount": amount}
                return {"type": "call"}

        # Last resort: fold if possible, otherwise check/call
        if "fold" in legal and to_call > 0:
            return {"type": "fold"}
        if "check" in legal:
            return {"type": "check"}
        if "call" in legal:
            return {"type": "call"}
        # Should never reach here; default to fold
        return {"type": "fold"}