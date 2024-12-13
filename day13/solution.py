# 1:07:40
import math
from typing import Optional
import numpy as np


# Parse the machines from the input
f = open("./input.txt", "r")
input = f.read()
lines = input.splitlines()
machines = []
new_machine = {}
for line in lines:
    if line.startswith("Button A"):
        new_machine = {}
        vals = line.split(": ")[1].split(",")
        new_machine["A"] = [int(val.split("+")[1]) for val in vals]
    if line.startswith("Button B"):
        vals = line.split(": ")[1].split(",")
        new_machine["B"] = [int(val.split("+")[1]) for val in vals]    
    if line.startswith("Prize"):
        vals = line.split(": ")[1].split(",")
        new_machine["P"] = [int(val.split("=")[1]) for val in vals]
    if line == "":
        machines.append(new_machine)

OFFSET = np.array([10000000000000,10000000000000])

def get_to_diag(vecA: np.ndarray, vecB: np.ndarray) -> Optional[list[int]]:
    if vecA[0] < vecA[1] and vecB[0] < vecB[1]:
        return None
    if vecA[0] > vecA[1] and vecB[0] > vecB[1]:
        return None
    
    return (
        [vecB[1] - vecB[0], vecA[0] - vecA[1]]
        if vecB[1] > vecB[0]
        else [vecB[0] - vecB[1], vecA[1] - vecA[0]]
    )

def solve(machine, with_offset=False):
    vector_a = np.array(machine["A"])
    vector_b = np.array(machine["B"])
    prize_vector = np.array(machine["P"])

    current_position = np.array([0,0])
    if with_offset:
        diag_counts = get_to_diag(vector_a, vector_b)
        if diag_counts is None:
            return 0
    
        [numadiag, numbdiag] = diag_counts
        firstdiag = vector_a * numadiag + vector_b * numbdiag

        # Kind of arbitrary choice for how close to get just via the diagonal.
        # We get too low if we don't use the extra `100_000` because we fail to
        # solve some machines which are solvable.
        numdiags = math.floor((OFFSET[0] - 100_000) / firstdiag[0])
        current_position = (numdiags * firstdiag) - OFFSET

    numA = 0
    numB = 0
    while current_position[0] < prize_vector[0] and current_position[1] < prize_vector[1]:
        delta = prize_vector - current_position
        if np.cross(vector_b, delta) == 0: # Are these vectors parallel?
            if (delta[0] / vector_b[0]).is_integer():
                numB = int(delta[0] / vector_b[0])
                return (
                    (numA + (numadiag * numdiags)) * 3 + (numB + (numbdiag * numdiags))
                    if with_offset
                    else numA * 3 + numB
                )

            return 0

        else:
            current_position += vector_a
            numA += 1

    return 0


print(f"Part 1: {sum(solve(machine) for machine in machines)}")
print(f"Part 2: {sum(solve(machine, with_offset=True) for machine in machines)}")
