# 1:07:40
import numpy as np
import re

# Parse the machines from the input
f = open("./input.txt", "r")
input = f.read()

machines = []
machines_text = input.split("\n\n")
machines = [[int(n) for n in re.findall("\d+", text)] for text in machines_text]

OFFSET = np.array([10000000000000,10000000000000])

def solve(machine, with_offset=False):
    target = np.array([machine[4], machine[5]]) + OFFSET if with_offset else np.array([machine[4], machine[5]])
    num_a, num_b = np.linalg.inv(np.array([[machine[0], machine[2]], [machine[1], machine[3]]])).dot(target)
    
    # Ignore rounding errors
    if round(num_a, 3).is_integer() and round(num_b, 3).is_integer():
        return round(num_b + (3 * num_a))
    return 0

print(f"Part 1: {sum(solve(machine) for machine in machines)}")
print(f"Part 2: {sum(solve(machine, with_offset=True) for machine in machines)}")
