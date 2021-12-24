# 3:01:06

# Inspecting the instructions, we can see that they come in chunks of 18 commands,
# where all commands are the same except the 5th, 6th and 16th commands. We also observe
# that the `mul x 0` and `mul y 0` commands reset `x` and `y` to `0`, and `w` is the input
# digit at the start of each chunk, so `z` is the only value that changes. If we call the
# changing variables in the 5th, 6th and 16th commands `A`, `B` and `C` respectively then
# we see that `z_2` depends on `z_1` as follows (where `z_1` is the value of `z` at the
# start of the chunk, `z_2` is the value at the end, and `w` is the input digit):

# if A == 26:
#     z_2 == z_1 // 26 if ((z_1 % 26) + B == w) else ((w + C) + ((z_1 // 26) * 26))
# if A == 1:
#     z_2 == (w + C) + (z_1 * 26)


if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_ops = f.read().splitlines()
    input_ops = [ln.split(" ") for ln in input_ops]
    for op in input_ops:
        if op[-1] not in ["w", "x", "y", "z"]:
            op[-1] = int(op[-1])

    relevant_input_pairs = list(zip(
        [op[-1] for op in input_ops[4::18]],
        [op[-1] for op in input_ops[5::18]],
        [op[-1] for op in input_ops[15::18]],
    ))


    def solve(highest=True):
        input_result_dict = {
            0: ""
        }
        for iteration, (a, b, c) in enumerate(relevant_input_pairs):
            output_result_dict = {}
            for z, str_so_far in input_result_dict.items():
                for w in range(1, 10):
                    if a == 26:
                        new_output = z // 26 if ((z % 26) + b == w) else ((w + c) + ((z // 26) * 26))
                    elif a == 1:
                        new_output = (w + c) + (z * 26)

                    if highest or (not new_output in output_result_dict.keys()):
                        output_result_dict[new_output] = str_so_far + str(w)

            input_result_dict = output_result_dict

        return int(input_result_dict[0])

    print(solve())
    print(solve(highest=False))
