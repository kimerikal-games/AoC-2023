"""
Advent of Code 2023 - Day 15: Lens Library
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from typing import Callable


class Node:
    def __init__(self, key: str, value: int) -> None:
        self.key = key
        self.value = value


class Boxes:
    def __init__(self, hash_fn: Callable[[str], int], num_boxes: int) -> None:
        self._boxes: list[list[Node]] = [[] for _ in range(num_boxes)]
        self._hash_fn = hash_fn

    def __setitem__(self, key: str, value: int) -> None:
        box = self._boxes[self._hash_fn(key)]
        for node in box:
            if node.key == key:
                node.value = value
                return
        box.append(Node(key, value))

    def __delitem__(self, key: str) -> None:
        box = self._boxes[self._hash_fn(key)]
        for i, node in enumerate(box):
            if node.key == key:
                del box[i]
                return

    def compute_power(self) -> int:
        # fmt: off
        return sum(
            box_id * slot_id * node.value
            for box_id, box in enumerate(self._boxes, start=1)
            for slot_id, node in enumerate(box, start=1)
        )  # fmt: on


def main() -> int:
    seqs = sys.stdin.readline().split(",")

    print("Part 1:", part1(seqs))
    print("Part 2:", part2(seqs))

    return 0


def part1(seqs: list[str]) -> int:
    return sum(map(compute_HASH, seqs))


def part2(seqs: list[str]) -> int:
    boxes = Boxes(compute_HASH, 256)

    for seq in seqs:
        if "=" in seq:
            args = seq.split("=")
            label, value = args[0], int(args[1])
            boxes[label] = value
        elif "-" in seq:
            label = seq.rstrip("-")
            del boxes[label]

    return boxes.compute_power()


def compute_HASH(seq: str) -> int:
    value = 0
    for c in seq:
        value = (value + ord(c)) * 17 % 256
    return value


if __name__ == "__main__":
    sys.exit(main())
