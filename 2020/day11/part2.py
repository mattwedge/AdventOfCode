def check_adjacency(input, row, col):
    if input[row][col] == ".":
        return 0

    adj_seats = []
    for row_diff in range(-1, 2):
        for col_diff in range(-1, 2):
            if not ((row_diff == 0) and (col_diff == 0)):
                for step in range(1, 1000):
                    try:
                        multiplied_row_diff = step * row_diff
                        multiplied_col_diff = step * col_diff
                        if ((row + multiplied_row_diff < 0) or (col + multiplied_col_diff < 0)):
                            break
                        else:
                            if not input[row + multiplied_row_diff][col + multiplied_col_diff] == ".":
                                adj_seats.append(input[row + multiplied_row_diff][col + multiplied_col_diff])
                                break
                    except:
                        break
    if adj_seats.count("#") >= 5:
        return 1
    if adj_seats.count("#") == 0:
        return -1
    return 0

def count_occupied_seats(input):
    num = 0
    for row in input:
        num += row.count("#")
    return num


if __name__ == "__main__":
    input = [list(row) for row in open("input.txt").read().splitlines()]

    stable = False
    while True:
        new_input = [row.copy() for row in input]
        if stable:
            break
        stable = True
        for row in range(len(input)):
            for col in range(len(input[0])):
                if input[row][col] == ".":
                    continue
                adj = check_adjacency(input, row, col)
                if new_input[row][col] == "#" and adj == 1:
                    new_input[row][col] = "L"
                    stable = False
                if new_input[row][col] == "L" and adj == -1:
                    new_input[row][col] = "#"
                    stable = False

        input = new_input

    print(count_occupied_seats(input))
