"""
Advent of Code 2023 - Day 19: Aplenty
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import Iterator
from math import prod

Category = str
Operator = str
Rating = int
Expression = tuple[Category, Operator, Rating]
NodeID = str
Decider = tuple[Expression, NodeID, NodeID]
Graph = dict[NodeID, Decider]
Config = dict[Category, Rating]
RangedConfig = dict[Category, tuple[Rating, Rating]]

TERMINALS = ("A", "R")
OPERATOR_FUNCTIONS = {"<": Rating.__lt__, ">": Rating.__gt__}


def main() -> int:
    front, back = sys.stdin.read().split("\n\n")

    graph: Graph = {}
    for line in front.splitlines():
        graph.update(parse_graph_line(line.strip()))

    configs = [parse_config_line(line.strip()) for line in back.splitlines()]

    print("Part 1:", part1(graph, configs))
    print("Part 2:", part2(graph))

    return 0


def parse_graph_line(line: str) -> Iterator[tuple[NodeID, Decider]]:
    node_id_base, line = line.rstrip("}").split("{")
    *rules_raw, name_fallback = line.split(",")

    for i, rule_raw in enumerate(rules_raw):
        rule_raw, node_id_then_base = rule_raw.split(":")
        category, operator, threshold = rule_raw[0], rule_raw[1], int(rule_raw[2:])

        node_id = make_node_id(node_id_base, i)
        node_id_then = make_node_id(node_id_then_base, 0)
        node_id_else = make_node_id(node_id_base, i + 1) if i < len(rules_raw) - 1 else make_node_id(name_fallback, 0)
        decider = ((category, operator, threshold), node_id_then, node_id_else)

        yield node_id, decider


def parse_config_line(line: str) -> Config:
    config: Config = {}

    for part_raw in line[1:-1].split(","):
        category, rating_raw = part_raw.split("=")
        config[category] = int(rating_raw)

    return config


def make_node_id(base: str, index: int) -> str:
    if base in TERMINALS:
        return base
    return f"{base}{index}"


def part1(graph: Graph, configs: list[Config]) -> int:
    result = 0

    for config in configs:
        node_id = "in0"

        while node_id not in TERMINALS:
            (category, operator, threshold), name_then, name_else = graph[node_id]
            func = OPERATOR_FUNCTIONS[operator]
            rating = config[category]
            node_id = name_then if func(rating, threshold) else name_else

        if node_id == "A":
            result += sum(config.values())

    return result


def part2(graph: Graph) -> int:
    config: RangedConfig = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    configs = filter_config(graph, "in0", config)
    return sum(prod(e - s + 1 for s, e in config.values()) for config in configs)


def filter_config(graph: Graph, node_id: NodeID, config: RangedConfig) -> list[RangedConfig]:
    if any(start > end for start, end in config.values()):
        return []

    if node_id == "A":
        return [config]
    elif node_id == "R":
        return []

    (category, operator, threshold), node_id_then, node_id_else = graph[node_id]
    start, end = config[category]

    if operator == "<":
        cut, node_id_left, node_id_right = threshold - 1, node_id_then, node_id_else
    elif operator == ">":
        cut, node_id_left, node_id_right = threshold, node_id_else, node_id_then
    else:
        assert False

    config_left = {**config, category: (start, min(end, cut))}
    config_right = {**config, category: (max(start, cut + 1), end)}

    return filter_config(graph, node_id_left, config_left) + filter_config(graph, node_id_right, config_right)


if __name__ == "__main__":
    sys.exit(main())
