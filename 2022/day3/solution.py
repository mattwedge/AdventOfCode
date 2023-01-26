# 10:11


def priority(val):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(val) + 1


if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()

    print(sum([
        int(priority(list(set(line[:int(len(line) / 2)]).intersection(set(line[int(len(line) / 2):])))[0]))
        for line in input_lines
    ]))

    groups = [input_lines[i: i+3] for i in range(0, len(input_lines), 3)]
    print(sum([
        int(priority(list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]))
        for group in groups
    ]))
