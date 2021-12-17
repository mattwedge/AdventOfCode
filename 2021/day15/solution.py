# > 3:00:00

import numpy as np

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = np.array([[int(n) for n in ln]  for ln in f.read().splitlines()])

    def calculate_min_risk(arr):
        input_shape = arr.shape
        arrival_maxima = np.zeros(input_shape)

        for diagonal in range(2, (2 * input_shape[0])):
            row_range = range(max(0, diagonal - input_shape[0]), min(input_shape[0], diagonal))
            for row in row_range:
                col = diagonal - row - 1
                prev_diag_vals = []
                if row > 0:
                    prev_diag_vals.append(arrival_maxima[row - 1, col])
                if col > 0:
                    prev_diag_vals.append(arrival_maxima[row, col - 1])
                arrival_maxima[row, col] = arr[row, col] + min(prev_diag_vals)

        while (
            (arrival_maxima[:-1, :] > arrival_maxima[1:, :] + arr[:-1, :]).any() or
            (arrival_maxima[:, :-1] > arrival_maxima[:, 1:] + arr[:, :-1]).any() or
            (arrival_maxima[1:, :] > arrival_maxima[:-1, :] + arr[1:, :]).any() or
            (arrival_maxima[:, 1:] > arrival_maxima[:, :-1] + arr[:, 1:]).any()
        ):
            arrival_maxima[:-1, :][arrival_maxima[:-1, :] > arrival_maxima[1:, :] + arr[:-1, :]] = \
                    (arrival_maxima[1:, :] + arr[:-1, :])[arrival_maxima[:-1, :] > arrival_maxima[1:, :] + arr[:-1, :]]

            arrival_maxima[:, :-1][arrival_maxima[:, :-1] > arrival_maxima[:, 1:] + arr[:, :-1]] = \
                    (arrival_maxima[:, 1:] + arr[:, :-1])[arrival_maxima[:, :-1] > arrival_maxima[:, 1:] + arr[:, :-1]]

            arrival_maxima[1:, :][arrival_maxima[1:, :] > arrival_maxima[:-1, :] + arr[1:, :]] = \
                    (arrival_maxima[:-1, :] + arr[1:, :])[arrival_maxima[1:, :] > arrival_maxima[:-1, :] + arr[1:, :]]

            arrival_maxima[:, 1:][arrival_maxima[:, 1:] > arrival_maxima[:, :-1] + arr[:, 1:]] = \
                    (arrival_maxima[:, :-1] + arr[:, 1:])[arrival_maxima[:, 1:] > arrival_maxima[:, :-1] + arr[:, 1:]]

        return int(arrival_maxima[-1, -1])

    print(calculate_min_risk(input))


    new_input = np.array(input)
    input_copy = np.array(input)
    for i in range(1, 5):
        input_copy = ((input_copy % 9) + 1)
        new_input = np.concatenate((new_input, input_copy), axis = 0)

    new_new_input = np.array(new_input)
    new_input_copy = np.array(new_input)
    for i in range(1, 5):
        new_input_copy = ((new_input_copy % 9) + 1)
        new_new_input = np.concatenate((new_new_input, new_input_copy), axis = 1)

    print(calculate_min_risk(new_new_input))