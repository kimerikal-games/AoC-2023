"""
Advent of Code 2023 - Day 17: Clumsy Crucible
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from heapq import heappush, heappop

Grid = list[list[int]]


def main() -> int:
    grid = [list(map(int, line.strip())) for line in sys.stdin]

    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))

    return 0


def part1(grid: Grid) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = [(0, 0, 0, ((0, 0), (0, 0), (0, 0)))]
    visited = set()
    while queue:
        s, x, y, (d3, d2, d1) = heappop(queue)
        if (x, y) == (rows - 1, cols - 1):
            return s
        if (x, y, (d3, d2, d1)) in visited:
            continue
        visited.add((x, y, (d3, d2, d1)))
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if d3 == d2 == d1 == (dx, dy):
                continue
            if d1 == (-dx, -dy):
                continue
            if (x + dx, y + dy, (d2, d1, (dx, dy))) in visited:
                continue
            if not (0 <= x + dx < rows and 0 <= y + dy < cols):
                continue
            heappush(queue, (s + grid[x + dx][y + dy], x + dx, y + dy, (d2, d1, (dx, dy))))
    raise ValueError


def part2(grid: Grid) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = [(0, 0, 0, ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)))]
    visited = set()
    while queue:
        s, x, y, (d10, d9, d8, d7, d6, d5, d4, d3, d2, d1) = heappop(queue)
        if (x, y) == (rows - 1, cols - 1):
            return s
        if (x, y, (d10, d9, d8, d7, d6, d5, d4, d3, d2, d1)) in visited:
            continue
        visited.add((x, y, (d10, d9, d8, d7, d6, d5, d4, d3, d2, d1)))

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if d1 == (-dx, -dy):
                continue
            x1, y1 = x + dx, y + dy
            x2, y2 = x1 + dx, y1 + dy
            x3, y3 = x2 + dx, y2 + dy

            x4, y4 = x3 + dx, y3 + dy
            if not (0 <= x4 < rows and 0 <= y4 < cols):
                continue
            if d7 == d6 == d5 == d4 == d3 == d2 == d1 == (dx, dy):
                continue
            if (x4, y4, (d6, d5, d4, d3, d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy))) in visited:
                continue
            heappush(
                queue,
                (
                    s + grid[x1][y1] + grid[x2][y2] + grid[x3][y3] + grid[x4][y4],
                    x4,
                    y4,
                    (d6, d5, d4, d3, d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy)),
                ),
            )

            x5, y5 = x4 + dx, y4 + dy
            if not (0 <= x5 < rows and 0 <= y5 < cols):
                continue
            if d6 == d5 == d4 == d3 == d2 == d1 == (dx, dy):
                continue
            if (x5, y5, (d5, d4, d3, d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy))) in visited:
                continue
            heappush(
                queue,
                (
                    s + grid[x1][y1] + grid[x2][y2] + grid[x3][y3] + grid[x4][y4] + grid[x5][y5],
                    x5,
                    y5,
                    (d5, d4, d3, d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy)),
                ),
            )

            x6, y6 = x5 + dx, y5 + dy
            if not (0 <= x6 < rows and 0 <= y6 < cols):
                continue
            if d5 == d4 == d3 == d2 == d1 == (dx, dy):
                continue
            if (x6, y6, (d4, d3, d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy))) in visited:
                continue
            heappush(
                queue,
                (
                    s + grid[x1][y1] + grid[x2][y2] + grid[x3][y3] + grid[x4][y4] + grid[x5][y5] + grid[x6][y6],
                    x6,
                    y6,
                    (d4, d3, d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy)),
                ),
            )

            x7, y7 = x6 + dx, y6 + dy
            if not (0 <= x7 < rows and 0 <= y7 < cols):
                continue
            if d4 == d3 == d2 == d1 == (dx, dy):
                continue
            if (x7, y7, (d3, d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy))) in visited:
                continue
            heappush(
                queue,
                (
                    s + grid[x1][y1] + grid[x2][y2] + grid[x3][y3] + grid[x4][y4] + grid[x5][y5] + grid[x6][y6] + grid[x7][y7],
                    x7,
                    y7,
                    (d3, d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy)),
                ),
            )

            x8, y8 = x7 + dx, y7 + dy
            if not (0 <= x8 < rows and 0 <= y8 < cols):
                continue
            if d3 == d2 == d1 == (dx, dy):
                continue
            if (x8, y8, (d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy))) in visited:
                continue
            heappush(
                queue,
                (
                    s + grid[x1][y1] + grid[x2][y2] + grid[x3][y3] + grid[x4][y4] + grid[x5][y5] + grid[x6][y6] + grid[x7][y7] + grid[x8][y8],
                    x8,
                    y8,
                    (d2, d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy)),
                ),
            )

            x9, y9 = x8 + dx, y8 + dy
            if not (0 <= x9 < rows and 0 <= y9 < cols):
                continue
            if d2 == d1 == (dx, dy):
                continue
            if (x9, y9, (d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy))) in visited:
                continue
            heappush(
                queue,
                (
                    s + grid[x1][y1] + grid[x2][y2] + grid[x3][y3] + grid[x4][y4] + grid[x5][y5] + grid[x6][y6] + grid[x7][y7] + grid[x8][y8] + grid[x9][y9],
                    x9,
                    y9,
                    (d1, (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy)),
                ),
            )

            x10, y10 = x9 + dx, y9 + dy
            if not (0 <= x10 < rows and 0 <= y10 < cols):
                continue
            if d1 == (dx, dy):
                continue
            if (x10, y10, ((dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy))) in visited:
                continue
            heappush(
                queue,
                (
                    s + grid[x1][y1] + grid[x2][y2] + grid[x3][y3] + grid[x4][y4] + grid[x5][y5] + grid[x6][y6] + grid[x7][y7] + grid[x8][y8] + grid[x9][y9] + grid[x10][y10],
                    x10,
                    y10,
                    ((dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy), (dx, dy)),
                ),
            )

    raise ValueError


if __name__ == "__main__":
    sys.exit(main())
