from itertools import combinations

if __name__ == "__main__":
    f = open("./input.txt")
    input_numbers = [int(num) for num in f.read().splitlines()]

    for j, num in enumerate(input_numbers):
        if j < 25:
            continue
        got_num = False
        for a, b in combinations(input_numbers[j - 25: j], 2):
            if a + b == num:
                got_num = True
                break
        if not got_num:
            print(num)
            break
