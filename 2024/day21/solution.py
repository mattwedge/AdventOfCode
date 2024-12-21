from collections import Counter
import re

lines = open("./input.txt", "r").read().splitlines()


charpositions = {
    "A": 0 + 0j,
    "0": 1 + 0j,
    "1": 2 + 1j,
    "2": 1 + 1j,
    "3": 0 + 1j,
    "4": 2 + 2j,
    "5": 1 + 2j,
    "6": 0 + 2j,
    "7": 2 + 3j,
    "8": 1 + 3j,
    "9": 0 + 3j,
}

dirpositions = {
    ">": 0 + 0j,
    "v": 1 + 0j,
    "<": 2 + 0j,
    "A": 0 + 1j,
    "^": 1 + 1j,
}

dirmovements = {
    "<": 1,
    ">": -1,
    "^": 1j,
    "v": -1j,
    "A": 0,
}

def is_valid_movement(dirs, currpos, dir_pad=False):
    posnow = currpos
    for dir in dirs:
        posnow += dirmovements[dir]
        if posnow == (2 + 1j if dir_pad else 2):
            return False

    return True

def get_directions_for_num_char(char, currpos):
    charposition = charpositions[char]
    yoffs = int((charposition - currpos).imag)
    xoffs = int((charposition - currpos).real)

    xdir = "<" if xoffs >= 0 else ">"
    ydir = "^" if yoffs >= 0 else "v"

    directions_list =  list(set([xdir * abs(xoffs) + ydir * abs(yoffs) + "A", ydir * abs(yoffs) + xdir * abs(xoffs) + "A"]))
    directions_list = [directions for directions in directions_list if is_valid_movement(directions, currpos)]

    if len(directions_list) == 1:
        return directions_list[0]


    if "<^^^A" in directions_list:
        return "<^^^A"

    if "vv>A" in directions_list:
        return "vv>A"

    if "^^>A" in directions_list:
        return "^^>A"

    if "<^A" in directions_list:
        return "<^A"

    if "<^^A" in directions_list:
        return "<^^A"


def get_dirs_for_dir_char(char, currpos):
    dirposition = dirpositions[char]
    yoffs = int((dirposition - currpos).imag)
    xoffs = int((dirposition - currpos).real)

    xdir = "<" if xoffs >= 0 else ">"
    ydir = "^" if yoffs >= 0 else "v"

    directions_list = list(set([xdir * abs(xoffs) + ydir * abs(yoffs) + "A", ydir * abs(yoffs) + xdir * abs(xoffs) + "A"]))
    directions_list = [directions for directions in directions_list if is_valid_movement(directions, currpos, dir_pad=True)]

    if "<vA" in directions_list:
        directions_list = ["<vA"]

    if "^>A" in directions_list:
        directions_list = ["^>A"]

    if "<^A" in directions_list:
        directions_list = ["<^A"]

    if "v>A" in directions_list:
        directions_list = ["v>A"]

    return directions_list[0]

def get_dirs_for_num_code(code, currpos):
    posnow = currpos
    dirs = ""
    for char in code:
        chardir = get_directions_for_num_char(char, posnow)
        dirs += chardir
        posnow = charpositions[char]

    return dirs

def get_dirs_for_dir_code(code):
    posnow = dirpositions["A"]
    dirs = ""
    for char in code:
        chardir = get_dirs_for_dir_char(char, posnow)
        dirs += chardir
        posnow = dirpositions[char]

    return dirs


def get_length(motif_counts: Counter):
    total_length = 0
    for motif, motif_count in motif_counts.items():
        total_length += len(motif) * motif_count
    return total_length


def get_motif_downstream_counts(motif) -> Counter:
    motif_sol = get_dirs_for_dir_code(motif)
    return Counter([d + "A" for d in motif_sol.split("A")][:-1])


def get_sol_counts_for_motif_counts(motif_counts: Counter):
    sol_counts = Counter()
    for motif, motif_count in motif_counts.items():
        motif_downstream_counts = get_motif_downstream_counts(motif)
        for k, v in motif_downstream_counts.items():
            sol_counts[k] += v * motif_count

    return sol_counts

for num_bots in [2, 25]:
    total = 0
    for code in lines:
        dircode = get_dirs_for_num_code(code, charpositions["A"])
        motif_counts = Counter([d + "A" for d in dircode.split("A")][:-1])
        for i in range(num_bots):
            motif_counts = get_sol_counts_for_motif_counts(motif_counts)
        
        sol_length = get_length(motif_counts)
        total += sol_length * int(re.findall("\d+", code)[0])

    print(total)
