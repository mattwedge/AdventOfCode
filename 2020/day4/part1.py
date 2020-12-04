import re

if __name__ == "__main__":
    f = open("./input.txt", "r")
    pspt_strings = f.read().split("\n\n")
    pspt_lists = [re.split(r"\n|\s", string) for string in pspt_strings]
    pspt_dicts = []
    for pspt_list in pspt_lists:
        new_pspt_dict = {}
        for field in pspt_list:
            field_pair = field.split(":")
            new_pspt_dict[field_pair[0]] = field_pair[1]
        pspt_dicts.append(new_pspt_dict)

    print(len(pspt_dicts))

    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]

    num_valid_passports = 0
    for pspt_dict in pspt_dicts:
        if all([field in pspt_dict for field in required_fields]):
            num_valid_passports += 1

    print(num_valid_passports)
