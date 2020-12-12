def md(pos):
    return abs(pos[0]) + abs(pos[1])

if __name__ == "__main__":
    input = open("./input.txt", "r").read().splitlines()

    waypoint_offset = [1, 10]
    ship_pos = [0, 0]

    def do_instr(instr):
        global waypoint_offset
        global ship_pos

        char = instr[0]
        num = int(instr[1:])

        if char == "N":
            waypoint_offset[0] += num
        if char == "S":
            waypoint_offset[0] -= num
        if char == "E":
            waypoint_offset[1] += num
        if char == "W":
            waypoint_offset[1] -= num
        if char == "L":
            if num == 90:
                waypoint_offset = [waypoint_offset[1], -waypoint_offset[0]]
            elif num == 180:
                waypoint_offset = [-waypoint_offset[0], -waypoint_offset[1]]
            elif num == 270:
                do_instr("R90")

        if char == "R":
            if num == 90:
                waypoint_offset = [-waypoint_offset[1], waypoint_offset[0]]
            elif num == 180:
                do_instr("L180")
            elif num == 270:
                do_instr("L90")

        if char == "F":
            ship_pos[0] += waypoint_offset[0] * num
            ship_pos[1] += waypoint_offset[1] * num

    for instr in input:
        do_instr(instr)

    print(md(ship_pos))
