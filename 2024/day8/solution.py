# 35:14

import math
import numpy as np

f = open("./input.txt", "r")
input = f.read()
lines = input.splitlines()

def count_antinodes(with_resonance=False):
    grid = np.array([[a for a in line] for line in lines])
    antinodes = set()
    for digit in grid.flatten():
        if digit != ".":
            digit_locs = np.argwhere(grid == digit)
            for loc in digit_locs:
                for other_loc in digit_locs:
                    if not np.all(loc == other_loc):
                        separation_vector = loc - other_loc
                        if with_resonance:
                            # Get the shortest vector that takes integer values which is parallel
                            # to the separation vector.
                            separation_vector = np.int32(separation_vector / math.gcd(*separation_vector))
                            new_antinode = loc
                            while not np.any(new_antinode < 0) and not np.any(new_antinode >= len(grid)):
                                antinodes.add(str(new_antinode))
                                new_antinode = new_antinode + separation_vector
                        else:
                            new_antinode = loc + separation_vector
                            if not np.any(new_antinode < 0) and not np.any(new_antinode >= len(grid)):
                                antinodes.add(str(new_antinode))

    return len(antinodes)

print(f"Part 1: {count_antinodes()}")
print(f"Part 2: {count_antinodes(True)}")
