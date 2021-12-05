from aoc.day04.game import Game


class GiveawayGame(Game):
    def __init__(self, raw_game: list[str]):
        super().__init__(raw_game)
        self.won_boards_with_positions = []

    def detect_winning_position(self) -> [int, list[int]]:
        won_boards = map(lambda wb: wb[0], self.won_boards_with_positions)
        still_playing_boards = [
            b for b in self.boards
            if b not in won_boards
        ]
        for board in still_playing_boards:
            winning_position = board.detect_winning_position()
            if winning_position is not None:
                self.won_boards_with_positions.append([board, winning_position])

        if len(self.won_boards_with_positions) == len(self.boards):
            return self.won_boards_with_positions[-1]
        else:
            return None
