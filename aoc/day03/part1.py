# Advent of Code - Day 3 - Part One
from aoc.day03.shared import bin_to_decimal, parse_report


def result(diagnostic_report: list[str]):
    diagnostic_report = parse_report(diagnostic_report)
    gamma_rate = []
    epsilon_rate = []
    for i in range(len(diagnostic_report[0])):
        zero_counts = len([
            diagnostic_report[d][i] for d in range(len(diagnostic_report)) if diagnostic_report[d][i] == 0
        ])
        if zero_counts > len(diagnostic_report) - zero_counts:
            gamma_rate.append(0)
            epsilon_rate.append(1)
        else:
            gamma_rate.append(1)
            epsilon_rate.append(0)

    return bin_to_decimal(gamma_rate) * bin_to_decimal(epsilon_rate)


