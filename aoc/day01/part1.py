# Advent of Code - Day 1 - Part One

def result(depths: list[str]):
    depths = [int(d) for d in depths]
    increases_count = 0
    current_depth = depths[0]
    for d in depths:
        if current_depth < d:
            increases_count += 1
        current_depth = d

    return increases_count
