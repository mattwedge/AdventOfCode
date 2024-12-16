# 1:06:19

from collections import defaultdict
from typing import Counter
import numpy as np
import sys

sys.setrecursionlimit(10_000)

f = open("./input.txt", "r")
grid = []
for line in f.read().splitlines():
    grid.append([a for a in line])

grid = np.array(grid)


position_minima = defaultdict(int)
dirs = [
    1 + 0j,
    -1 + 0j,
    0 + 1j,
    0 - 1j,
]
def get_solutions(g: np.ndarray, current_pos: int, current_dir, current_score: int):
    if current_pos in position_minima and position_minima[current_pos] < current_score - 1000:
        return []
    
    position_minima[current_pos] = current_score

    if g[int(current_pos.real)][int(current_pos.imag)] == "E":
        return [[]]

    sols = []
    for dir in dirs:
        new_pos = current_pos + dir
        if g[int(new_pos.real)][int(new_pos.imag)] == "#":
            continue
        if dir + current_dir == 0:
            sols += [[1, 1, 0, *sol] for sol in get_solutions(g, new_pos, dir, current_score + 2000 + 1)]
        elif dir == current_dir:
            sols += [[0, *sol] for sol in get_solutions(g, new_pos, dir, current_score + 1)]
        elif dir == current_dir * 1j:
            sols += [[1, 0, *sol] for sol in get_solutions(g, new_pos, dir, current_score + 1000 + 1)]
        else:
            sols += [[-1, 0, *sol] for sol in get_solutions(g, new_pos, dir, current_score + 1000 + 1)]

    return sols

def score_sol(sol: list[int]):
    counts = Counter(sol)
    return 1000  * (counts[1] + counts[-1]) + counts[0]

visited = set()
current_dir = 0 + 1j
possible_paths = []
pos_arr = np.argwhere(grid=="S")[0]
pos = pos_arr[0] + pos_arr[1] * 1j

sols = get_solutions(grid, pos, current_dir, 0)
scores = [score_sol(sol) for sol in sols]
min_score = min(scores)
minargs = []
for i, score in enumerate(scores):
    if score == min_score:
        minargs.append(i)

sqs = set()
for a in minargs:
    sol = sols[a]
    pos_arr = np.argwhere(grid=="S")[0]
    curr = pos_arr[0] + pos_arr[1] * 1j
    current_dir = 0 + 1j
    sqs.add(curr)
    for m in sol:
        if m == 1:
            current_dir *= 1j
        elif m == -1:
            current_dir *= -1j
        else:
            curr += current_dir
            sqs.add(curr)

print(min_score)
print(len(sqs))
