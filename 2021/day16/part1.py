import numpy as np
from collections import defaultdict, Counter

def parse_binary_input(input, max_packets=None):
    num_packets = 0
    version_sum = 0
    iter_input = input
    while "1" in iter_input:
        print(iter_input)
        num_packets += 1
        if (max_packets is not None) and (num_packets > max_packets):
            return version_sum, iter_input
        version = int(iter_input[:3], 2)
        version_sum += version
        packet_type_id = int(iter_input[3:6], 2)
        if packet_type_id == 4:
            print("PACKET TYPE 4")
            current_digit = ""
            current_index = 6
            prefix = iter_input[current_index]

            current_digit += str(int(iter_input[current_index + 1: current_index + 5], 2))
            current_index += 5
            print(current_digit)

            while prefix == "1":
                prefix = iter_input[current_index]
                current_digit += str(int(iter_input[current_index + 1: current_index + 5], 2))
                current_index += 5
                print(current_digit)


            iter_input = iter_input[current_index:]

            # while iter_input[0] == "0":
            #     iter_input = iter_input[1:]
            #     if len(iter_input) == 0:
            #         break

        else:
            current_index = 6
            length_type_id = iter_input[current_index]
            if length_type_id == "0":
                subpacket_length = int(iter_input[current_index + 1: current_index + 16], 2)
                subpacket_version_sum, _ = parse_binary_input(iter_input[current_index + 16: current_index + 16 + subpacket_length])
                version_sum += subpacket_version_sum
                iter_input = iter_input[current_index + 16 + subpacket_length:]
            else:
                num_subpackets = int(iter_input[current_index + 1: current_index + 12], 2)
                subpacket_version_sum, remaining_input = parse_binary_input(iter_input[current_index + 12:], num_subpackets)
                version_sum += subpacket_version_sum
                iter_input = remaining_input
            
        if len(iter_input) == 0:
            break
        # while iter_input[0] == "0":
        #     iter_input = iter_input[1:]
        #     if len(iter_input) == 0:
        #         break

        continue

    return version_sum, ""


if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read()
    bin_input = str(bin(int(input, 16)))[2:]
    if input[0] == "0":
        bin_input = "0000" + bin_input
    while not len(bin_input) % 4 == 0:
        bin_input = "0" + bin_input

    # print(bin_input)
    # print(parse_binary_input(bin_input))
    print(parse_binary_input(bin_input))
    
    # print(parse_binary_input("11101110000000001101010000001100100000100011000001100000"))

    