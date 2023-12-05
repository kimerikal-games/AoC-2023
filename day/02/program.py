"""
Advent of Code 2023 - Day 2: Cube Conundrum
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import Counter
from functools import reduce
from math import prod

CUBES_TARGET = Counter({"red": 12, "green": 13, "blue": 14})


def main() -> int:
    games = preprocess(sys.stdin.readlines())

    print("Part 1:", part1(games))
    print("Part 2:", part2(games))

    return 0


def preprocess(games: list[str]) -> list[list[Counter[str]]]:
    counters = []
    for game in games:
        _, back = game.strip().split(": ")
        subset_strs = back.strip().split("; ")
        subset_counters = []
        for subset_str in subset_strs:
            cubes = Counter()
            cube_strs = subset_str.strip().split(", ")
            for cube_str in cube_strs:
                cube_count_str, cube_color = cube_str.strip().split(" ")
                cube_count = int(cube_count_str)
                cubes[cube_color] += cube_count
            subset_counters.append(cubes)
        counters.append(subset_counters)
    return counters


def part1(games: list[list[Counter[str]]]):
    return sum(
        game_id
        for game_id, game in enumerate(games, start=1)
        if all(cubes <= CUBES_TARGET for cubes in game)
    )


def part2(games: list[list[Counter[str]]]):
    return sum(prod(reduce(Counter.__ior__, game, Counter()).values()) for game in games)


if __name__ == "__main__":
    sys.exit(main())
