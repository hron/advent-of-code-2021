# Advent of Code - Day 5 - Part One
from aoc.day05.line import Line, DiagonalLineNotSupported


def result(raw_input: list[str]):
    lines = [
        Line.parse(raw_line) for raw_line in raw_input
    ]

    points = set()
    for l1 in range(len(lines)):
        for l2 in range(l1 + 1, len(lines)):
            try:
                intersection_point = lines[l1].intersection_points(lines[l2])
            except DiagonalLineNotSupported:
                continue
            if intersection_point is not None:
                points.update(intersection_point)

    return len(points)
