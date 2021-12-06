# Advent of Code - Day 5 - Part One
from aoc.day05.line import Line, DiagonalLineNotSupported
from aoc.day05.field import Field


def result(raw_input: list[str]):
    field_size = (0, 0)
    lines = []
    for raw_line in raw_input:
        l = Line.parse(raw_line)
        lines.append(l)
        field_size = (
            max([field_size[0], l.p1.x, l.p2.x]),
            max([field_size[1], l.p1.y, l.p2.y]),
        )
    field = Field(field_size[0], field_size[1])

    for line in lines:
        try:
            field.draw_line(line)
        except DiagonalLineNotSupported:
            continue

    overlaps = 0
    for x in range(field.size_x()):
        for y in range(field.size_y()):
            if field.number_of_lines_at(x, y) > 1:
                overlaps += 1

    return overlaps
