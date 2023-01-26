# 13:11
wins = ["A Y", "B Z", "C X"]
losses = ["A Z", "B X", "C Y"]
draws = ["A X", "B Y", "C Z"]
score_map = {"X": 1, "Y": 2, "Z": 3}


def calculate_round_score(line):
    p1, p2 = line.split(" ")
    base_score = score_map[p2]
    result_score = 6 if line in wins else (3 if line in draws else 0)
    return base_score + result_score


def calculate_score(lines):
    return sum([calculate_round_score(line) for line in lines])


def parse_part2_line(line):
    p1, p2 = line.split(" ")
    if p2 == "X":
        return [ln for ln in losses if ln[0] == p1][0]
    if p2 == "Y":
        return [ln for ln in draws if ln[0] == p1][0]
    if p2 == "Z":
        return [ln for ln in wins if ln[0] == p1][0]


if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()

    print(calculate_score(input_lines))
    print(calculate_score([parse_part2_line(ln) for ln in input_lines]))
