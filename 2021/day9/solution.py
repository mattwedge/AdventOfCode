# 39:00

from collections import Counter
import numpy as np
from scipy.ndimage.measurements import label

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_matrix = np.array([[int(a) for a in list(ln)] for ln in f.read().splitlines()])


    # Part 1
    comparison_matrices = [
        np.concatenate((input_matrix[:, 1:], np.ones((100, 1)) * np.inf), axis=1),
        np.concatenate((np.ones((100, 1)) * np.inf, input_matrix[:, :-1]), axis=1),
        np.concatenate((input_matrix[1:, :], np.ones((1, 100)) * np.inf), axis=0),
        np.concatenate((np.ones((1, 100)) * np.inf, input_matrix[:-1, :]), axis=0),
    ]
    
    danger_points = input_matrix[
        (input_matrix < comparison_matrices[0]) &
        (input_matrix < comparison_matrices[1]) &
        (input_matrix < comparison_matrices[2]) &
        (input_matrix < comparison_matrices[3])
    ]
    print(sum(danger_points) + len(danger_points))


    # Part 2
    structure = np.array([
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ])

    labeled, ncomponents = label((9 - input_matrix), structure)
    label_counts = Counter(list(labeled.flatten()))
    del label_counts[0]

    print(np.prod([a[1] for a in label_counts.most_common(3)]))
