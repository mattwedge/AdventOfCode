# 19:48

from functools import lru_cache

lines = open("./input.txt", "r").read().splitlines()
pats, designs = lines[0].split(", "), lines[2:]

@lru_cache
def get_num_sols(design):
    return 1 if not design else sum(get_num_sols(design[len(pattern):]) for pattern in pats if design.startswith(pattern))

sols = [get_num_sols(d) for d in designs]
print(len([s for s in sols if s]))
print(sum(s for s in sols))
