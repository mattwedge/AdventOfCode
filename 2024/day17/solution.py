from collections import defaultdict
import math
import re


f = open("./input.txt", "r")
grid = []
gettingprog = False
prog = ""
registers = []
for line in f.read().splitlines():
    if line == "":
        gettingprog = True
    if gettingprog:
        prog = [int(a) for a in re.findall("\d+", line)]
    else:
        registers.append(int(re.findall("\d+", line)[0]))

def combo(operand):
    if operand < 4:
        return operand
    if operand == 4:
        return registers[0]
    if operand == 5:
        return registers[1]
    if operand == 6:
        return registers[2]
    
    raise Exception("UNKNOWN")
        

pointer = 0
outputs = []
outnum = 0 
while True:
    if pointer + 1 > len(prog) - 1:
        break
    val = prog[pointer]
    operand = prog[pointer + 1]

    if val == 0:
        registers[0] = math.floor(registers[0] / (2 ** combo(operand)))
    if val == 1:
        registers[1] = registers[1] ^ operand
    if val == 2:
        registers[1] = combo(operand) % 8
    if val == 3:
        if registers[0] != 0:
            pointer = operand
            continue
    if val == 4:
        registers[1] = registers[1] ^ registers[2]
    if val == 5:
        newout = combo(operand) % 8
        outputs.append(newout)
        outnum += 1
    if val == 6:
        registers[1] = math.floor(registers[0] / (2 ** combo(operand)))
    if val == 7:
        registers[2] = math.floor(registers[0] / (2 ** combo(operand)))

    pointer += 2

print(",".join(str(a) for a in outputs))



sols = defaultdict(list)
for outval in range(8):
    for ainit in range (2 ** 10):
        pointer = 0
        outputs = []
        registers = [ainit, 0, 0]
        match = True
        outnum = 0 
        while True:
            val = prog[pointer]
            operand = prog[pointer + 1]

            if val == 0:
                registers[0] = math.floor(registers[0] / (2 ** combo(operand)))
            if val == 1:
                registers[1] = registers[1] ^ operand
            if val == 2:
                registers[1] = combo(operand) % 8
            if val == 3:
                if registers[0] != 0:
                    pointer = operand
                    continue
            if val == 4:
                registers[1] = registers[1] ^ registers[2]
            if val == 5:
                newout = combo(operand) % 8
                if newout == outval:
                    sols[outval].append(ainit)
                break
            if val == 6:
                registers[1] = math.floor(registers[0] / (2 ** combo(operand)))
            if val == 7:
                registers[2] = math.floor(registers[0] / (2 ** combo(operand)))

            pointer += 2


def stitchsols(progr, currentsols):
    if len(progr) == 1:
        localsols = [sol for sol in sols[progr[0]] if ((sol * 8) % (2 ** 10) ) == (currentsols[0] - (currentsols[0] % 8))]
        return [[sol, *currentsols] for sol in localsols]
    
    solutions = []
    if currentsols:
        localsols = [sol for sol in sols[progr[-1]] if ((sol * 8) % (2 ** 10) ) == (currentsols[0] - (currentsols[0] % 8))]
    else:
        localsols = sols[progr[-1]]

    for sol in localsols:
        solutions += stitchsols(progr[:-1], [sol, *currentsols])

    return solutions



finalsols = stitchsols(prog[::-1], [])

nums = []
for sol in finalsols:
    num = ""
    for p in sol:
        num = num + "{0:07b}".format(p)[-3:] if num else "{0:07b}".format(p)
    nums.append(int(num, 2))

print(min(nums))
