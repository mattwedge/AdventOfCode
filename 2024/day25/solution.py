from collections import Counter


keys = []
locks = []

lines = open("./input.txt", "r").read().splitlines()

addingkey = False
addinglock = False
vals = Counter()
for line in lines:
    if not addingkey and not addinglock:
        addingkey = line == "....."
        addinglock = not addingkey
    for i, v in enumerate(line):
        if v == "#":
            vals[i] += 1
    if line == "":
        if addingkey:
            keys.append(vals)
        else:
            locks.append(vals)

        vals = Counter()
        addinglock = False
        addingkey = False

matches = 0
for key in keys:
    for lock in locks:
        if max((key + lock).values()) <= 7:
            matches += 1

print(matches)