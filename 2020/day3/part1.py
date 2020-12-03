if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_rows = f.read().splitlines()
    pattern_length = len(input_rows[0])
    num_trees_encountered = 0

    for i in range(len(input_rows)):
        if input_rows[i][(i*3) % pattern_length] == "#":
            num_trees_encountered += 1

    print(num_trees_encountered)
