# > 1:00:00

import numpy as np

def is_lower(str):
    return all(a.lower() == a for a in str)

def paths_from_to(src, dst, lines, visit_counts, pt2=False):
    if src == dst:
        return [[src]]

    initial_lines = [ln for ln in lines if src in ln]
    if not initial_lines:
        return []

    res = []
    for ln in initial_lines:
        new_src = [p for p in ln if not p == src][0]
        visit_counts_copy = {k: v for k,v in visit_counts.items()}
        visit_counts_copy[src] += 1
        new_permitted_lines = lines
        if src in ["start", "end"]:
            new_permitted_lines = [ln for ln in new_permitted_lines if not src in ln]
        elif is_lower(src):
            if pt2:
                if any(visit_counts_copy[p] == 2 for p in [a for a in visit_counts_copy if is_lower(a)]):
                    new_permitted_lines = lines
                    for p in visit_counts_copy:
                        if is_lower(p) and visit_counts_copy[p] > 0 and not (src in ["start", "end"]):
                            new_permitted_lines = [ln for ln in new_permitted_lines if not p in ln]
            else:
                new_permitted_lines = [ln for ln in new_permitted_lines if not src in ln]

        res += [([src] + path) for path in paths_from_to(new_src, dst, new_permitted_lines, visit_counts_copy, pt2=pt2)]

    return res


if __name__ == "__main__":
    f = open("./input.txt", "r")
    lines = [ln.split("-") for ln in f.read().splitlines()]
    visit_counts = { a: 0  for a in set(np.array(lines).flatten())}

    print(len(paths_from_to("start", "end", lines, visit_counts)))
    print(len(paths_from_to("start", "end", lines, visit_counts, pt2=True)))
