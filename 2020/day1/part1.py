if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_numbers = [int(num) for num in f.read().splitlines()]
    for i, num1 in enumerate(input_numbers):
        for j, num2 in enumerate(input_numbers[i:]):
            if num1 + num2 == 2020:
                print(num1 * num2)
