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


def parse_report(diagnostic_report):
    return [[int(c) for c in d] for d in diagnostic_report]
