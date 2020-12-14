def get_val(mem_val, mask):
    mask_copy = list(mask[::-1])
    bin_mem_val = list("{0:b}".format(mem_val)[::-1])

    for i, m in enumerate(mask_copy):
        if (len(bin_mem_val) >= i + 1) and m == "X" and bin_mem_val[i]:
            mask_copy[i] = bin_mem_val[i]
        elif m == "X":
            mask_copy[i] = 0

    return int("".join([str(a) for a in mask_copy[::-1]]), 2)

if __name__=="__main__":
    input = open("./input.txt", "r").read().splitlines()

    mask = None
    mem = {}

    for instr in input:
        if "mask" in instr:
            mask = instr.split("mask = ")[1]
        else:
            mem[int(instr.split("mem[")[1].split("]")[0])] = get_val(int(instr.split("] = ")[1]), mask)
  
    print(sum(mem.values()))
