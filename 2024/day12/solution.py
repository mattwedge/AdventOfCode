# 1:17:22

from collections import defaultdict
import json
import numpy as np

f = open("./input.txt", "r")
input = f.read()
lines = input.splitlines()
grid = np.array([[a for a in line] for line in lines], dtype="str")


def get_perimeter(grid, plant):
    plant_locations = np.argwhere(grid == plant)
    perimeter = 0

    for loc in plant_locations:
        if loc[0] == 0 or grid[loc[0] - 1, loc[1]] != plant:
            perimeter += 1
        if loc[0] == np.shape(grid)[0] - 1 or grid[loc[0] + 1, loc[1]] != plant:
            perimeter += 1
        if loc[1] == 0 or grid[loc[0], loc[1] - 1] != plant:
            perimeter += 1
        if loc[1] == np.shape(grid)[1] - 1 or grid[loc[0], loc[1] + 1] != plant:
            perimeter += 1
    return perimeter

def get_num_sides(grid, plant):
    plant_locations = np.argwhere(grid == plant)
    
    current_sides = set()
    
    num_sides = 0
    for loc in plant_locations:
        if loc[0] == 0 or grid[loc[0] - 1, loc[1]] != plant:
            if (
                not str([loc[0], loc[1] + 1]) + "<" in current_sides
                and not str([loc[0], loc[1] + -1]) + "<" in current_sides
            ):
                num_sides += 1

            current_sides.add(str([loc[0], loc[1]]) + "<")

        if loc[0] == np.shape(grid)[0] - 1 or grid[loc[0] + 1, loc[1]] != plant:
            if (
                not str([loc[0], loc[1] + 1]) + ">" in current_sides
                and not str([loc[0], loc[1] + -1]) + ">" in current_sides
            ):
                num_sides += 1

            current_sides.add(str([loc[0], loc[1]]) + ">")

        if loc[1] == 0 or grid[loc[0], loc[1] - 1] != plant:
            if (
                not str([loc[0] + 1, loc[1]]) + "^" in current_sides
                and not str([loc[0] - 1, loc[1]]) + "^" in current_sides
            ):
                num_sides += 1

            current_sides.add(str([loc[0], loc[1]]) + "^")
    
        if loc[1] == np.shape(grid)[1] - 1 or grid[loc[0], loc[1] + 1] != plant:
            if (
                not str([loc[0] + 1, loc[1]]) + "V" in current_sides
                and not str([loc[0] - 1, loc[1]]) + "V" in current_sides
            ):
                num_sides += 1

            current_sides.add(str([loc[0], loc[1]]) + "V")

    return num_sides

def get_contiguous_regions(grid: np.ndarray):
    current_regions = defaultdict(list)
    for i in range(np.shape(grid)[0]):
        for j in range(np.shape(grid)[1]):
            current_loc = [i, j]
            plant = grid[current_loc[0], current_loc[1]]
            plant_regions = current_regions[plant]
            if not plant_regions:
                plant_regions.append([current_loc])
            else:
                found_region = False
                for region in plant_regions:
                    for p in region:
                        if np.linalg.norm(p - np.array(current_loc)) == 1:
                            if not current_loc in region:
                                found_region = True
                                region.append(current_loc)


                if not found_region:
                    plant_regions.append([current_loc])

    deduped_regions = defaultdict(list)
    for plant in current_regions:
        plant_regions = current_regions[plant]
        region_sets = [set([str(p) for p in region]) for region in plant_regions]
        for region_set_a in region_sets:
            for region_set_b in region_sets:
                if region_set_a != region_set_b:
                    if region_set_a & region_set_b:
                        for b in region_set_b:
                            region_set_a.add(b)
                        
                        region_set_b.clear()

        for region_set in region_sets:
            if region_set:
                deduped_regions[plant].append([json.loads(p) for p in region_set])


    return deduped_regions


crs = get_contiguous_regions(grid)


all_crs = []
for plant in crs:
    all_crs += crs[plant]


new_grid = np.empty(shape=np.shape(grid))
for i, cr in enumerate(all_crs):
    for p in cr:
        new_grid[p[0], p[1]] = i


plants = set(new_grid.flatten())
total_cost_part1 = 0
total_cost_part2 = 0
for plant in plants:
    total_cost_part1 += get_perimeter(new_grid, plant) * len([p for p in new_grid.flatten() if p == plant])
    total_cost_part2 += get_num_sides(new_grid, plant) * len([p for p in new_grid.flatten() if p == plant])

print(total_cost_part1)
print(total_cost_part2)


