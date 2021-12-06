from aoc.day05.line import Line


class Field:
    def __init__(self, size_x: int, size_y: int):
        self.field = [
            [0 for y in range(size_y + 1)]
            for _ in range(size_x + 1)
        ]

    def draw_line(self, line: Line):
        for p in line.points():
            self.field[p.x][p.y] += 1

    def number_of_lines_at(self, x: int, y: int):
        return self.field[x][y]

    def size_x(self):
        return len(self.field)

    def size_y(self):
        return len(self.field[0])
