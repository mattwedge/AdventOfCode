def parse_seat(binary_val):
    binary_row = binary_val[:7]
    binary_col = binary_val[7:]

    numeric_row = 0
    for i, bit in enumerate(binary_row[::-1]):
        numeric_row += (2 ** i) if bit == "B" else 0

    numeric_col = 0
    for i, bit in enumerate(binary_col[::-1]):
        numeric_col += (2 ** i) if bit == "R" else 0

    return numeric_row, numeric_col, (numeric_row * 8) + numeric_col

if __name__ == "__main__":
    f = open("./input.txt", "r")
    seat_vals = f.read().splitlines()
    all_seat_ids = [parse_seat(val)[2] for val in seat_vals]
    all_seat_ids.sort()
    for i, seat_id in enumerate(all_seat_ids):
        if all_seat_ids[i+1] != seat_id + 1:
            print(seat_id + 1)
            break
