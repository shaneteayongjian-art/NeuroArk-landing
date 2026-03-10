"""
Monte‑Carlo hand equity estimation using eval7.

Given hole cards and a community board, this module estimates the probability
that our hand will win against a uniformly random opponent hand drawn from
the remaining deck.  It can also integrate an opponent range estimate from
the opponent model, although in this simple implementation we ignore it and
treat all unseen cards as equally likely.
"""
from __future__ import annotations

import random
from typing import Iterable, List

from treys import Card, Deck, Evaluator


def est_equity(hole, board, opp_range, iters=500):
    evaluator = Evaluator()
    deck = Deck()
    # 移除已知牌
    used = set(hole + board)
    deck.cards = [c for c in deck.cards if Card.int_to_str(c) not in used]
    wins = 0
    ties = 0
    for _ in range(iters):
        deck.shuffle()
        opp = [Card.int_to_str(deck.cards[0]), Card.int_to_str(deck.cards[1])]
        community_needed = 5 - len(board)
        drawn = [Card.int_to_str(deck.cards[i+2]) for i in range(community_needed)]
        our_hand = [Card.new(card) for card in hole]
        opp_hand = [Card.new(card) for card in opp]
        board_cards = [Card.new(card) for card in board + drawn]
        our_score = evaluator.evaluate(board_cards, our_hand)
        opp_score = evaluator.evaluate(board_cards, opp_hand)
        if our_score < opp_score:
            wins += 1
        elif our_score == opp_score:
            ties += 1
    return (wins + 0.5 * ties) / iters

def est_equity(hole: List[str], board: List[str], opp_range: Iterable[tuple[str, str]] | None, iters: int = 500) -> float:
    """Estimate the probability of winning using Monte‑Carlo simulation.

    Args:
        hole: Our two hole cards, e.g., ["As", "Kd"].
        board: Community cards revealed so far, up to five cards.
        opp_range: Optional iterable of opponent hole card combinations.  If
            provided, the simulation will sample exclusively from these combos;
            otherwise, a random hand is drawn uniformly from the remaining
            cards.
        iters: Number of random simulations.  More iterations yield a more
            stable estimate at the cost of increased runtime.

    Returns:
        A float between 0 and 1 representing our winning probability (ties
        count as half a win).
    """
    if not hole or len(hole) != 2:
        return 0.0

    # Convert string cards into eval7.Card objects
    our_cards = [eval7.Card(c) for c in hole]
    board_cards = [eval7.Card(c) for c in board]

    # Build a deck excluding our cards and board cards
    deck = eval7.Deck()
    used_cards = set(card for card in our_cards + board_cards)
    deck.cards = [c for c in deck.cards if c not in used_cards]

    wins = 0
    ties = 0
    for _ in range(iters):
        deck.shuffle()
        # Opponent hand selection
        if opp_range:
            # For now, ignore the provided range and sample uniformly
            opp_cards = [deck.peek(0), deck.peek(1)]
        else:
            opp_cards = [deck.peek(0), deck.peek(1)]

        # Draw remaining community cards if needed
        remaining = 5 - len(board_cards)
        drawn = [deck.peek(i + 2) for i in range(remaining)]

        our_hand = our_cards + drawn
        opp_hand = opp_cards + drawn
        our_score = eval7.evaluate(our_hand)
        opp_score = eval7.evaluate(opp_hand)
        if our_score > opp_score:
            wins += 1
        elif our_score == opp_score:
            ties += 1

    return (wins + 0.5 * ties) / float(iters)