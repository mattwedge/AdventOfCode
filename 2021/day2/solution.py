# 5:15

def part1():
    f = open("./input.txt", "r")
    input_instructions = [ln.split(" ") for ln in f.read().splitlines()]
    total_forward = sum([int(instr[1]) for instr in input_instructions if instr[0] == "forward"])
    total_depth = (
        sum([int(instr[1]) for instr in input_instructions if instr[0] == "down"])
        - sum([int(instr[1]) for instr in input_instructions if instr[0] == "up"])
    )

    return total_depth * total_forward

def part2():
    f = open("./input.txt", "r")
    input_instructions = [ln.split(" ") for ln in f.read().splitlines()]
    total_forward = sum([int(instr[1]) for instr in input_instructions if instr[0] == "forward"])
    
    depth = 0
    aim = 0
    for instr in input_instructions:
        instr[1] = int(instr[1])
        if instr[0] == "forward":
            depth += aim * instr[1]
        if instr[0] == "down":
            aim += instr[1]
        if instr[0] == "up":
            aim -= instr[1]

    return depth * total_forward

if __name__ == "__main__":
    print(part1())
    print(part2())