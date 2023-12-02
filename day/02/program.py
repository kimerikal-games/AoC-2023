"""
Advent of Code 2023 - Day 2: Cube Conundrum
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import Counter
from math import prod


def main() -> int:
    games = sys.stdin.readlines()
    games = preprocess(games)

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
    cubes_target = Counter({"red": 12, "green": 13, "blue": 14})

    result = 0

    for game_id, game in enumerate(games, start=1):
        if all(cubes <= cubes_target for cubes in game):
            result += game_id

    return result


def part2(games):
    result = 0

    for game in games:
        cubes = Counter()
        for subset in game:
            cubes |= subset

        value = prod(cubes.values())
        result += value

    return result


if __name__ == "__main__":
    sys.exit(main())
