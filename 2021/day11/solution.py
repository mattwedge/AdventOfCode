# 33:08

import numpy as np

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_matrix = np.array([[int(a) for a in ln] for ln in f.read().splitlines()])
    num_rows, num_cols = input_matrix.shape

    total_num_flashes = 0

    for i in range(1000):
        num_flashes = 0
        input_matrix += 1
        while any(input_matrix[input_matrix > 9]):
            num_flashes += len(input_matrix[input_matrix > 9])
            flash_mask = input_matrix > 9
            input_matrix[flash_mask] = 0
            for row in range(num_rows):
                for col in range(num_cols):
                    if (input_matrix[row][col] <= 9) and not (input_matrix[row][col] == 0):
                        adj = flash_mask[max(0, row - 1): row + 2, max(0, col - 1): col + 2]
                        num_adj_flashers = sum(adj.flatten())
                        input_matrix[row][col] += num_adj_flashers

        total_num_flashes += num_flashes

        # Part 1
        if i == 99:
            print(total_num_flashes)

        # Part 2
        if num_flashes == num_rows * num_cols:
            print(i + 1)
            break
