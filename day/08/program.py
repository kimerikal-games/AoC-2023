"""
Advent of Code 2023 - Day 8: Haunted Wasteland
Author: kimerikal <kimerikal.games@gmail.com>
"""
import re
import sys
from itertools import cycle
from math import lcm


def main() -> int:
    input = sys.stdin.readline
    line_p = re.compile(r"(?P<node>\w+) = \((?P<left>\w+), (?P<right>\w+)\)")

    instructions = input().strip()
    input()

    graph = {}
    while line := input().strip():
        assert (m := line_p.match(line))
        node = m.group("node")
        left = m.group("left")
        right = m.group("right")
        graph[node] = (left, right)

    print("Part 1:", part1(instructions, graph))
    print("Part 2:", part2(instructions, graph))

    return 0


def part1(instructions: str, graph: dict[str, tuple[str, str]]):
    node = "AAA"
    for step, instruction in enumerate(cycle(instructions), start=1):
        if instruction == "L":
            node = graph[node][0]
        elif instruction == "R":
            node = graph[node][1]
        if node == "ZZZ":
            return step


def part2(instructions: str, graph: dict[str, tuple[str, str]]):
    nodes = [node for node in graph if node[-1] == "A"]
    cycles: list[int] = []
    for node in nodes:
        for step, d in enumerate(cycle(instructions), start=1):
            if d == "L":
                node = graph[node][0]
            elif d == "R":
                node = graph[node][1]
            if node[-1] == "Z":
                cycles.append(step)
                break
    return lcm(*cycles)


if __name__ == "__main__":
    sys.exit(main())
