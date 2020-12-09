if __name__ == "__main__":
    f = open("./input.txt")
    input_numbers = [int(num) for num in f.read().splitlines()]

    TARGET_NUMBER = 217430975
    for j in range(len(input_numbers)):
        current_sum = 0
        j_curr = j
        got_answer = False
        while current_sum < TARGET_NUMBER:
            current_sum += input_numbers[j_curr]
            if current_sum == TARGET_NUMBER:
                got_answer = True
                print(min(input_numbers[j:j_curr]) + max(input_numbers[j:j_curr]))
                break
            if current_sum > TARGET_NUMBER:
                break
            j_curr += 1
        if got_answer:
            break
