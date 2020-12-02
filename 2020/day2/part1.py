if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_strings = f.read().splitlines()
    input_lists = [string.replace(":", "").replace("-", " ").split(" ") for string in input_strings]
    input_dicts = [{
        "min_occurrences": int(l[0]),
        "max_occurrences": int(l[1]),
        "letter": l[2],
        "pwd": l[3],
    } for l in input_lists]

    num_valid = 0
    for d in input_dicts:
        num_occurrences = d["pwd"].count(d["letter"])
        if (num_occurrences <= d["max_occurrences"]) and (num_occurrences >= d["min_occurrences"]):
            num_valid += 1

    print(num_valid)
