# Advent of Code - Day 4 - Part Two
from aoc.day04.giveaway_game import GiveawayGame


def result(raw_bingo_game: list[str]):
    game = GiveawayGame(raw_bingo_game)
    game.perform()

    return sum(game.all_unmarked_numbers(game.winning_board)) * game.winning_number
