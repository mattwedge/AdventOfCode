# 19:55

import numpy as np

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_matrix = np.array([list(ln) for ln in f.read().splitlines()])
    rows, cols = input_matrix.shape

    iteration = 0
    while True:
        iteration += 1
        prev_input = np.array(input_matrix)
        horiz = input_matrix == ">"
        horiz_can_move = np.roll(input_matrix, -1, axis=1) == "."
        input_matrix[horiz & horiz_can_move] = "."
        input_matrix[np.roll(horiz & horiz_can_move, 1, axis=1)] = ">"

        vert = input_matrix == "v"
        vert_can_move = np.roll(input_matrix, -1, axis=0) == "."
        input_matrix[vert & vert_can_move] = "."
        input_matrix[np.roll(vert & vert_can_move, 1, axis=0)] = "v"

        if (prev_input == input_matrix).all():
            break

    print(iteration)
