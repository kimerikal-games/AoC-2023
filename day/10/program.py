"""
Advent of Code 2023 - Day 10: Pipe Maze
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import deque

Grid = list[list[str]]
Coord = tuple[int, int]

UP = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DOWN = (1, 0)
MOVES = [UP, LEFT, RIGHT, DOWN]
TILES_MOVES = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "7": [LEFT, DOWN],
    "F": [RIGHT, DOWN],
    ".": [],
}


def main() -> int:
    grid = [list(line.strip()) for line in sys.stdin]
    start = find_start(grid)
    fix_start(grid, start)
    visited = bfs(grid, start)

    print("Part 1:", part1(grid, start, visited))
    print("Part 2:", part2(grid, start, visited))

    return 0


def find_start(grid: Grid) -> Coord:
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                return y, x

    raise ValueError("No start found")


def fix_start(grid: Grid, start: Coord) -> None:
    rows, cols = len(grid), len(grid[0])
    y, x = start
    moves = []
    for dy, dx in MOVES:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < rows and 0 <= nx < cols):
            continue
        if tile_accepts(grid[ny][nx], (dy, dx)):
            moves.append((dy, dx))

    for tile, tile_moves in TILES_MOVES.items():
        if tile_moves == moves:
            grid[y][x] = tile
            return y, x

    raise ValueError("Start cannot be fixed")


def part1(grid: Grid, start: Coord, visited: dict[Coord, int]) -> int:
    return max(visited.values())


def part2(grid: Grid, start: Coord, visited: dict[Coord, int]) -> int:
    result = 0
    for y, row in enumerate(grid):
        incidence = 0
        direction = None
        for x, char in enumerate(row):
            if (y, x) in visited:
                tile_moves = TILES_MOVES[char]
                if RIGHT in tile_moves:
                    if UP in tile_moves:
                        direction = "UP"
                    elif DOWN in tile_moves:
                        direction = "DOWN"
                elif LEFT in tile_moves:
                    if UP in tile_moves and direction == "DOWN":
                        incidence += 1
                    elif DOWN in tile_moves and direction == "UP":
                        incidence += 1
                else:
                    incidence += 1
            else:
                if incidence % 2 == 1:
                    result += 1

    return result


def bfs(grid: Grid, start: Coord):
    rows, cols = len(grid), len(grid[0])
    visited = {start: 0}
    visit_queue = deque([start])

    while visit_queue:
        y, x = visit_queue.popleft()

        for dy, dx in TILES_MOVES[grid[y][x]]:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < rows and 0 <= nx < cols):
                continue
            if (ny, nx) in visited:
                continue
            if not tile_accepts(grid[ny][nx], (dy, dx)):
                continue

            visited[ny, nx] = visited[y, x] + 1
            visit_queue.append((ny, nx))

    return visited


def tile_accepts(tile: str, move: tuple[int, int]) -> bool:
    dy, dx = move
    return (-dy, -dx) in TILES_MOVES[tile]


if __name__ == "__main__":
    sys.exit(main())
