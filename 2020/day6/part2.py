if __name__ == "__main__":
    f = open("./input.txt", "r")
    answer_string_lists = [string.split("\n") for string in f.read().split("\n\n")]
    all_shared_chars = []
    for string_list in answer_string_lists:
        all_shared_chars.append(
            [char for char in string_list[0] if all([char in string for string in string_list])]
        )

    sum_shared_chars = sum(len(chars) for chars in all_shared_chars)
    print(sum_shared_chars)
