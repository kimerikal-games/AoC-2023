"""
Advent of Code 2023 - Day 7: Camel Cards
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import Counter
from enum import IntEnum
from itertools import product
from typing import Callable, NamedTuple


class HandType(IntEnum):
    FIVE_OF_A_KIND  = -10
    FOUR_OF_A_KIND  = -20
    FULL_HOUSE      = -30
    THREE_OF_A_KIND = -40
    TWO_PAIR        = -50
    ONE_PAIR        = -60
    HIGH_CARD       = -70

    @classmethod
    def from_hand(cls, hand: 'Hand') -> "HandType":
        match sorted(Counter(hand).values(), reverse=True):
            case [5]:             return cls.FIVE_OF_A_KIND
            case [4, 1]:          return cls.FOUR_OF_A_KIND
            case [3, 2]:          return cls.FULL_HOUSE
            case [3, 1, 1]:       return cls.THREE_OF_A_KIND
            case [2, 2, 1]:       return cls.TWO_PAIR
            case [2, 1, 1, 1]:    return cls.ONE_PAIR
            case [1, 1, 1, 1, 1]: return cls.HIGH_CARD
            case _:               assert False, "Unreachable"


Hand = str
HandValue = tuple[HandType, tuple[int, ...]]
Game = NamedTuple("Game", [("hand", Hand), ("bid", int)])


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
    return compute_winnings(games, hand_value_part1)


def part2(games: list[Game]) -> int:
    return compute_winnings(games, hand_value_part2)


def compute_winnings(games: list[Game], hand_value_fn: Callable[[Hand], HandValue]) -> int:
    ordered_games = sorted(games, key=lambda game: hand_value_fn(game.hand))
    winnings = sum(rank * game.bid for rank, game in enumerate(ordered_games, start=1))
    return winnings


def hand_value_part1(hand: Hand) -> HandValue:
    cards = "23456789TJQKA"
    hand_type = HandType.from_hand(hand)
    hand_tuple = tuple(map(cards.index, hand))
    return (hand_type, hand_tuple)


def hand_value_part2(hand: Hand) -> HandValue:
    cards = "J23456789TQKA"
    hand_type = max(map(HandType.from_hand, replace_joker(hand)))
    hand_tuple = tuple(map(cards.index, hand))
    return (hand_type, hand_tuple)


def replace_joker(hand: str):
    cards = "23456789TJQKA"
    joker_idxs = [i for i, card in enumerate(hand) if card == "J"]
    hand_list = list(hand)
    for replaced in product(cards, repeat=len(joker_idxs)):
        for idx, card in zip(joker_idxs, replaced):
            hand_list[idx] = card
        yield "".join(hand_list)


if __name__ == "__main__":
    sys.exit(main())
