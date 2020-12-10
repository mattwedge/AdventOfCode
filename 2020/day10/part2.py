def count_possibilites(joltages, last_joltage):
    if not joltages:
        return 1

    for i in range(1, len(joltages)):
        if joltages[i] - joltages[i-1] == 3:
            return count_possibilites(joltages[:i], last_joltage) * count_possibilites(joltages[i:], joltages[i-1])

    return_val = 0
    for idx, j in enumerate(joltages):
        if j - last_joltage <= 3:
            return_val += count_possibilites(joltages[idx + 1:], j)
        else:
            break
    return return_val

if __name__ == "__main__":    
    joltages = [int(j) for j in open("input.txt").read().splitlines()]
    joltages.sort()
    joltages.append(joltages[-1] + 3)

    print(count_possibilites(joltages, 0))
