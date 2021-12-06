# 35:17

def get_covered_points(vent, include_diagonals=False):
    if vent[0][0] == vent[1][0]:
        return set([(vent[0][0], y) for y in range(min(vent[0][1], vent[1][1]), max(vent[0][1], vent[1][1]) + 1)])
    elif vent[0][1] == vent[1][1]:
        return set([(x, vent[0][1]) for x in range(min(vent[0][0], vent[1][0]), max(vent[0][0], vent[1][0]) + 1)])
    else:
        if include_diagonals:
            x_range = list(range(min(vent[0][0], vent[1][0]), max(vent[0][0], vent[1][0]) + 1))
            y_range = list(range(min(vent[0][1], vent[1][1]), max(vent[0][1], vent[1][1]) + 1))

            if ((vent[0][0] < vent[1][0]) and (vent[0][1] < vent[1][1])) or ((vent[0][0] > vent[1][0]) and (vent[0][1] > vent[1][1])):
                return set(zip(x_range, y_range))
            else:
                return set(zip(x_range, y_range[::-1]))
        else:
            return set()

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()
    vents = [[tuple([int(coord) for coord in pt.split(",")]) for pt in ln.split(" -> ")] for ln in input_lines]

    for include_diagonals in [False, True]:
        any_covered = set()
        double_covered = set()
        for vent in vents:
            vent_points = get_covered_points(vent, include_diagonals=include_diagonals)
            double_covered = double_covered.union(vent_points.intersection(any_covered))
            any_covered = any_covered.union(vent_points)

        print(len(double_covered))
