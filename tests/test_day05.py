from aoc.day05.point import Point
from aoc.day05.line import Line
from aoc.day05 import part1, part2

sample_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()


#
# --- Part One ---
#

def test_part1():
    assert part1.result(sample_input) == 5


#
# --- Part Two ---
#

def test_part2():
    assert part2.result(sample_input) == 12


def test_line_points():
    line = Line(Point(0, 9), Point(5, 9))
    assert line.points() == {Point(i, 9) for i in range(0, 6)}

    diagonal_line = Line(Point(1, 1), Point(3, 3))
    assert diagonal_line.points() == {Point(x, y) for (x, y) in [(1,1), (2,2), (3,3)]}

    diagonal_line2 = Line(Point(9, 7), Point(7, 9))
    assert diagonal_line2.points() == {Point(x, y) for (x, y) in [(9,7), (8,8), (7,9)]}


def test_line_intersection_points():
    line = Line(Point(0, 9), Point(5, 9))
    line2 = Line(Point(0, 9), Point(2, 9))
    assert line.intersection_points(line2) == {Point(i, 9) for i in range(0, 3)}
