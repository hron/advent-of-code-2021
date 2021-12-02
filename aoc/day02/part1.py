# Advent of Code - Day 2 - Part One

def result(commands: list[str]):
    horizontal = 0
    depth = 0
    for c in commands:
        [command, argument] = c.split(' ')
        argument = int(argument)
        if command == 'forward':
            horizontal += argument
        elif command == 'up':
            depth -= argument
        else:
            depth += argument

    return horizontal * depth
