# Advent of Code - Day 3 - Part Two
from aoc.day03.shared import parse_report, bin_to_decimal


def find_number_by_criteria(report: list[list[int]], detect_bit_criteria, position = 0):
    bit_criteria = detect_bit_criteria(report, position)
    candidates = [
        c for c in report if c[position] == bit_criteria
    ]
    if len(candidates) == 1:
        return candidates[0]
    else:
        return find_number_by_criteria(candidates, detect_bit_criteria, position + 1)


def detect_most_common(report: list[list[int]], position: int):
    zeroes_count = len([
        report[d][position] for d in range(len(report)) if report[d][position] == 0
    ])

    if zeroes_count > len(report) - zeroes_count:
        return 0
    else:
        return 1


def detect_less_common(report: list[list[int]], position: int):
    most_common = detect_most_common(report, position)
    return 1 if most_common == 0 else 0


def result(report: list[str]):
    report = parse_report(report)

    oxygen_generator_rating = find_number_by_criteria(report, detect_most_common)
    co2_scrubber_rating = find_number_by_criteria(report, detect_less_common)

    return bin_to_decimal(oxygen_generator_rating) * bin_to_decimal(co2_scrubber_rating)
