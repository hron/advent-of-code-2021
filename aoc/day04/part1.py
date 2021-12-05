# Advent of Code - Day 4 - Part One
from aoc.day04.game import Game


def result(raw_bingo_game: list[str]):
    game = Game(raw_bingo_game)
    game.perform()

    return sum(game.all_unmarked_numbers(game.winning_board)) * game.winning_number
