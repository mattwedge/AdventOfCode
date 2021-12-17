# > 3:00:00

import numpy as np

def gt(arr):
    if len(arr) > 2:
        raise Exception("gt")
    return 1 if arr[0] > arr[1] else 0

def lt(arr):
    if len(arr) > 2:
        raise Exception("lt")
    return 1 if arr[0] < arr[1] else 0

def eq(arr):
    if len(arr) > 2:
        raise Exception("eq")
    return 1 if arr[0] == arr[1] else 0

operations = {
    0: sum,
    1: np.product,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq
}

def parse_binary_input(input, max_packets=np.Inf):
    if "1" not in input:
        return [], ""

    if max_packets == 0:
        return [], input

    version_sum = 0
    iter_input = input
    
    version = int(iter_input[:3], 2)
    version_sum += version
    packet_type_id = int(iter_input[3:6], 2)
    if packet_type_id == 4:
        binary_val = ""

        current_index = 6
        prefix = iter_input[current_index]

        binary_val += iter_input[current_index + 1: current_index + 5]
        current_index += 5

        while prefix == "1":
            prefix = iter_input[current_index]
            binary_val += iter_input[current_index + 1: current_index + 5]
            current_index += 5
        
        iter_input = iter_input[current_index:]

        next_packets, remaining_input = parse_binary_input(iter_input, max_packets=max_packets - 1)

        decimal_val = int(binary_val, 2)
        return [decimal_val] + next_packets, remaining_input

    else:
        current_index = 6
        length_type_id = iter_input[current_index]
        if length_type_id == "0":
            subpacket_length = int(iter_input[current_index + 1: current_index + 16], 2)

            next_packets, remaining_input = parse_binary_input(iter_input[current_index + 16 + subpacket_length:], max_packets=max_packets-1)
            return (
                [operations[packet_type_id](parse_binary_input(iter_input[current_index + 16: current_index + 16 + subpacket_length])[0])] +
                next_packets
            ), remaining_input

        else:
            num_subpackets = int(iter_input[current_index + 1: current_index + 12], 2)
            subpacket_vals, remaining_input = parse_binary_input(iter_input[current_index + 12:], max_packets=num_subpackets)

            next_packets, remaining_input_2 = parse_binary_input(remaining_input, max_packets=max_packets-1)
            return [operations[packet_type_id](subpacket_vals)] + next_packets, remaining_input_2

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read()
    bin_input = str(bin(int(input, 16)))[2:]
    if input[0] == "0":
        bin_input = "0000" + bin_input
    while not len(bin_input) % 4 == 0:
        bin_input = "0" + bin_input

    print(parse_binary_input(bin_input)[0][0])