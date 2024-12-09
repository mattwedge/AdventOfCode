# 8:34

def calculate_possible_outputs(arr, include_concat=False):
    if len(arr) == 1:
        return arr

    up_to_last = calculate_possible_outputs(arr[:-1], include_concat=include_concat)

    return (
        [s * arr[-1] for s in up_to_last]
        + [s + arr[-1] for s in up_to_last]
        + ([int(str(s) + str(arr[-1])) for s in up_to_last] if include_concat else [])
    )


part_1_total = 0
part_2_total = 0

f = open("./input.txt", "r")
input = f.read()
lines = input.splitlines()
for line in lines:
    line_total, line_operands = line.split(": ")
    line_total = int(line_total)
    line_operands = [int(num) for num in line_operands.split(" ")]

    if line_total in calculate_possible_outputs(line_operands, include_concat=False):
        part_1_total += line_total
    if line_total in calculate_possible_outputs(line_operands, include_concat=True):
        part_2_total += line_total

print(f"{part_1_total = }")
print(f"{part_2_total = }")