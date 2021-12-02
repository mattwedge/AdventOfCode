# 5:14

def get_num_increases(arr):
    return len([pair for pair in zip(arr, arr[1:]) if pair[1] > pair[0]])

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_numbers = [int(num) for num in f.read().splitlines()]

    print(get_num_increases(input_numbers)) 
    print(get_num_increases([sum(tup) for tup in zip(input_numbers, input_numbers[1:], input_numbers[2:])]))
    