if __name__ == "__main__":
    f = open("./input.txt", "r")
    steps = [a.split(" ") for a in f.read().splitlines()]
    for step in steps:
        step[1] = int(step[1])
    acc = 0
    current_step = 0
    done_steps = [0]
    while True:
        if steps[current_step][0] == "acc":
            acc += steps[current_step][1]
            current_step += 1
        elif steps[current_step][0] == "jmp":
            current_step += steps[current_step][1]
        elif steps[current_step][0] == "nop":
            current_step += 1
        if current_step in done_steps:
            print(acc)
            break
        else:
            done_steps.append(current_step)
