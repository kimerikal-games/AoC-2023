"""
Advent of Code 2023 - Day 6: Wait For It
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from math import ceil, floor, prod, sqrt


def main() -> int:
    durations = list(map(int, input().removeprefix("Time:").split()))
    distances = list(map(int, input().removeprefix("Distance:").split()))

    print("Part 1:", part1(durations, distances))
    print("Part 2:", part2(durations, distances))

    return 0


def part1(durations: list[int], distances: list[int]) -> int:
    return prod(map(count_ways, durations, distances))


def part2(durations: list[int], distances: list[int]) -> int:
    actual_duration = int("".join(map(str, durations)))
    actual_distance = int("".join(map(str, distances)))
    return count_ways(actual_duration, actual_distance)


def count_ways(duration: int, distance: int) -> int:
    sqrt_d = sqrt(duration * duration - 4 * distance)
    upper_bound = ceil((duration + sqrt_d) / 2) - 1
    lower_bound = floor((duration - sqrt_d) / 2)
    ways = upper_bound - lower_bound
    return ways


if __name__ == "__main__":
    sys.exit(main())
