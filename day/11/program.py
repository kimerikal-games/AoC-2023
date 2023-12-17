"""
Advent of Code 2023 - Day 11: Cosmic Expansion
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from itertools import accumulate


def main() -> int:
    ys: list[int] = []
    xs: list[int] = []
    for y, line in enumerate(sys.stdin):
        for x, char in enumerate(line.strip()):
            if char == "#":
                ys.append(y)
                xs.append(x)
    n = len(ys)

    print("Part 1:", part1(n, ys, xs))
    print("Part 2:", part2(n, ys, xs))

    return 0


def part1(n: int, ys: list[int], xs: list[int]) -> int:
    return solve(n, ys, xs, 2)


def part2(n: int, ys: list[int], xs: list[int]) -> int:
    return solve(n, ys, xs, 1_000_000)


def solve(n: int, ys: list[int], xs: list[int], factor: int) -> int:
    ys = expand(ys, factor)
    xs = expand(xs, factor)

    total = 0
    for i in range(n):
        yi, xi = ys[i], xs[i]
        for j in range(i + 1, n):
            yj, xj = ys[j], xs[j]
            d = abs(yj - yi) + abs(xj - xi)
            total += d

    return total


def expand(arr: list[int], factor: int) -> list[int]:
    set_ = set(arr)
    grid = [1 if x in set_ else factor for x in range(max(set_) + 1)]
    grid = list(accumulate(grid))
    arr = [grid[x] for x in arr]
    return arr


if __name__ == "__main__":
    sys.exit(main())
