import re

def height_check(hgt):
    [val, metric] = hgt[:-2], hgt[-2:]
    if not metric in ["cm", "in"]:
        return False
    if metric == "cm":
        return int(val) >= 150 and int(val) <= 193
    if metric == "in":
        return int(val) >= 59 and int(val) <= 76

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

    validation_checks = {
        "byr": [
            lambda x: len(x) == 4,
            lambda x: int(x) >= 1920 and int(x) <= 2002,
        ],
        "iyr": [
            lambda x: len(x) == 4,
            lambda x: int(x) >= 2010 and int(x) <= 2020,
        ],
        "eyr": [
            lambda x: len(x) == 4,
            lambda x: int(x) >= 2020 and int(x) <= 2030,
        ],
        "hgt": [
            lambda x: height_check(x)
        ],
        "hcl": [
            lambda x: re.match(r"^#[0-9a-f]{6}$", x)
        ],
        "ecl": [
            lambda x: re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", x)
        ],
        "pid": [
            lambda x: re.match(r"^[0-9]{9}$", x)
        ]
    }

    num_valid_passports = 0
    for pspt_dict in pspt_dicts:
        is_valid = True
        for field in validation_checks.keys():
            if not field in pspt_dict.keys():
                is_valid = False
            else:
                val_checks = validation_checks[field]
                if not all([val(pspt_dict[field]) for val in val_checks]):
                    is_valid = False
        if is_valid:
            num_valid_passports += 1

    print(num_valid_passports)
