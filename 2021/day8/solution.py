# 39:33

from collections import defaultdict

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = [[s.split(" ") for s in l.split(" | ") ] for l in f.read().splitlines()]
    
    # Part 1
    print(sum(len([d for d in b if len(d) in [2, 4, 3, 7]]) for [_, b] in input_lines))

    # Part 2
    example_mapping = {
        0: "cagedb",
        1: "ab",
        2: "gcdfa",
        3: "fbcad",
        4: "eafb",
        5: "cdfbe",
        6: "cdfgeb",
        7: "dab",
        8: "acedgfb",
        9: "cefabd",
    }


    total = 0
    for line in input_lines:
        patterns = line[0]
        output = line[1]
        known_digits = defaultdict(str)

        known_digits[1] = [a for a in patterns if len(a) == 2][0]
        known_digits[4] = [a for a in patterns if len(a) == 4][0]
        known_digits[7] = [a for a in patterns if len(a) == 3][0]
        known_digits[8] = [a for a in patterns if len(a) == 7][0]

        remaining_patterns = [a for a in patterns if not a in known_digits.values()]

        for unknown_digit in set(range(10)).symmetric_difference(known_digits.keys()):
            possible_patterns = [pattern for pattern in remaining_patterns]
            for known_digit in known_digits:
                expected_intersects = len(set(example_mapping[known_digit]).intersection(example_mapping[unknown_digit]))
                possible_patterns = [
                    pattern for pattern in possible_patterns if
                    sum(char in pattern for char in known_digits[known_digit]) == expected_intersects
                ]
                
            if len(possible_patterns) == 1:
                known_digits[unknown_digit] = possible_patterns[0]
            else:
                raise Exception("Couldn't uniquely identify digit")


        parsed_output = [[k for k, v in known_digits.items() if (len(v) == len(d) and (all([a in d for a in v])))][0] for d in output]
        total += int("".join([str(a) for a in parsed_output]))

    print(total)