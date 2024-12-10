# 23:22
import numpy as np

f = open("./input.txt", "r")
input = f.read()

lines = input.splitlines()

grid = np.array([[int(a) for a in line] for line in lines])
trailheads = np.argwhere(grid == 0)


def find_routes(grid: np.ndarray, start_loc: list[int, int]):
    start_val = grid[start_loc[0]][start_loc[1]]

    if start_loc[0] < 0 or start_loc[1] < 0:
        return []

    if start_val == 9:
        return [[start_loc]]

    next_locs = [
        [start_loc[0] + 1, start_loc[1]],
        [start_loc[0] - 1, start_loc[1]],
        [start_loc[0], start_loc[1] + 1],
        [start_loc[0], start_loc[1] - 1],
    ]

    routes = []
    for loc in next_locs:
        if loc[0] < 0 or loc[1] < 0 or loc[0] >= np.shape(grid)[0] or loc[1] >= np.shape(grid)[0]:
            continue
        if grid[loc[0]][loc[1]] == start_val + 1:
            routes += [[start_loc] + route for route in find_routes(grid, loc)]

    return routes

all_routes = []
for trailhead in trailheads:
    all_routes += find_routes(grid, trailhead)


independent_start_end_points = set([str(route[0]) + str(route[-1]) for route in all_routes])
print(len(independent_start_end_points))
print(len(all_routes))
