# 25:32

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read()
    x_str, y_str = input.split(", ")
    x_range = [int(x) for x in x_str.split("x=")[1].split("..")]
    y_range = [int(y) for y in y_str.split("y=")[1].split("..")]

    x_range = range(x_range[0], x_range[1] + 1)
    y_range = range(y_range[0], y_range[1] + 1)

    def hits_target(x_vel_init, y_vel_init, target_x_range, target_y_range):
        x_pos = y_pos = y_pos_max = 0
        x_vel = x_vel_init
        y_vel = y_vel_init

        hits = False
        while (x_pos <= target_x_range[-1]) and (y_pos >= target_y_range[0]):
            x_pos += x_vel
            y_pos += y_vel
            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel == 1
            y_vel -= 1

            if y_pos > y_pos_max:
                y_pos_max = y_pos

            if x_pos in x_range and y_pos in y_range:
                hits = True
                break

        return hits, y_pos_max

    results = {}
    for x_vel_init in range(x_range[-1] + 1):
        for y_vel_init in range(y_range[0] - 1, 1000):
            hits, y_pos_max = hits_target(x_vel_init, y_vel_init, x_range, y_range)
            if hits:
                results["{}_{}".format(x_vel_init, y_vel_init)] = y_pos_max

    print(max(list(results.values())))
    print(len(list(results.values())))
