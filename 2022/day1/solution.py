# 6:01

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_numbers = [int(num) if num else None for num in f.read().splitlines()]
    cals_list = []

    new = 0
    for num in input_numbers:
        if not num:
            cals_list.append(new)
            new = 0
        else:
            new += int(num)

    sorted_list = sorted(cals_list)
    print(sorted_list[-1])
    print(sum(sorted_list[-3:]))
