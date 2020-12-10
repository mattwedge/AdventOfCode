def count_possibilites(joltages, last_joltage):
    if not joltages:
        return 1
    if joltages[0] - last_joltage > 3:
        return 0

    for i in range(1, len(joltages)):
        if joltages[i] - joltages[i-1] == 3:
            return count_possibilites(joltages[:i], last_joltage) * count_possibilites(joltages[i:], joltages[i-1])

    if len(joltages) == 1:
        return count_possibilites(joltages[1:], joltages[0])
    else:
        return count_possibilites(joltages[1:], joltages[0]) + count_possibilites(joltages[1:], last_joltage)


if __name__ == "__main__":    
    joltages = [int(j) for j in open("input.txt").read().splitlines()]
    joltages.sort()
    joltages.append(joltages[-1] + 3)

    print(count_possibilites(joltages, 0))
