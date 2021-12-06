# 23:35

import numpy as np
import itertools

def read_input(input_file):
    f = open(input_file, "r")
    input_lines = f.read().splitlines()
    nums = input_lines[0].split(",")
    boards = np.array([ line.strip().replace("  ", " ").split(" ") for line in input_lines[1:] if not line == "" ]).reshape((-1, 5, 5))

    return nums, boards

def part_1():
    nums, boards = read_input("./input.txt")
    MARKER = "-"
    for num in nums:
        boards[boards == num] = MARKER
        for board_number in range(boards.shape[0]):
            for row, column in itertools.product(range(boards.shape[1]), repeat=2):
                if (boards[board_number][row, :] == MARKER).all() or (boards[board_number][:, column] == MARKER).all():
                    return int(num) * sum([int(a) for a in itertools.chain(*boards[board_number]) if not a == MARKER])

def part_2():
    nums, boards = read_input("./input.txt")
    MARKER = "-"
    for num in nums:
        boards_to_delete = set()
        boards[boards == num] = MARKER
        for board_number in range(boards.shape[0]):
            for row, column in itertools.product(range(boards.shape[1]), repeat=2):
                if (boards[board_number][row, :] == MARKER).all() or (boards[board_number][:, column] == MARKER).all():
                    boards_to_delete.add(board_number)
                    break

        if boards.shape[0] == len(boards_to_delete):
            return int(num) * sum([int(a) for a in itertools.chain(*boards[0]) if not a == MARKER])

        boards = np.delete(boards, list(boards_to_delete), 0)               

if __name__ == "__main__":
    print(part_1())
    print(part_2())
