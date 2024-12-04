# 12:08

import re
import numpy as np

def count_horizontal(grid):
    num = 0
    for line in grid:
        num += len(re.findall("XMAS", "".join(line)))
        num += len(re.findall("SAMX", "".join(line)))

    return num

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read()
    lines = input.splitlines()
    grid = np.array([[char for char in line] for line in lines])
    num_horizontal = count_horizontal(grid)

    num_vertical = count_horizontal(grid.T)

    num_diag = 0

    for grid_init in [grid, np.fliplr(grid)]:
        main_diag = grid_init.diagonal()
        diag_str = "".join(main_diag)
        num_diag += len(re.findall("XMAS", diag_str))
        num_diag += len(re.findall("SAMX", diag_str))
    
    l = len(grid.diagonal())
    for grid_init in [grid, np.fliplr(grid)]:
        for i in range(1, l-1):
            subgrid = grid_init[i:,:l-i]
            diag_str = "".join(subgrid.diagonal())
            num_diag += len(re.findall("XMAS", diag_str))
            num_diag += len(re.findall("SAMX", diag_str))


            subgrid = grid_init[:l-i,i:]
            diag_str = "".join(subgrid.diagonal())
            num_diag += len(re.findall("XMAS", diag_str))
            num_diag += len(re.findall("SAMX", diag_str))


    print(f"{num_diag = }")
    print(f"{num_horizontal = }")
    print(f"{num_vertical = }")
    print(num_diag + num_horizontal + num_vertical)