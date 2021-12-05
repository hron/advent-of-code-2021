from aoc.day04.board import Board


class Game:
    board_size = 5

    def __init__(self, raw_game: list[str]):
        self.draw: list[int] = [int(d) for d in raw_game[0].split(',')]
        self.boards = [
            Board(raw_game[board_start:board_start + Game.board_size])
            for board_start in range(2, len(raw_game), Game.board_size + 1)
        ]
        self.winning_number = None
        self.winning_combination = None
        self.winning_board = None

    def perform(self):
        for d in self.draw:
            for board in self.boards:
                board.mark(d)
            if self.is_victory():
                self.winning_number = d
                [winning_board, winning_combination] = self.detect_winning_position()
                self.winning_board = self.boards.index(winning_board)
                self.winning_combination = [cell.value for cell in winning_combination]
                break
        else:
            raise 'Nobody wins!'

    def in_progress(self):
        return not self.is_victory()

    def is_victory(self):
        if self.detect_winning_position() is None:
            return False
        else:
            return True

    def detect_winning_position(self) -> [int, list[int]]:
        for board in self.boards:
            winning_position = board.detect_winning_position()
            if winning_position is not None:
                return board, winning_position
        return None

    def __repr__(self):
        to_print = ""
        for board in self.boards:
            for row in board.rows():
                to_print += ' '.join([cell.__repr__() for cell in row]) + '\n'
            to_print += '\n'
        return to_print

    def all_unmarked_numbers(self, board_index: int):
        result = []
        for row in self.boards[board_index].rows():
            for cell in row:
                if not cell.is_marked():
                    result.append(cell.value)
        return result
