"""
Advent of Code 2023 - Day 18: Lavaduct Lagoon
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import TypeAlias

Color: TypeAlias = str
Dig = tuple[str, int, Color]

MOVES = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
LARGE = sys.maxsize


def main() -> int:
    plan: list[Dig] = []
    for line in sys.stdin:
        args = line.split()
        direction = args[0]
        length = int(args[1])
        color: Color = args[2][2:8]
        plan.append((direction, length, color))

    print("Part 1:", part1(plan))
    print("Part 2:", part2(plan))

    return 0


def part1(plan: list[Dig]) -> int:
    return compute_area(plan)


def part2(plan: list[Dig]) -> int:
    return compute_area(fix_plan(plan))


def fix_plan(plan: list[Dig]) -> list[Dig]:
    new_plan: list[Dig] = []
    for _, _, color in plan:
        direction = "RDLU"[int(color[5])]
        length = int(color[0:5], 16)
        new_plan.append((direction, length, ""))
    return new_plan


def compute_area(plan: list[Dig]) -> int:
    y0 = x0 = 0
    inner = sides = 0

    for direction, length, _ in plan:
        dy, dx = MOVES[direction]
        y1, x1 = y0 + dy * length, x0 + dx * length
        inner += (y0 + y1) * (x1 - x0) - (x0 + x1) * (y1 - y0)
        sides += length

        y0, x0 = y1, x1

    inner = abs(inner) // 2
    area = (inner + sides) // 2 + 1
    return area


if __name__ == "__main__":
    sys.exit(main())
