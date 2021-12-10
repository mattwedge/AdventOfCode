# 27:22
from collections import Counter
import numpy as np

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()

    full_pairs = ["()", "[]", "{}", "<>"]
    closers = [")", "]", "}", ">"]

    # Part 1
    illegal_chars = []
    for line in input_lines:
        while any([pair in line for pair in full_pairs]):
            for pair in full_pairs:
                line = line.replace(pair, "")

        illegal_char_indices = [line.index(closer) for closer in closers if closer in line]
        if illegal_char_indices:
            illegal_char_index = min(illegal_char_indices)
            illegal_chars.append(line[min(illegal_char_indices)])

    counts = Counter(illegal_chars)
    print(counts[")"] * 3 + counts["]"] * 57 + counts["}"] * 1197 + counts[">"] * 25137)

    # Part 2
    score_map = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    line_scores = []
    for line in input_lines:
        while any([pair in line for pair in full_pairs]):
            for pair in full_pairs:
                line = line.replace(pair, "")

        if not any(closer in line for closer in closers):
            line_score = 0
            for c in line[::-1]:
                line_score *= 5
                line_score += score_map[c]
            line_scores.append(line_score)

    print(int(np.median(line_scores)))
