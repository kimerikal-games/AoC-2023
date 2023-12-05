"""
Advent of Code 2023 - Day 3: Gear Ratios
Author: kimerikal <kimerikal.games@gmail.com>
"""
import re
import sys

Grid = list[str]


def main() -> int:
    grid = [line.strip() for line in sys.stdin.readlines()]
    grid = pad_grid(grid)
    rows = len(grid)
    cols = len(grid[0])

    print("Part 1:", part1(rows, cols, grid))
    print("Part 2:", part2(rows, cols, grid))

    return 0


def pad_grid(grid: Grid) -> Grid:
    cols = len(grid[0])
    grid = ["." * cols] + grid + ["." * cols]
    grid = ["." + row + "." for row in grid]
    return grid


def part1(rows: int, cols: int, grid: Grid) -> int:
    stripes = extract_stripes(rows, cols, grid)

    total = 0
    for y, x_start, x_end, value in stripes:
        is_around_symbol = any(
            is_symbol(grid[yp][xp])
            for yp, xp in around_stripe(y, x_start, x_end)
        )
        if is_around_symbol:
            total += value
    return total


def part2(rows: int, cols: int, grid: Grid) -> int:
    grid_ids, id_values = assign_grid_ids(rows, cols, grid)

    total = 0
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            if not is_symbol(grid[y][x]):
                continue
            nearby_ids = {
                cell
                for yp, xp in around_cell(y, x)
                if (cell := grid_ids[yp][xp]) is not None
            }
            if len(nearby_ids) == 2:
                id1, id2 = nearby_ids
                gear_value = id_values[id1] * id_values[id2]
                total += gear_value

    return total


def extract_stripes(rows: int, cols: int, grid: Grid) -> list[tuple[int, int, int, int]]:
    stripes = []
    for y in range(1, rows - 1):
        for match in re.finditer(r"\d+", grid[y]):
            value = int(match.group())
            x_start = match.start()
            x_end = match.end()
            stripes.append((y, x_start, x_end, value))
    return stripes


def around_stripe(y: int, x_start: int, x_end: int):
    yield y, x_start - 1
    yield y, x_end
    for yp in (y - 1, y + 1):
        for xp in range(x_start - 1, x_end + 1):
            yield yp, xp


def around_cell(y: int, x: int):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            yield y + dy, x + dx


def assign_grid_ids(rows: int, cols: int, grid: Grid) -> tuple[list[list[int]], list[int]]:
    grid_ids: list[list[int | None]] = [[None] * cols for _ in range(rows)]
    id_values: list[int] = []
    stripes = extract_stripes(rows, cols, grid)
    for y, x_start, x_end, value in stripes:
        grid_id = len(id_values)
        id_values.append(value)
        for xp in range(x_start, x_end):
            grid_ids[y][xp] = grid_id
    return grid_ids, id_values  # type: ignore


def is_symbol(x: str) -> bool:
    return not (x.isdigit() or x == ".")


if __name__ == "__main__":
    sys.exit(main())
