from aoc.day05.point import Point


class Line:
    @classmethod
    def parse(cls, raw_line):
        [p1, p2] = [Point.parse(raw_point) for raw_point in raw_line.split(' -> ')]
        return Line(p1, p2)

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return "{} -> {}".format(self.p1, self.p2)

    def intersection_points(self, another_line: 'Line') -> set[Point]:
        return self.points() & another_line.points()

    def points(self):
        xxs = [self.p1.x, self.p2.x]
        yys = [self.p1.y, self.p2.y]
        if self.p1.x == self.p2.x:
            return {Point(self.p1.x, y) for y in range(min(yys), max(yys) + 1)}
        elif self.p1.y == self.p2.y:
            return {Point(x, self.p1.y) for x in range(min(xxs), max(xxs) + 1)}
        else:
            raise DiagonalLineNotSupported


class DiagonalLineNotSupported(RuntimeError):
    pass


