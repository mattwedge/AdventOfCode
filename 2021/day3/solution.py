# 18:04

from collections import Counter

# Returns `default` if equal number of 0s and 1s
def get_most_common(lines, bit_position, default="1"):
    counts = Counter([ln[bit_position] for ln in lines]).most_common()
    if counts[0][1] == counts[1][1]:
        return default
    else:
        return counts[0][0]

def get_least_common(lines, bit_position, default="1"):
    return str(1 - int(get_most_common(lines, bit_position, default=default)))

def part_1():
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()

    num_bits = len(input_lines[0])
    gamma = "".join([get_most_common(input_lines, i) for i in range(num_bits)])
    epsilon = "".join([get_least_common(input_lines, i) for i in range(num_bits)])
    return int(gamma, 2) * int(epsilon, 2)

def part_2():
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()

    ratings = []
    for bit_criteria in [get_most_common, get_least_common]:
        current_lines = [ln for ln in input_lines]
        bit_position = 0
        while len(current_lines) > 1:
            most_common = bit_criteria(current_lines, bit_position)
            current_lines = [ln for ln in current_lines if ln[bit_position] == most_common]
            bit_position += 1

        ratings.append(current_lines[0])

    return int(ratings[0], 2) * int(ratings[1], 2)

if __name__ == "__main__":
    print(part_1())
    print(part_2())
