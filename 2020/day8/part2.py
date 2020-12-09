def toggle_step(step):
    if step[0] == "jmp":
        step[0] = "nop"
    elif step[0] == "nop":
        step[0] = "jmp"

if __name__ == "__main__":
    f = open("./input.txt", "r")
    steps = [a.split(" ") for a in f.read().splitlines()]
    for step in steps:
        step[1] = int(step[1])

    for step in steps:
        toggle_step(step)

        acc = 0
        current_step = 0
        done_steps = [0]
        finished = False
        while True:
            if steps[current_step][0] == "acc":
                acc += steps[current_step][1]
                current_step += 1
                if current_step == len(steps):
                    print(acc)
                    finished = True
                    break
                elif current_step > len(steps):
                    toggle_step(step)
                    continue
            elif steps[current_step][0] == "jmp":
                current_step += steps[current_step][1]
                if current_step == len(steps):
                    print(acc)
                    finished = True
                    break
                elif current_step > len(steps):
                    toggle_step(step)
                    continue
            elif steps[current_step][0] == "nop":
                current_step += 1
                if current_step == len(steps):
                    print(acc)
                    finished = True
                    break
                elif current_step > len(steps):
                    toggle_step(step)
                    continue
            if current_step in done_steps:
                toggle_step(step)
                break
            else:
                done_steps.append(current_step)

        if finished:
            break
