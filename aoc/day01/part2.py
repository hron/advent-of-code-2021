# Advent of Code - Day 1 - Part Two

def result(depths: list[str]):
    depths = [int(d) for d in depths]
    increases_count = 0
    for c in range(len(depths) - 3):
        d1 = sum(depths[c:c+3])
        d2 = sum(depths[c+1:c+4])
        if d1 < d2:
            increases_count += 1

    return increases_count

