# 59:59

import numpy as np
import re

f = open("./input.txt", "r")
robots = [[int(a) for a in re.findall("[-\d]+", line)] for line in f.read().splitlines()]

grid_width = 101
grid_height = 103
grid_middle_x = int((grid_width - 1) / 2)
grid_middle_y = int((grid_height - 1) / 2)

current_positions = [[robot[0], robot[1]] for robot in robots]
seconds = 0
while True:
    seconds += 1
    current_positions = [
        [(current_position[0] + robot[2]) % grid_width, (current_position[1] + robot[3]) % grid_height]
        for current_position, robot in zip(current_positions, robots)
    ]

    if seconds == 100:
        print(
            "Part 1: " + str(
                len([p for p in current_positions if p[0] > grid_middle_x and p[1] > grid_middle_y])
                * len([p for p in current_positions if p[0] < grid_middle_x and p[1] > grid_middle_y])
                * len([p for p in current_positions if p[0] > grid_middle_x and p[1] < grid_middle_y])
                * len([p for p in current_positions if p[0] < grid_middle_x and p[1] < grid_middle_y])
            )
        )

    # If 80% of the robots are near the middle then print the image and exit
    centralps = len([p for p in current_positions if p[0] > 10 and p[0] < grid_width - 10 and p[1] > 10 and p[1] < grid_height -10])
    if centralps > len(robots) * 0.8:
        # Print the image
        im = np.zeros(shape=(grid_width, grid_height))
        for p in current_positions:
            im[p[0], p[1]] = 1
        for rownum, row in enumerate(im):
            print("".join([str(int(a)) if a else " " for a in row]))


        print(f"Part 2: {seconds}")
        break

