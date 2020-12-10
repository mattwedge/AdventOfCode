if __name__ == "__main__":
    joltages = [int(j) for j in open("input.txt").read().splitlines()]
    joltages.sort()

    diffs = {}
    last_joltage = 0
    for j in joltages:
        diff = j - last_joltage
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
        last_joltage = j

    print(diffs[1] * (diffs[3] + 1))
