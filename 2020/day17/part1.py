import math
import random
import itertools
import numpy as np

def count_adj(layer_middle, layer_after, layer_before, i, j):
    num_adj = 0
    for ind in itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
        if not ind == (0, 0, 0):
            if ind[2] == -1 and layer_before is not None:
                num_adj += (1 if layer_before[i + ind[0]][j + ind[1]] == "#" else 0)
            elif ind[2] == 1 and layer_after is not None:
                num_adj += (1 if layer_after[i + ind[0]][j + ind[1]] == "#" else 0)
            elif ind[2] == 0:
                num_adj += (1 if layer_middle[i + ind[0]][j + ind[1]] == "#" else 0)

    return num_adj

def calculate_new(layer_middle, layer_after, layer_before):
    new_layer_middle = [layer.copy() for layer in layer_middle]
    for i, row in enumerate(layer_middle):
        for j, col in enumerate(row):
            if i==0 or i==len(layer_middle)-1 or j==0 or j==len(row)-1:
                continue
            adj_count = count_adj(layer_middle, layer_after, layer_before, i, j)
            if layer_middle[i][j] == "#":
                if adj_count in [2, 3]:
                    new_layer_middle[i][j] = "#"
                else:
                    new_layer_middle[i][j] = "."
            elif layer_middle[i][j] == ".":
                if adj_count == 3:
                    new_layer_middle[i][j] = "#"
                else:
                    new_layer_middle[i][j] = "."

    return new_layer_middle

if __name__ == "__main__":
    input_data = (6 * [list("." * 20)] +
                [list("." * 6 + a + "." * 6) for a in
                open("./input.txt", "r").read().splitlines()]
                + 6 * [list("." * 20)])


    # z = (np.stack(*([np.full(input_data.shape, ".")] * 6))
    # + input_data
    # + np.stack(*([np.full(input_data.shape, ".")] * 6)))
    
    # print(z)
    z = {0 : input_data}

    for _ in range(6):
        z_min = min(z.keys())
        z_max = max(z.keys())
        
        z[z_min - 1] = [list("." * 20)] * 20
        z[z_max + 1] = [list("." * 20)] * 20

        new_z = {}
        for layer in z:
            new_z[layer] = calculate_new(z[layer], z.get(layer + 1), z.get(layer - 1))

        z = new_z

    count = 0
    for layer in z.values():
        for row in layer:
            count += row.count("#")

    print(count)
