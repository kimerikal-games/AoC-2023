"""
Advent of Code 2023 - Day 1: Trebuchet?!
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys

_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
_DIGIT_MAP = {word: digit for digit, word in enumerate(_WORDS, start=1)}
_DIGIT_MAP |= {str(digit): digit for digit in range(10)}


def main() -> int:
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

    return 0


def part1(lines: list[str]) -> int:
    return sum(map(get_part1_line_value, lines))


def part2(lines: list[str]) -> int:
    return sum(map(get_part2_line_value, lines))


def get_part1_line_value(line: str) -> int:
    digits = [int(digit) for digit in line.strip() if digit.isdigit()]
    value = 10 * digits[0] + digits[-1]
    return value


def get_part2_line_value(line: str) -> int:
    index_value_pairs: list[tuple[int, int]] = []
    for word, value in _DIGIT_MAP.items():
        last = 0
        while (index := line.find(word, last)) != -1:
            last = index + 1
            index_value_pairs.append((index, value))
    value = 10 * min(index_value_pairs)[1] + max(index_value_pairs)[1]
    return value


if __name__ == "__main__":
    sys.exit(main())
