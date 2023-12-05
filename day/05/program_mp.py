"""
Advent of Code 2023 - Day 5: If You Give A Seed A Fertilizer
Author: kimerikal <kimerikal.games@gmail.com>
Note: The measured main solution is program.py. This code is an attempt to speed up the bruteforce
    solution using multiprocessing.
"""
import sys
import multiprocessing as mp
from functools import partial


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


def part1(seeds, maps):
    locations = []
    for seed in seeds:
        location = forward(maps, seed, "seed", "location")
        locations.append(location)
    return min(locations)


def part2(seeds, maps):
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_start, seed_range = seeds[i : i + 2]
        seed_end = seed_start + seed_range
        chunk_size = 1_000_000
        for chunk_start in range(seed_start, seed_end, chunk_size):
            chunk_end = min(chunk_start + chunk_size, seed_end)
            seed_ranges.append((chunk_start, chunk_end))
    seed_ranges.sort(key=len)

    forward_unit_with_maps = partial(forward_unit, maps=maps, in_cat="seed", out_cat="location")
    with mp.Pool(max(1, mp.cpu_count() // 2)) as pool:
        min_location = min(pool.map(forward_unit_with_maps, seed_ranges))

    return min_location


def forward(maps, seed, in_cat, out_cat):
    value, src_cat = seed, in_cat
    while src_cat != out_cat:
        dst_cat, cat_maps = maps[src_cat]

        lo, hi = 0, len(cat_maps)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            dst_start, _, _ = cat_maps[mid]
            if value < dst_start:
                hi = mid
            else:
                lo = mid

        dst_start, dst_end, offset = cat_maps[lo]
        if dst_start <= value < dst_end:
            value += offset

        src_cat = dst_cat
    return value


def forward_unit(seed_range, maps, in_cat, out_cat):
    unit_min_location = float("inf")
    for seed in range(*seed_range):
        location = forward(maps, seed, in_cat, out_cat)
        unit_min_location = min(unit_min_location, location)
    return unit_min_location


if __name__ == "__main__":
    sys.exit(main())
