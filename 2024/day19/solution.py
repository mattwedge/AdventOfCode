# 19:48

from functools import lru_cache

f = open("./input.txt", "r")
lines = f.read().splitlines()
pats = lines[0].split(", ")
designs = lines[2:]

@lru_cache
def get_num_sols(design):
    if design == "":
        return 1
    return sum(get_num_sols(design[len(pattern):]) for pattern in pats if design.startswith(pattern))

sols = [get_num_sols(d) for d in designs]
print(len([s for s in sols if s]))
print(sum(s for s in sols))
