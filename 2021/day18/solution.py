# 2:15:57

import json
import math
import copy
from functools import reduce
from itertools import product

def depth(L): return isinstance(L, list) and max(map(depth, L)) + 1

def get_value_at_index(arr, index):
    try:
        return reduce(lambda v, i: v[i], index, arr)
    except:
        return None

def get_first_nested_pair_index(L, min_depth):
    if depth(L) < min_depth + 1:
        return None

    if min_depth == 0:
        return []

    first = get_first_nested_pair_index(L[0], min_depth - 1)
    if first is not None:
        return [0] + first
    else:
        remaining = get_first_nested_pair_index(L[1:], min_depth)
        remaining[0] += 1
        return remaining

def get_first_over_9_index(L):
    if isinstance(L, int):
        if L < 10:
            return None
        else:
            return []

    first = get_first_over_9_index(L[0])
    if first is not None:
        return [0] + first

    if len(L) > 1:
        remaining = get_first_over_9_index(L[1:])
        if remaining is not None:
            remaining[0] += 1
            return remaining

    return None

def get_prev_index(index, arr):
    for dim, index_value in list(enumerate(index))[::-1]:
        if index_value > 0:
            index_copy = list(index)
            index_copy[dim] = index_value - 1

            while len(index_copy) > dim + 1 and index_copy[-1] == 0:
                del index_copy[-1]

            value_at_new_index = get_value_at_index(arr, index_copy)
            if value_at_new_index is not None:
                while isinstance(get_value_at_index(arr, index_copy), list):
                    index_copy.append(len(get_value_at_index(arr, index_copy)) - 1)

            return index_copy
            
    return None

def get_next_index(index, arr):
    for dim, index_value in list(enumerate(index))[::-1]:
        index_copy = list(index)
        index_copy[dim] = index_value + 1
        for extra_dim  in range(len(index) - 1, dim, -1):
            del index_copy[extra_dim]

        value_at_new_index = get_value_at_index(arr, index_copy)
        if value_at_new_index is not None:
            while isinstance(get_value_at_index(arr, index_copy), list):
                index_copy.append(0)

            return index_copy

    return None

def set_at_index(index, arr, new_val):
    if len(index) == 1:
        arr[index[0]] = new_val
    else:
        arr_to_change = arr[index[0]]
        set_at_index(index[1:], arr_to_change, new_val)

def calculate_magnitude(arr):
    if isinstance(arr, int):
        return arr

    if len(arr) == 2:
        return (3 * calculate_magnitude(arr[0])) + (2 * calculate_magnitude(arr[1]))

def sum_numbers(all_numbers):
    val = copy.deepcopy(all_numbers[0])
    row = 1
    to_add = copy.deepcopy(all_numbers[row])
    val = [val, to_add]

    while True:
        first_pair_index = get_first_nested_pair_index(val, 4)
        if first_pair_index:
            first_pair_val = get_value_at_index(val, first_pair_index)

            prev_index = get_prev_index(first_pair_index, val)
            if prev_index:
                set_at_index(prev_index, val, get_value_at_index(val, prev_index) + first_pair_val[0])

            next_index = get_next_index(first_pair_index, val)
            if next_index:
                set_at_index(next_index, val, get_value_at_index(val, next_index) + first_pair_val[1])

            set_at_index(first_pair_index, val, 0)
            continue

        first_over_9_index = get_first_over_9_index(val)
        if first_over_9_index:
            set_at_index(first_over_9_index, val, [
                math.floor(get_value_at_index(val, first_over_9_index) / 2),
                math.ceil(get_value_at_index(val, first_over_9_index) / 2),
            ])
            continue

        if row >= len(all_numbers) - 1:
            return val

        row += 1
        to_add = copy.deepcopy(all_numbers[row])
        val = [val, to_add]


if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = [json.loads(s) for s in f.read().splitlines()]

    # part 1
    print(calculate_magnitude(sum_numbers(input)))

    # part 2
    print(max(calculate_magnitude(sum_numbers(copy.deepcopy([val_1, val_2]))) for val_1, val_2 in product(input, input)))
