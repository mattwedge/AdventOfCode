# 1:26:09

import math
from collections import Counter, defaultdict

if __name__ == "__main__":
    f = open("./input.txt", "r")
    lines = [ln  for ln in f.read().splitlines()]
    polymer = lines[0]
    insertions = {ln.split(" -> ")[0]: ln.split(" -> ")[1] for ln in lines if "->" in ln}


    def run_n_iter(n):
        pair_counts = Counter(["".join(pair) for pair in zip(list(polymer), list(polymer)[1:])])
        
        for _ in range(n):
            new_pair_counts = defaultdict(int)
            for insertion in insertions.items():
                new_pair_counts[insertion[0][0] + insertion[1]] += pair_counts[insertion[0]]
                new_pair_counts[insertion[1] + insertion[0][1]] += pair_counts[insertion[0]]

            pair_counts = new_pair_counts

        element_counts = defaultdict(int)

        for k, v in pair_counts.items():
            element_counts[k[0]] +=v
            element_counts[k[1]] +=v

        # The elements are all double-counted except those at the ends which
        # occur an odd number of times (we hope that they are not the same)
        for k, v in element_counts.items():
            element_counts[k] = math.ceil(v / 2)

        return max(element_counts.values()) - min(element_counts.values())

    print(run_n_iter(10))
    print(run_n_iter(40))
