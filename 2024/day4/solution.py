# ~30:00
import re
import numpy as np

def count_horizontal(grid):
    num = 0
    for line in grid:
        num += len(re.findall("XMAS", "".join(line)))
        num += len(re.findall("SAMX", "".join(line)))

    return num

def count_diagonal(grid):
    num_diag = 0
    grid_length = len(grid.diagonal())
    for grid_init in [grid, np.fliplr(grid)]:
        for i in range(-grid_length, grid_length):
            diag_str = "".join(grid_init.diagonal(offset=i))
            num_diag += len(re.findall("XMAS", diag_str))
            num_diag += len(re.findall("SAMX", diag_str))

    return num_diag

def count_x(grid):
    grid_length = len(grid.diagonal())
    num_x = 0
    for i in range(grid_length):
        for j in range(grid_length):
            subgrid = grid[i-1:i+2, j-1:j+2]
            if "".join(subgrid.diagonal()) in ["MAS", "SAM"]:
                if "".join(np.fliplr(subgrid).diagonal()) in ["MAS", "SAM"]:
                    num_x += 1

    return num_x

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read()
    lines = input.splitlines()
    grid = np.array([[char for char in line] for line in lines])

    num_horizontal = count_horizontal(grid)
    num_vertical = count_horizontal(grid.T)
    num_diag = count_diagonal(grid)

    print(num_diag + num_horizontal + num_vertical)
    print(count_x(grid))
