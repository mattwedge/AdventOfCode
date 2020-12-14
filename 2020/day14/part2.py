def get_val_pt2(mem_val, mask):
    mask_copy = list(mask[::-1])
    bin_mem_val = list("{0:b}".format(mem_val)[::-1])

    for i, m in enumerate(mask_copy):
        if (len(bin_mem_val) >= i + 1) and m == "0" and bin_mem_val[i]:
            mask_copy[i] = bin_mem_val[i]

    return mask_copy[::-1]

def get_possible(mask):
    if not "X" in mask:
        return [mask]
    all_possible = []
    floating_indices = [i for i in range(len(mask)) if mask[i] == "X"]
    for floating_val in [0, 1]:
        mask_copy = mask
        mask_list = list(mask_copy)
        mask_list[floating_indices[0]] = floating_val
        all_possible += get_possible("".join([str(a) for a in mask_list]))

    return all_possible

def get_vals_pt2(mem_val, mask):
    return [int(
        "".join([str(a) for a in val]),
        2
    ) for val in get_possible("".join(get_val_pt2(mem_val, mask)))]

if __name__=="__main__":
    input = open("./input.txt", "r").read().splitlines()

    mask = None
    mem = {}

    for instr in input:
        if "mask" in instr:
            mask = instr.split("mask = ")[1]
        else:
            base_mem_addr = int(instr.split("mem[")[1].split("]")[0])
            for mem_addr in get_vals_pt2(base_mem_addr, mask):
                mem[mem_addr] = int(instr.split("] = ")[1])

    print(sum(mem.values()))
