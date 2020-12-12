def md(pos):
    return abs(pos[0]) + abs(pos[1])

if __name__ == "__main__":
    input = open("./input.txt", "r").read().splitlines()

    pos = [0, 0]
    direc = 0

    def do_instr(instr):
        global direc
        char = instr[0]
        num = int(instr[1:])
        if char == "N":
            pos[0] += num
        if char == "S":
            pos[0] -= num
        if char == "E":
            pos[1] += num
        if char == "W":
            pos[1] -= num
        if char == "L":
            direc += num
        if char == "R":
            direc -= num

        if char == "F":
            dir_dict = {
                0: "E",
                90: "N",
                180: "W",
                270: "S"
            }
            do_instr(dir_dict[direc % 360] + str(num))

    for instr in input:
        do_instr(instr)
        
    print(md(pos))
