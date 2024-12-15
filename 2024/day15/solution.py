# 1:58:46

import numpy as np

dirsdict  = {
    "^": np.array([-1, 0]),
    ">": np.array([0, 1]),
    "<": np.array([0, -1]),
    "v": np.array([1, 0]),
}

class WallError(Exception):
    pass

class UnknownError(Exception):
    pass


def dedupearrs(arrs: list[np.ndarray]):
    deduped = []
    for l in arrs:
        if not str(l) in [str(a) for a in deduped]:
            deduped.append(l)

    return deduped

def get_squares_to_push(grid: np.ndarray, pos: np.ndarray, dirstr: str):
    dir = dirsdict[dirstr]

    v = grid[(pos + dir)[0]][(pos + dir)[1]]
    if v == "#":
        raise WallError("BOX")
    
    if v == ".":
        return [pos]
    
    if v == "[":
        if dirstr in ["<", ">"]:
            return dedupearrs([pos] + get_squares_to_push(grid, pos + dir, dirstr))
        if dirstr in ["^", "v"]:
            return dedupearrs([pos] + get_squares_to_push(grid, pos + dir, dirstr) + get_squares_to_push(grid, pos + dir + dirsdict[">"], dirstr))
        
    if v == "]":
        if dirstr in ["<", ">"]:
            return dedupearrs([pos] + get_squares_to_push(grid, pos + dir, dirstr))
        if dirstr in ["^", "v"]:
            return dedupearrs([pos] + get_squares_to_push(grid, pos + dir, dirstr) + get_squares_to_push(grid, pos + dir + dirsdict["<"], dirstr))
        
    if v == "O":
        return [pos] + get_squares_to_push(grid, pos + dir, dirstr)
    
    
    raise UnknownError(v)



dirs = ""
adddirs = False
part_2_grid = []
part_1_grid = []

f = open("./input.txt", "r")
for line in f.read().splitlines():
    if line == "":
        adddirs = True
        continue
    if adddirs:
        dirs += line
        continue

    newline = ""
    for a in line:
        if a == ".":
            newline += ".."
        if a == "O":
            newline += "[]"
        if a == "@":
            newline += "@."
        if a == "#":
            newline += "##"
    part_2_grid.append([a for a in newline])
    part_1_grid.append([a for a in line])

part_1_grid = np.array(part_1_grid)
part_2_grid = np.array(part_2_grid)

for grid in [part_1_grid, part_2_grid]:
    for dirstr in dirs:
        pos = np.argwhere(grid == "@")[0]
        dir = dirsdict[dirstr]

        try:
            squares_to_push = sorted(
                get_squares_to_push(grid, pos, dirstr),
                key=lambda x: -x[1] if dirstr == ">" else (x[1] if dirstr == "<" else (-x[0] if dirstr == "v" else x[0]))
            )
        except WallError:
            squares_to_push = []

        new_positions = [square + dir for square in squares_to_push]

        for square, new_position in zip(squares_to_push, new_positions):
            grid[new_position[0]][new_position[1]] = grid[square[0]][square[1]]

            if str(square) not in [str(p) for p in new_positions]:
                grid[square[0]][square[1]] = "."


    print(sum(b[0] * 100 + b[1] for b in np.argwhere(np.logical_or(grid == "[",  grid == "O"))))

