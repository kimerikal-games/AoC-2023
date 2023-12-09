"""
Advent of Code 2023 - Day 9: Mirage Maintenance
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from itertools import pairwise


def main() -> int:
    sequences = [list(map(int, line.split())) for line in sys.stdin]

    print("Part 1:", part1(sequences))
    print("Part 2:", part2(sequences))

    return 0


def part1(sequences: list[int]) -> int:
    return sum(map(extrapolate, sequences))


def part2(sequences: list[int]) -> int:
    sequences = [sequence[::-1] for sequence in sequences]
    return sum(map(extrapolate, sequences))


def extrapolate(sequence):
    levels = [sequence[:]]
    while not all(x == 0 for x in levels[-1]):
        next_level = [b - a for a, b in pairwise(levels[-1])]
        levels.append(next_level)
    levels[-1].append(0)
    for level1, level2 in pairwise(reversed(levels)):
        level2.append(level2[-1] + level1[-1])
    return levels[0][-1]


if __name__ == "__main__":
    sys.exit(main())
