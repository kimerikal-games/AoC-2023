"""
Advent of Code 2023 - Day 14: Parabolic Reflector Dish
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import Sequence as Seq

Grid = Seq[Seq[str]]


def main() -> int:
    grid = [line.strip() for line in sys.stdin]

    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))

    return 0


def part1(grid: Grid) -> int:
    return compute_load(tilt_up(grid))


def part2(grid: Grid) -> int:
    target = 1_000_000_000
    history = {as_str(grid): 0}
    for step in range(1, target + 1):
        grid = run_cycle(grid)
        grid_str = as_str(grid)
        if grid_str in history:
            cycle_len = step - history[grid_str]
            cycle_start = history[grid_str]
            cycle_offset = (target - cycle_start) % cycle_len
            for _ in range(cycle_offset):
                grid = run_cycle(grid)
            break
        history[grid_str] = step
    return compute_load(grid)


def tilt_up(grid: Grid) -> Grid:
    rows = len(grid)
    cols = len(grid[0])
    new_grid = []
    for j in range(cols):
        col = [grid[i][j] for i in range(len(grid))]
        put_i = 0
        for scan_i in range(rows):
            if col[scan_i] == "O":
                if put_i != scan_i:
                    col[put_i], col[scan_i] = "O", "."
                put_i += 1
            elif col[scan_i] == "#":
                put_i = scan_i + 1
        new_grid.append(col)
    new_grid = transpose(new_grid)
    return new_grid


def run_cycle(grid: Grid) -> Grid:
    for _ in range(4):
        grid = rotate_cw(tilt_up(grid))
    return grid


def compute_load(grid: Grid) -> int:
    return sum(i * row.count("O") for i, row in enumerate(reversed(grid), start=1))


def transpose(grid: Grid) -> Grid:
    return [list(row) for row in zip(*grid)]


def rotate_cw(grid: Grid) -> Grid:
    return [list(row[::-1]) for row in zip(*grid)]


def as_str(grid: Grid) -> str:
    return "\n".join("".join(row) for row in grid)


if __name__ == "__main__":
    sys.exit(main())
