"""
Advent of Code 2023 - Day 5: If You Give A Seed A Fertilizer
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from itertools import count

Category = str
CategoryMap = list[tuple[int, int, int]]


def main() -> int:
    input = sys.stdin.readline

    seeds = list(map(int, input().strip().removeprefix("seeds: ").split()))
    input()

    maps = {}
    while True:
        line = input().strip()
        if not line:
            break
        src_cat, dst_cat = tuple(line.removesuffix(" map:").split("-to-"))

        cat_maps = []
        while True:
            line = input().strip()
            if not line:
                break
            dst_start, src_start, length = map(int, line.split())
            src_end = src_start + length
            offset = dst_start - src_start
            cat_maps.append((src_start, src_end, offset))
        cat_maps.sort()

        maps[src_cat] = (dst_cat, cat_maps)

    print("Part 1:", part1(seeds, maps))
    print("Part 2:", part2(seeds, maps))

    return 0


def part1(seeds: list[int], maps: dict[Category, tuple[Category, CategoryMap]]):
    return min(forward(maps, seed, "seed", "location") for seed in seeds)


def part2(seeds: list[int], maps: dict[Category, tuple[Category, CategoryMap]]):
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_start, seed_range = seeds[i : i + 2]
        seed_end = seed_start + seed_range
        seed_ranges.append((seed_start, seed_end))
    seed_ranges.sort()

    rev_maps = {}
    for src_cat, (dst_cat, cat_maps) in maps.items():
        cat_rev_maps = []
        for src_start, src_end, offset in cat_maps:
            dst_start = src_start + offset
            dst_end = src_end + offset
            offset = -offset
            cat_rev_maps.append((dst_start, dst_end, offset))
        cat_rev_maps.sort()
        rev_maps[dst_cat] = (src_cat, cat_rev_maps)

    for location in count(start=0):
        seed = forward(rev_maps, location, "location", "seed")
        for seed_start, seed_end in seed_ranges:
            if seed_start <= seed < seed_end:
                return location


def forward(maps: dict[Category, tuple[Category, CategoryMap]], value: int, in_cat: Category, out_cat: Category):
    src_cat = in_cat
    while src_cat != out_cat:
        dst_cat, cat_maps = maps[src_cat]

        for src_start, src_end, offset in cat_maps:
            if src_start <= value < src_end:
                value += offset
                break

        src_cat = dst_cat
    return value


if __name__ == "__main__":
    sys.exit(main())
