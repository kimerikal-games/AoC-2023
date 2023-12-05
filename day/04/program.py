"""
Advent of Code 2023 - Day 4: Scratchcards
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys


def main() -> int:
    values = []
    for line in sys.stdin:
        left, right = line.split(":")[1].split("|")
        value = len(set(map(int, left.split())) & set(map(int, right.split())))
        values.append(value)

    print("Part 1:", part1(values))
    print("Part 2:", part2(values))

    return 0


def part1(values: list[int]) -> int:
    return sum(1 << v >> 1 for v in values)


def part2(values: list[int]) -> int:
    count_table: list[int | None] = [None] * len(values)
    return sum(subproblem(values, index, count_table) for index in range(len(values)))


def subproblem(values: list[int], index: int, count_table: list[int | None]) -> int:
    if count_table[index] is None:
        count_table[index] = 1 + sum(
            subproblem(values, other_index, count_table)
            for other_index in range(index + 1, index + values[index] + 1)
            if other_index < len(values)
        )
    return count_table[index]  # type: ignore


if __name__ == "__main__":
    sys.exit(main())
