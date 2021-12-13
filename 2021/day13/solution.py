# 29:25

import numpy as np

def calculate_positions(dots, folds):
    if not folds:
        return dots

    shifted_dots = [dot for dot in dots]

    fold = folds[0]
    if fold[0] == "x":
        for dot in shifted_dots:
            if dot[0] > fold[1]:
                dot[0] = fold[1] - (dot[0] - fold[1])

    if fold[0] == "y":
        for dot in shifted_dots:
            if dot[1] > fold[1]:
                dot[1] = fold[1] - (dot[1] - fold[1])

    return calculate_positions(shifted_dots, folds[1:])


if __name__ == "__main__":
    f = open("./input.txt", "r")
    lines = [ln  for ln in f.read().splitlines()]
    dots = [ln.split(",") for ln in lines if "," in ln]
    for d in dots:
        d[0] = int(d[0])
        d[1] = int(d[1])

    folds = [ln.split("fold along ")[1].split("=") for ln in lines if "fold along" in ln]
    for f in folds:
        f[1] = int(f[1])
    
    # Part 1
    new_dots = calculate_positions(dots, folds[:1])
    print(len(set([",".join([str(p) for p in dot]) for dot in new_dots])))

    # Part 2
    final_dots = calculate_positions(dots, folds)
    
    min_x = min(*[dot[0] for dot in final_dots])
    min_y =  min(*[dot[1] for dot in final_dots])
    max_x = max(*[dot[0] for dot in final_dots])
    max_y = max(*[dot[1] for dot in final_dots])
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    res = np.zeros((width, height))
    for dot in final_dots:
        res[dot[0], dot[1]] = 1

    print(np.where(res==0, ".", "#")[:, ::-1])
