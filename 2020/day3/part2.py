def count_trees_on_slope(input_rows, right_slope, down_slope):
    pattern_length = len(input_rows[0])

    num_trees_encountered = 0
    ### for every i down, go j to the right 
    for j, i in enumerate(list(range(len(input_rows))[::down_slope])):
        if input_rows[i][(j*right_slope) % pattern_length] == "#":
            num_trees_encountered += 1

    return num_trees_encountered

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_rows = f.read().splitlines()

    prod = 1
    for right_down_pair in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        prod *= count_trees_on_slope(input_rows, right_down_pair[0], right_down_pair[1])

    print(prod)
