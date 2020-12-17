import itertools
import numpy as np

def count_adj(vals, coords):
    dim = len(coords)
    num_adj = 0
    for ind in itertools.product([-1, 0, 1], repeat=dim):
        if not ind == (0,)*dim:
            abs_ind = np.array(coords) + np.array(ind)
            num_adj += (1 if vals[tuple(abs_ind)] == "#" else 0)
    return num_adj

def get_new_val(old_val, num_adj):
    if old_val == "#" and num_adj in [2, 3]:
        return "#"
    if old_val == "." and num_adj == 3:
        return "#"
    return "."

def add_padding(arr):
    dims = len(arr.shape)
    return np.pad(
        arr,
        [(1, 1)] * dims,
        "constant",
        constant_values=[(".", ".")] * dims
    )

def solve(start_data, iterations):
    all_values = add_padding(add_padding(start_data))
    for _ in range(iterations):
        new_vals = all_values.copy()

        for coords in np.ndindex(all_values.shape):
            if not (0 in coords) and (not 1 in all_values.shape - np.array(coords)):
                adj_count = count_adj(all_values, coords)
                new_vals[tuple(coords)] = get_new_val(all_values[tuple(coords)], adj_count)

        all_values = add_padding(new_vals)

    return np.count_nonzero(all_values == "#")

if __name__ == "__main__":
    input_data = np.array([list(a) for a in open("./input.txt", "r").read().splitlines()])
    input_data = input_data.reshape((*input_data.shape, 1))

    print(solve(input_data, 6))

    input_data = input_data.reshape((*input_data.shape, 1))
    print(solve(input_data, 6))
