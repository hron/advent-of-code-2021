class Point:
    @classmethod
    def parse(cls, raw_point):
        [x, y] = [int(c) for c in raw_point.split(',')]
        return Point(x, y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "{},{}".format(self.x, self.y)
