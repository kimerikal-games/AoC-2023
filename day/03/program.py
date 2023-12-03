"""
Advent of Code 2023 - Day 3: Gear Ratios
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys


def main() -> int:
    lines = sys.stdin.readlines()
    grid = [list(line.strip()) for line in lines]

    rows, cols, grid = pad_grid(grid)

    print("Part 1:", part1(rows, cols, grid))
    print("Part 2:", part2(rows, cols, grid))

    return 0


def pad_grid(grid: list[list[str]]) -> list[list[str]]:
    rows = len(grid)
    cols = len(grid[0])
    grid = [["."] * cols] + grid + [["."] * cols]
    grid = [["."] + row + ["."] for row in grid]
    rows += 2
    cols += 2
    return rows, cols, grid


def part1(rows: int, cols: int, grid: list[list[str]]) -> int:
    non_symbols = "0123456789."

    total = 0
    for y in range(1, rows - 1):
        x = 1
        while x < cols - 1:
            if grid[y][x].isdigit():
                x_start = x
                while grid[y][x].isdigit():
                    x += 1
                x_end = x
                value = int("".join(grid[y][x_start:x_end]))
                if not (
                    grid[y][x_start - 1] in non_symbols
                    and grid[y][x_end] in non_symbols
                    and all(c in non_symbols for c in grid[y - 1][x_start - 1 : x_end + 1])
                    and all(c in non_symbols for c in grid[y + 1][x_start - 1 : x_end + 1])
                ):
                    total += value
            x += 1

    return total


def part2(rows: int, cols: int, grid: list[list[str]]) -> int:
    non_symbols = "0123456789."

    grid_ids = [[None] * cols for _ in range(rows)]
    id_values = [0]
    for y in range(1, rows - 1):
        x = 1
        while x < cols - 1:
            if grid[y][x].isdigit():
                x_start = x
                while grid[y][x].isdigit():
                    x += 1
                x_end = x
                value = int("".join(grid[y][x_start:x_end]))
                grid_id = len(id_values)
                id_values.append(value)
                for xp in range(x_start, x_end):
                    grid_ids[y][xp] = grid_id
            x += 1

    total = 0
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] not in non_symbols:
                nearby_ids = set()
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        grid_id = grid_ids[y + dy][x + dx]
                        if grid_id is not None:
                            nearby_ids.add(grid_id)
                if len(nearby_ids) == 2:
                    id1, id2 = nearby_ids
                    gear_value = id_values[id1] * id_values[id2]
                    total += gear_value

    return total


if __name__ == "__main__":
    sys.exit(main())
