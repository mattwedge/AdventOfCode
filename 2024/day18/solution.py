# 1:41:12

from collections import defaultdict
import re
import sys

sys.setrecursionlimit(10_000)

dirs = [
    1 + 0j,
    -1 + 0j,
    0 + 1j,
    0 - 1j,
]

f = open("./input.txt", "r")
lines = [[int(a) for a in re.findall("\d+", line)] for line in f.read().splitlines()]

num_bytes = 1024
grid_size = 71

blocks = set()
for line in lines[:num_bytes]:
    blocks.add(line[0] + line[1] * 1j)

added = set([1])
while added:
    added.clear()
    for i in range(grid_size):
        for k in range(grid_size):
            pos = i + k * 1j
            if pos not in blocks and len([dir for dir in dirs if pos + dir in blocks]) >= 3:
                blocks.add(i + k * 1j)
                added.add(i + k * 1j)

            if pos not in blocks and (i == 0 or i == grid_size - 1) and k != 0 and k != grid_size - 1 and len([dir for dir in dirs if pos + dir in blocks]) >= 2:
                blocks.add(i + k * 1j)
                added.add(i + k * 1j)

            if pos not in blocks and (k == 0 or k == grid_size - 1) and i != 0 and i != grid_size - 1 and len([dir for dir in dirs if pos + dir in blocks]) >= 2:
                blocks.add(i + k * 1j)
                added.add(i + k * 1j)


min_used_squares = set() # Use this to track the squares used in the shortest solution
while True:
    new_pos = lines[num_bytes][0] + lines[num_bytes][1] * 1j
    if new_pos in blocks:
        num_bytes += 1
        continue

    blocks.add(new_pos)
    if min_used_squares and new_pos not in min_used_squares:
        num_bytes += 1
        continue

    min_used_squares = set()
    position_minima = defaultdict(int)
    explored_scores = set()
    def get_solutions(current_pos: int, current_score: int, target: int):
        pos_score = str(current_pos) + "asdAs" + str(current_score)
        if pos_score in explored_scores:
            return []
        if current_pos in position_minima and position_minima[current_pos] < current_score:
            return []
        
        explored_scores.add(pos_score)

        
        position_minima[current_pos] = current_score
        for dir in dirs:
            offs = 1
            offs_pos = current_pos + offs * dir
            while offs_pos.real >= 0 and offs_pos.real <= grid_size and offs_pos.imag >= 0 and offs_pos.imag <= grid_size and offs_pos not in blocks:
                offs_pos = current_pos + offs * dir
                position_minima[current_pos + offs * dir] = min(position_minima[offs_pos], current_score + offs) if offs_pos in position_minima else current_score + offs
                offs += 1

        if current_pos.real == target.real and current_pos.imag == target.imag:
            return [[]]

        sols = []
        for dir in dirs:
            new_pos = current_pos + dir
            if new_pos.real < 0 or new_pos.real > target.real or new_pos.imag < 0 or new_pos.imag > target.imag:
                continue
            if new_pos in blocks:
                continue
            else:
                sols += [[new_pos, *sol] for sol in get_solutions(new_pos, current_score + 1, target)]

        return sols


    sols = get_solutions(0 + 0j, 0, grid_size - 1 + (grid_size - 1) * 1j)

    if not sols:
        print(",".join(str(a) for a in lines[num_bytes]))
        break

    min_sol_length = min(len(s) for s in sols)
    min_sol_index = [len(s) for s in sols].index(min_sol_length)
    min_sol = sols[min_sol_index]
    min_used_squares = set(min_sol)

    if num_bytes == 1024:
        print(min_sol_length)

    num_bytes += 1
