"""
Advent of Code 2023 - Day 13: Point of Incidence
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import Callable, Sequence as Seq

Grid = Seq[Seq[str]]
IntGrid = list[int]


def main() -> int:
    blocks = sys.stdin.read().split("\n\n")
    grids = [block.split("\n") for block in blocks]
    int_grids = list(map(as_ints, grids))

    print("Part 1:", part1(int_grids))
    print("Part 2:", part2(int_grids))

    return 0


def as_ints(grid: Grid) -> tuple[IntGrid, IntGrid]:
    row_ints = [int("".join(row).replace(".", "0").replace("#", "1").lstrip("0"), 2) for row in grid]
    col_ints = [int("".join(col).replace(".", "0").replace("#", "1").lstrip("0"), 2) for col in zip(*grid)]

    return row_ints, col_ints


def part1(int_grids: list[tuple[IntGrid, IntGrid]]) -> int:
    return solve(int_grids, find_reflection)


def part2(int_grids: list[tuple[IntGrid, IntGrid]]) -> int:
    return solve(int_grids, find_reflection_with_smudge)


def solve(
    int_grids: list[tuple[IntGrid, IntGrid]],
    find_reflection_func: Callable[[IntGrid], int | None],
) -> int:
    total = 0
    for row_ints, col_ints in int_grids:
        if (reflection_row := find_reflection_func(row_ints)) is not None:
            total += 100 * (reflection_row + 1)
        elif (reflection_col := find_reflection_func(col_ints)) is not None:
            total += reflection_col + 1
        else:
            raise ValueError("No reflection found")
    return total


def find_reflection(ints: IntGrid) -> int | None:
    for i in range(len(ints) - 1):
        front, back = i, i + 1
        while front >= 0 and back < len(ints):
            if ints[front] != ints[back]:
                break
            front -= 1
            back += 1
        else:
            return i
    return None


def find_reflection_with_smudge(ints: IntGrid) -> int | None:
    for i in range(len(ints) - 1):
        front, back = i, i + 1
        error = 0
        while front >= 0 and back < len(ints):
            error += (ints[front] ^ ints[back]).bit_count()
            front -= 1
            back += 1
        if error == 1:
            return i
    return None


if __name__ == "__main__":
    sys.exit(main())
