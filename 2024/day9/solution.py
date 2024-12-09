# 57:20

f = open("./input.txt", "r")
input = f.read()

def expand_digits(arr: list[str]) -> list[int, str]:
    expanded = []
    for i, char in enumerate(arr):
        if not i % 2:
            expanded += [int(i / 2) for _ in list(range(int(char)))]
        else:
            expanded += ["." for _ in list(range(int(char)))]

    return expanded

def sum_from_position(arr: list[int, str]) -> int:
    total = 0
    for i, num in enumerate(arr):
        if num != ".":
            total += i * int(num)
    return total

def part_1(arr: list[int, str]):
    for i in range(len(arr)):
        num = arr[-1 - i]
        first_null = arr.index(".")
        if first_null > len(arr) - 1 - i:
            break

        arr[first_null] = num
        arr[len(arr) - i - 1] = "."

    return sum_from_position(arr)

def part_2(arr: list[int, str]):
    processed_nums = set() # Keep a record of which blocks we've processed
    for file_position in range(len(arr)):
        num = arr[-1-file_position]
        if num == ".":
            continue

        if num in processed_nums:
            continue

        if num == 0:
            break

        processed_nums.add(num)

        file_length = 1
        while arr[-1-file_position-file_length] == num:
            file_length += 1
            if 1 + file_position + file_length >= len(arr):
                break


        for starting_position, file_id in enumerate(arr):
            if starting_position >= len(arr) - file_position:
                break

            if file_id == ".":
                blocked = any(
                    (
                        starting_position + l >= len(arr)
                        or arr[starting_position + l] != "."
                    )
                    for l in range(file_length)
                )

                if blocked:
                    continue

                # Valid placement - move block
                for l in range(file_length):
                    arr[starting_position + l] = num
                    arr[-1 - file_position - l] = "."
                
                break


    return sum_from_position(arr)

        
part_1_total = part_1(expand_digits(list(input)))
print(part_1_total)

part_2_total = part_2(expand_digits(list(input)))
print(part_2_total)