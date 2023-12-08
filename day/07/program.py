"""
Advent of Code 2023 - Day 7: Camel Cards
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import Counter
from itertools import product
from typing import Any, Callable, NamedTuple, TypeAlias


Hand: TypeAlias = str
Game = NamedTuple("Game", hand=Hand, bid=int)
ValueTuple = tuple[Any, ...]


def main() -> int:
    games: list[Game] = []
    for line in sys.stdin:
        parts = line.split()
        hand = parts[0]
        bid = int(parts[1])
        games.append(Game(hand, bid))

    print("Part 1:", part1(games))
    print("Part 2:", part2(games))

    return 0


def part1(games: list[Game]) -> int:
    return compute_winnings(games, compute_hand_value_part1)


def part2(games: list[Game]) -> int:
    return compute_winnings(games, compute_hand_value_part2)


def compute_winnings(games: list[Game], compute_hand_value_fn: Callable[[Hand], ValueTuple]) -> int:
    ordered_games = sorted(games, key=lambda game: compute_hand_value_fn(game.hand))
    winnings = sum(rank * game.bid for rank, game in enumerate(ordered_games, start=1))
    return winnings


def compute_hand_value_part1(hand: Hand) -> ValueTuple:
    card_order = "23456789TJQKA"
    hand_type_value = compute_hand_type_value(hand)
    hand_card_value = compute_hand_card_value(hand, card_order)
    return (hand_type_value, hand_card_value)


def compute_hand_value_part2(hand: Hand) -> ValueTuple:
    card_order = "J23456789TQKA"
    hand_type_value = max(map(compute_hand_type_value, replace_jokers(hand)))
    hand_card_value = compute_hand_card_value(hand, card_order)
    return (hand_type_value, hand_card_value)


def compute_hand_type_value(hand: Hand) -> ValueTuple:
    return tuple(sorted(Counter(hand).values(), reverse=True))


def compute_hand_card_value(hand: Hand, card_order: str) -> ValueTuple:
    return tuple(map(card_order.index, hand))


def replace_jokers(hand: Hand):
    joker_idxs = [i for i, card in enumerate(hand) if card == "J"]
    hand_list = list(hand)
    for replaced in product(set(hand), repeat=len(joker_idxs)):
        for idx, card in zip(joker_idxs, replaced):
            hand_list[idx] = card
        yield "".join(hand_list)


if __name__ == "__main__":
    sys.exit(main())
