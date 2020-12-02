if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_strings = f.read().splitlines()
    input_lists = [string.replace(":", "").replace("-", " ").split(" ") for string in input_strings]
    input_dicts = [{
        "first_occurrence": int(l[0]),
        "second_occurrence": int(l[1]),
        "letter": l[2],
        "pwd": l[3],
    } for l in input_lists]

    num_valid = 0
    for d in input_dicts:
        is_valid = not (d["pwd"][d["first_occurrence"] - 1] == d["letter"]) == (d["pwd"][d["second_occurrence"] - 1] == d["letter"])
        if is_valid:
            num_valid += 1

    print(num_valid)
