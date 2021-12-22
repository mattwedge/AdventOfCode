# 1:21:38

import numpy as np
import copy
from functools import reduce
from collections import Counter

def subtract_cube(start_cube, remove_cube):
    all_new_cubes = []

    for i in range(3):
        if remove_cube[i][0] > start_cube[i][1]:
            return [start_cube]
        if remove_cube[i][1] < start_cube[i][0]:
            return [start_cube]

    for i in range(3):
        if start_cube[i][0] < remove_cube[i][0]:
            below_x = copy.deepcopy(start_cube)
            below_x[i][1] = remove_cube[i][0] - 1
            all_new_cubes.append(below_x)

        if start_cube[i][1] > remove_cube[i][1]:
            above_x = copy.deepcopy(start_cube)
            above_x[i][0] = remove_cube[i][1] + 1
            all_new_cubes.append(above_x)

    return all_new_cubes

def count_volume(cubes):
    if len(cubes) == 1:
        return np.prod([(1 + cubes[0][i][1] - cubes[0][i][0]) for i in range(3)])

    vol = 0
    for i, cube in enumerate(cubes):
        prev_cubes = cubes[:i]
        new_cubes = [cube]
        
        for prev_cube in prev_cubes:
            new_cubes = reduce(lambda x, y: x + y, [subtract_cube(cube_part, prev_cube) for cube_part in new_cubes], [])

        vol += count_volume(new_cubes)

    return vol

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read().splitlines()

    parsed_lines = []
    for ln in input:
        parts = ln.split(" ")
        action = parts[0]
        
        coords = parts[1].split(",")
        coords_parsed = [ [int(a) for a in coord.split("=")[1].split("..")] for coord in coords ]

        parsed_lines.append({
            "action": action,
            "coords": coords_parsed
        })

    # Part 1
    reactor = np.zeros((101, 101, 101), dtype=int)
    for ln in parsed_lines:
        if ln["action"] == "on":
            reactor[
                ln["coords"][0][0] + 50: ln["coords"][0][1] + 51,
                ln["coords"][1][0] + 50: ln["coords"][1][1] + 51,
                ln["coords"][2][0] + 50: ln["coords"][2][1] + 51,
            ] = 1

        if ln["action"] == "off":
            reactor[
                ln["coords"][0][0] + 50: ln["coords"][0][1] + 51,
                ln["coords"][1][0] + 50: ln["coords"][1][1] + 51,
                ln["coords"][2][0] + 50: ln["coords"][2][1] + 51,
            ] = 0
    print(Counter(reactor.flatten())[1])

    # Part 2
    all_cubes = []
    for ln in parsed_lines:
        if ln["action"] == "on":
            all_cubes.append(ln["coords"])

        if ln["action"] == "off":
            new_cubes = []
            for cube in all_cubes:
                new_cubes += subtract_cube(cube, ln["coords"])

            all_cubes = new_cubes


    # Slight optimisation - this still takes a few minutes to run. TODO - speed up
    def contains_cube(inner, outer):
        return all(outer[i][0] <= inner[i][0] and outer[i][1] >= inner[i][1] for i in range(3))

    all_cubes = [cube for cube in all_cubes if not any(contains_cube(cube, outer_cube) for outer_cube in [c for c in all_cubes if not c == cube])]
    print(count_volume(all_cubes))
