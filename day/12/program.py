"""
Advent of Code 2023 - Day 12: Hot Springs
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from collections import Counter


def main() -> int:
    all_reads: list[str] = []
    all_sizes: list[list[int]] = []
    for line in sys.stdin:
        reads, line = line.split()
        sizes = list(map(int, line.split(",")))
        all_reads.append(reads)
        all_sizes.append(sizes)

    print("Part 1:", part1(all_reads, all_sizes))
    print("Part 2:", part2(all_reads, all_sizes))

    return 0


def part1(all_reads: list[str], all_sizes: list[list[int]]) -> int:
    return sum(map(compute_arrangements, all_reads, all_sizes))


def part2(all_reads: list[str], all_sizes: list[list[int]]) -> int:
    all_reads = ["?".join(reads for _ in range(5)) for reads in all_reads]
    all_sizes = [sizes * 5 for sizes in all_sizes]

    return sum(map(compute_arrangements, all_reads, all_sizes))


def compute_arrangements(reads: str, sizes: list[int]) -> int:
    reads = f".{reads}."
    n = len(reads)

    prev = [Counter({0: 1}) for _ in range(n)]
    for size in sizes:
        curr = [Counter() for _ in range(n)]
        for j in range(size + 1, n):
            section = reads[j - size : j]
            if reads[j - size - 1] == "#" or reads[j] == "#" or "." in section:
                continue
            octo_curr = section.count("#")
            curr[j] += Counter({octo_prev + octo_curr: count for octo_prev, count in prev[j - size - 1].items()})
        for j in range(1, n):
            curr[j] += curr[j - 1]
        prev = curr

    total_octo = reads.count("#")
    total_count = prev[-1][total_octo]

    return total_count


if __name__ == "__main__":
    sys.exit(main())
