# 28:09

lines = open("./input.txt", "r").read().splitlines()
dirs = { 1, 1j, -1, -1j }
racetrack = { a + (b * 1j) for (b, line) in enumerate(lines) for (a, val) in enumerate(line) if val in ["S", ".", "E"] }
start = [r for r in racetrack if lines[int(r.imag)][int(r.real)] == "S"][0]
end = [r for r in racetrack if lines[int(r.imag)][int(r.real)] == "E"][0]

order = [start]
while len(order) < len(racetrack):
    for pos in [order[-1] + dir for dir in dirs]:
        if pos in racetrack and pos not in order:
            order.append(pos)
            break

min_saving = 100
for max_cheat_length in (2, 20):
    cheat_counts = []
    for r1 in order:
        for r2 in set(order[order.index(r1) + min_saving:]) & {r for r in racetrack if abs((r1 - r).real) + abs((r1 - r).imag) <= max_cheat_length}:
            cheat_length = abs((r1 - r2).real) + abs((r1 - r2).imag)
            cheat_counts.append(order.index(r2) - order.index(r1) - cheat_length)

    print(len([a for a in cheat_counts if a >= min_saving]))
