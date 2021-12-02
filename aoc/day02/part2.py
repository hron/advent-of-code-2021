# Advent of Code - Day 2 - Part Two

def result(commands: list[str]):
    horizontal = 0
    depth = 0
    aim = 0
    for c in commands:
        [command, argument] = c.split(' ')
        argument = int(argument)
        if command == 'forward':
            horizontal += argument
            depth += aim * argument
        elif command == 'up':
            aim -= argument
        else:
            aim += argument

    return horizontal * depth
