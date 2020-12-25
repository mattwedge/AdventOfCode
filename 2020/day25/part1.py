def transform(val, subject_num):
    val = val * subject_num
    val = val % 20201227
    return val

def transform_n_times(num, loop_size):
    val = 1
    for i in range(loop_size):
        val = transform(val, num)
    return val

if __name__ == "__main__":
    public_keys = [int(a) for a in open("./input.txt", "r").read().splitlines()]

    loop_sizes = []
    for key in public_keys:
        val = 1
        num_iter = 0
        while not val == key:
            num_iter += 1
            val = transform(val, 7)
        loop_sizes.append(num_iter)

    print(transform_n_times(public_keys[0], loop_sizes[1]))
    