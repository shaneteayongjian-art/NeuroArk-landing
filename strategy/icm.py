"""
Independent Chip Model (ICM) risk adjustments.

In elimination rounds where tournament life is at stake, players should adopt
a more risk‑averse strategy than in cash games.  The ICM assigns each chip a
diminishing marginal value relative to overall tournament payout.  This module
provides a simple function to scale equity thresholds according to stack
relative to the average stack.
"""
from __future__ import annotations

from typing import List


def risk_weight(stack: int, stacks: List[int]) -> float:
    """Return a risk multiplier based on stack size relative to the field.

    A smaller stack should be more risk‑averse (weight > 1) while a larger
    stack can take more risk (weight < 1).  The average stack has weight 1.

    Args:
        stack: Our current chip count.
        stacks: List of all players' chip counts.

    Returns:
        A multiplier applied to required call equity.  Values >1 mean raise the
        threshold to be more conservative; values <1 mean loosen up.
    """
    if not stacks:
        return 1.0
    avg = sum(stacks) / len(stacks)
    if avg == 0:
        return 1.0
    ratio = stack / avg
    # Use an exponential form to emphasise differences.  For instance, a short
    # stack at half the average chips returns ~1.4; a big stack at twice the
    # average returns ~0.7.  Clip extremes to avoid runaway adjustments.
    weight = (1 / ratio) ** 0.5
    return max(0.6, min(1.4, weight))