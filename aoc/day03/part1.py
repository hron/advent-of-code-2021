# Advent of Code - Day 3 - Part One

def result(diagnostic_report: list[str]):
    diagnostic_report = [[int(c) for c in d] for d in diagnostic_report]
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


def bin_to_decimal(binary: list[int]):
    decimal = 0
    i = 0
    for d in reversed(binary):
        if i == 0:
            decimal += d
        else:
            decimal += d * 2**i
        i += 1

    return decimal
