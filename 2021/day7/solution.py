# 7:05

if __name__ == "__main__":
    f = open("./input.txt", "r")
    positions = sorted([int(p) for p in f.read().splitlines()[0].split(",")])

    pt1_min = 1e8
    pt2_min = 1e8
    for p in range(positions[-1]):
        pt1_new_sum = sum([abs(pos - p) for pos in positions])
        pt2_new_sum = sum([sum(list(range(abs(pos - p) + 1))) for pos in positions])
        
        if pt1_new_sum < pt1_min:
            pt1_min = pt1_new_sum

        if pt2_new_sum < pt2_min:
            pt2_min = pt2_new_sum

    print(pt1_min)
    print(pt2_min)
