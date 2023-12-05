"""
Advent of Code 2023 - Day 5: If You Give A Seed A Fertilizer
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys
from itertools import count


Category = str
CategoryMap = list[tuple[int, int, int]]  # [(start, end, offset)]
Maps = dict[Category, tuple[Category, CategoryMap]]


def main() -> int:
    maps, seeds = parse_input()

    print("Part 1:", part1(maps, seeds))
    print("Part 2:", part2(maps, seeds))

    return 0


def parse_input() -> tuple[Maps, list[int]]:
    blocks = sys.stdin.read().split("\n\n")
    seeds_raw, *maps_raw = blocks
    seeds = list(map(int, seeds_raw.removeprefix("seeds: ").split()))
    maps = {}
    for map_raw in maps_raw:
        map_meta_raw, *map_data_raw = map_raw.splitlines()
        src_cat, dst_cat = map_meta_raw.removesuffix(" map:").split("-to-")
        cat_maps = []
        for line in map_data_raw:
            dst_start, src_start, length = map(int, line.split())
            src_end = src_start + length
            offset = dst_start - src_start
            cat_maps.append((src_start, src_end, offset))
        cat_maps.sort()
        maps[src_cat] = (dst_cat, cat_maps)
    return maps, seeds


def part1(maps: Maps, seeds: list[int]) -> int:
    return min(propagate(maps, seed, "seed", "location") for seed in seeds)


def part2(maps: Maps, seeds: list[int]) -> int:
    inv_maps = get_inverse_maps(maps)
    seed_ranges = get_seed_ranges(seeds)
    for location in count(start=0):
        seed = propagate(inv_maps, location, "location", "seed")
        for seed_start, seed_end in seed_ranges:
            if seed_start <= seed < seed_end:
                return location
    assert False, "Unreachable"


def propagate(maps: Maps, value: int, in_cat: Category, out_cat: Category) -> int:
    src_cat = in_cat
    while src_cat != out_cat:
        dst_cat, cat_maps = maps[src_cat]
        for src_start, src_end, offset in cat_maps:
            if src_start <= value < src_end:
                value += offset
                break
        src_cat = dst_cat
    return value


def get_inverse_maps(maps: Maps) -> Maps:
    return {
        dst_cat: (src_cat, get_inverse_cat_maps(cat_maps))
        for src_cat, (dst_cat, cat_maps) in maps.items()
    }


def get_inverse_cat_maps(cat_maps: CategoryMap) -> CategoryMap:
    inv_cat_maps = []
    for src_start, src_end, offset in cat_maps:
        dst_start = src_start + offset
        dst_end = src_end + offset
        offset = -offset
        inv_cat_maps.append((dst_start, dst_end, offset))
    inv_cat_maps.sort()
    return inv_cat_maps


def get_seed_ranges(seeds: list[int]) -> list[tuple[int, int]]:
    seed_ranges = []
    for seed_start, seed_range in zip(seeds[0::2], seeds[1::2]):
        seed_end = seed_start + seed_range
        seed_ranges.append((seed_start, seed_end))
    seed_ranges.sort()
    return seed_ranges


if __name__ == "__main__":
    sys.exit(main())
