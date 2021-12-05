from aoc.day04.cell import Cell


class Board:
    def __init__(self, raw_board: list[str]):
        self.board_state = [
            [Cell(int(d)) for d in r.split()]
            for r in raw_board
        ]

    def mark(self, number: int):
        for row in self.board_state:
            for cell in row:
                if cell.value == number:
                    cell.mark()

    def rows(self):
        return self.board_state

    def columns(self):
        clmns = []
        for c in range(len(self.board_state[0])):
            clmns.append([])
            for r in range(len(self.board_state[0])):
                clmns[-1].append(self.board_state[r][c])
        return clmns

    def detect_winning_position(self):
        for row in self.rows():
            for cell in row:
                if not cell.is_marked():
                    break
            else:
                return row
        for column in self.columns():
            for cell in column:
                if not cell.is_marked():
                    break
            else:
                return column
        return None

