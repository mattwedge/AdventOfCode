from collections import defaultdict


lines = open("./input.txt", "r").read().splitlines()

vals = {}
ops = defaultdict(lambda: defaultdict(list))
outdeps = defaultdict(list)
adding_ops = False
for line in lines:
    if line == "":
        adding_ops = True
        continue
    if adding_ops:
        inpts, out = line.split(" -> ")
        inp1, op, inp2 = inpts.split(" ")
        ops[inp1][inp2].append([op, out])
        vals[out] = None
        outdeps[out].append(inp1)
        outdeps[out].append(op)
        outdeps[out].append(inp2)
    else:
        k, v = line.split(": ")
        vals[k] = int(v)

while None in vals.values():
    print(vals)
    for inp1, obj in ops.items():
        for inp2, outobj in obj.items():
            if vals[inp1] is not None and vals[inp2] is not None:
                for op, out in outobj:
                    if op == "AND":
                        vals[out] = vals[inp1] and vals[inp2]
                    if op == "OR":
                        vals[out] = vals[inp1] or vals[inp2]
                    if op == "XOR":
                        vals[out] = vals[inp1] ^ vals[inp2]

zvals = {}
xvals = {}
yvals = {}
for k, v in vals.items():
    if k.startswith("z"):
        pos = int(k[1:])
        zvals[pos] = v
    if k.startswith("x"):
        pos = int(k[1:])
        xvals[pos] = v
    if k.startswith("y"):
        pos = int(k[1:])
        yvals[pos] = v

sx = ""
for pos in sorted(xvals.keys()):
    sx += str(xvals[pos])

sy = ""
for pos in sorted(yvals.keys()):
    sy += str(yvals[pos])

sz = ""
for pos in sorted(zvals.keys()):
    sz += str(zvals[pos])

print(sx[::-1])
print(sy[::-1])
print(sz[::-1])

zsum = "{0:00b}".format(int(sx[::-1], 2) + int(sy[::-1], 2))
print(zsum)
zdiffs = []
for i in range(len(zsum)):
    if zsum[::-1][i] != sz[i]:
        zdiffs.append(i)
print(zdiffs)

zdiffstrs = ["z{:02}".format(zz) for zz in zdiffs]

zdeps = {}
for zstr in zdiffstrs:
    deps = set(outdeps[zstr])
    while True:
        depsorig = set(deps)
        for dep in depsorig:
            deps |= set(outdeps[dep])
        if deps == depsorig:
            break

    zdeps[zstr] = deps

print(zdeps)
for v in zdeps.values():
    print(len(v))


# z07 -> vmv
# z20 -> kfm
# z28 -> hnv
# hth -> tqr

# bvd,hnv,kfn,vmv,z07,z20,z28,z45

# zN = xN XOR yN XOR (SUM(N-1))