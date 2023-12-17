"""
Advent of Code 2023 - Day 16: The Floor Will Be Lava
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from itertools import chain
from typing import Literal, Sequence as Seq


Cell = Literal[".", "/", "\\", "-", "|"]
Grid = Seq[Seq[Cell]]
Direction = Literal["U", "D", "L", "R"]
State = tuple[int, int, Direction]


NDS: dict[Cell, dict[Direction, list[Direction]]] = {
    ".": {"U": ["U"], "D": ["D"], "L": ["L"], "R": ["R"]},
    "/": {"U": ["R"], "D": ["L"], "L": ["D"], "R": ["U"]},
    "\\": {"U": ["L"], "D": ["R"], "L": ["U"], "R": ["D"]},
    "-": {"U": ["R", "L"], "D": ["R", "L"], "L": ["L"], "R": ["R"]},
    "|": {"U": ["U"], "D": ["D"], "L": ["U", "D"], "R": ["U", "D"]},
}
MOVES: dict[Direction, tuple[int, int]] = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def main() -> int:
    grid: Grid = [line.strip() for line in sys.stdin]  # type: ignore

    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))

    return 0


def part1(grid: Grid) -> int:
    return simulate_energy(grid, (0, -1, "R"))


def part2(grid: Grid) -> int:
    rows, cols = len(grid), len(grid[0])

    from_top = ((-1, x, "D") for x in range(cols))
    from_bottom = ((rows, x, "U") for x in range(cols))
    from_left = ((y, -1, "R") for y in range(rows))
    from_right = ((y, cols, "L") for y in range(rows))
    from_any = chain(from_top, from_bottom, from_left, from_right)

    max_energy = max(simulate_energy(grid, state) for state in from_any)
    return max_energy


def simulate_energy(grid: Grid, state: State) -> int:
    rows, cols = len(grid), len(grid[0])

    visit_queue = list[State]()
    visited = set[State]()
    energized = [[False] * cols for _ in range(rows)]

    visit_queue.append(state)
    visited.add(state)

    while visit_queue:
        y, x, d = visit_queue.pop()

        dy, dx = MOVES[d]
        ny, nx = y + dy, x + dx
        if not (0 <= ny < rows and 0 <= nx < cols):
            continue

        cell = grid[ny][nx]
        energized[ny][nx] = True

        nds = NDS[cell][d]
        for nd in nds:
            if (ny, nx, nd) not in visited:
                visit_queue.append((ny, nx, nd))
                visited.add((ny, nx, nd))

    energy = sum(sum(row) for row in energized)
    return energy


if __name__ == "__main__":
    sys.exit(main())
