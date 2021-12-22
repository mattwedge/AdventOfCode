# 40:11

import numpy as np
from collections import Counter

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read().splitlines()

    cipher = input[0].replace(".", "0").replace("#", "1")
    im = np.array([[0 if v == "." else 1 for v in ln] for ln in input[2:]])

    for num_iters in [2, 50]:
        im_copy = np.array(im)
        default_val = 0
        for i in range(num_iters):
            rows, cols = im_copy.shape
            new_im = np.zeros((rows + 2, cols + 2), dtype=int)

            for row in range(-1, rows + 1):
                for col in range(-1, cols + 1):
                    val = []
                    if row <= 0:
                        val += [default_val] * 3 * (1 - row)

                    for sub_row in range(max(0, row - 1), min(rows, row + 2)):
                        if col <= 0:
                            val += [default_val] * (1 - col)

                        val += list(im_copy[sub_row, max(0, col - 1): min(cols, col + 2)])

                        if col >= cols - 1:
                            val += [default_val] * (2 + col - cols)

                    if row >= rows - 1:
                        val += [default_val] * 3 * (2 + row - rows)

                    cipher_index = int("".join(str(a) for a in val), 2)
                    cipher_value = cipher[cipher_index]

                    new_im[row + 1][col + 1] = int(cipher_value)

            if cipher[0] == "1":
                default_val = 1 - default_val

            im_copy = new_im

        print(Counter(new_im.flatten())[1])
