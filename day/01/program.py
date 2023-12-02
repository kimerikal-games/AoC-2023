"""
Advent of Code 2023 - Day 1: Trebuchet?!
Author: kimerikal <kimerikal.games@gmail.com>
"""
import sys


def main() -> int:
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

    return 0


def part1(lines: list[str]):
    total = 0
    for line in lines:
        digits = [int(digit) for digit in line.strip() if digit.isdigit()]
        if digits:
            first = digits[0]
            last = digits[-1]
            value = 10 * first + last
        else:
            value = 0
        total += value

    return total


def part2(lines: list[str]):
    tofind = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    tofind |= {str(digit): digit for digit in range(10)}

    total = 0
    for line in lines:
        digits = []
        for word, value in tofind.items():
            last = 0
            while True:
                index = line.find(word, last)
                if index == -1:
                    break
                last = index + 1
                digits.append((index, value))
        if digits:
            first = min(digits)[1]
            last = max(digits)[1]
            value = 10 * first + last
        else:
            value = 0
        total += value

    return total


if __name__ == "__main__":
    sys.exit(main())
