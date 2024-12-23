import functools
from itertools import combinations
# import networkx as nx

lines = [set(a.split("-")) for a in open("./input.txt", "r").read().splitlines()]
nodes = functools.reduce(lambda a, b: a | b, lines, set())
print(nodes)
print(lines)
total = 0
trips = []
nodes_list = list(nodes)
for asd, node in enumerate(nodes_list):
    print(asd)
    matching_nodes = [n for n in nodes_list[asd:] if {n, node} in lines]
    for matching_node in matching_nodes:
        qwe = nodes_list.index(matching_node)
        final_nodes = [n for n in nodes_list[qwe:] if {n, matching_node} in lines and n != node]
        for final_node in final_nodes:
            if {final_node, node} in lines:
                total += 1

print(total)

# 11011 too high