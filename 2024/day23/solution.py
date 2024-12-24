from itertools import combinations
import networkx as nx

lines = [set(a.split("-")) for a in open("./input.txt", "r").read().splitlines()]
g = nx.Graph(lines)

cliques = list(nx.find_cliques(g))
maxclique = max(len(c) for c in cliques)
threecliques = set()
for c in cliques:
    if len(c) == maxclique:
        print("Part 2: " + ','.join(sorted(c)))
    for a, b, c in combinations(c, 3):
        if a.startswith("t") or b.startswith("t") or c.startswith("t"):
            threecliques.add(",".join(sorted([a, b, c])))


print("Part 1: " + str(len(threecliques)))
