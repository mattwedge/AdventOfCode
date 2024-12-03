# 33:00

def check_valid(sequence):
    sorted_seq = sorted(sequence)
    reverse_sorted_seq = sorted_seq[::-1]

    if not (sequence == sorted_seq or sequence == reverse_sorted_seq):
        return False
    
    return all(
        sequence[i+1] - sequence[i] != 0
        and abs(sequence[i+1] - sequence[i]) <= 3
        for i in range(len(sequence) - 1)
    )

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()

    num_safe = sum(check_valid([int(a) for a in line.split()]) for line in input_lines)
    print(f"{num_safe = }")


    num_almost_safe = 0
    for line in input_lines:
        parsed = [int(a) for a in line.split()]
        if any(
            check_valid(parsed[:i] + parsed[i+1:])
            for i in range(len(parsed))
        ):
            num_almost_safe += 1
        
    print(f"{num_almost_safe = }")
