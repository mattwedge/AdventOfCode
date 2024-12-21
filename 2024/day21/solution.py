import re
import numpy as np

lines = open("./input.txt", "r").read().splitlines()


charpositions = {
    "A": 0 + 0j,
    "0": 1 + 0j,
    "1": 2 + 1j,
    "2": 1 + 1j,
    "3": 0 + 1j,
    "4": 2 + 2j,
    "5": 1 + 2j,
    "6": 0 + 2j,
    "7": 2 + 3j,
    "8": 1 + 3j,
    "9": 0 + 3j,
}

dirpositions = {
    ">": 0 + 0j,
    "v": 1 + 0j,
    "<": 2 + 0j,
    "A": 0 + 1j,
    "^": 1 + 1j,
}

dirmovements = {
    "<": 1,
    ">": -1,
    "^": 1j,
    "v": -1j,
    "A": 0,
}

inv_dirpositions = {v: k for k, v in dirpositions.items()}
inv_charpositions = {v: k for k, v in charpositions.items()}


def get_dirs_for_num_char(char, currpos):
    charposition = charpositions[char]
    yoffs = int((charposition - currpos).imag)
    xoffs = int((charposition - currpos).real)

    xdir = "<" if xoffs >= 0 else ">"
    ydir = "^" if yoffs >= 0 else "v"

    reses =  list(set([xdir * abs(xoffs) + ydir * abs(yoffs) + "A", ydir * abs(yoffs) + xdir * abs(xoffs) + "A"]))

    realres = []
    for res in reses:
        fake = False
        posnow = currpos
        for v in res:
            posnow += dirmovements[v]
            if posnow == 2:
                fake = True

        if not fake:
            realres.append(res)

    return realres

def get_dirs_for_dir_char(char, currpos):
    dirposition = dirpositions[char]
    yoffs = int((dirposition - currpos).imag)
    xoffs = int((dirposition - currpos).real)

    xdir = "<" if xoffs >= 0 else ">"
    ydir = "^" if yoffs >= 0 else "v"

    return list(set([xdir * abs(xoffs) + ydir * abs(yoffs) + "A", ydir * abs(yoffs) + xdir * abs(xoffs) + "A"]))

def get_dirs_for_num_code(code, currpos):
    posnow = currpos
    dirs = []
    for char in code:
        newdirs = []
        chardirs = get_dirs_for_num_char(char, posnow)
        if dirs:
            for chardir in chardirs:
                for dir in dirs:
                    newdirs.append(dir + chardir)

        else:
            newdirs = chardirs

        dirs = newdirs
        posnow = charpositions[char]

    return dirs

def get_dirs_for_dir_code(code, currpos):
    posnow = currpos
    dirs = []
    for char in code:
        newdirs = []
        dirdirs = get_dirs_for_dir_char(char, posnow)
        if dirs:
            for chardir in dirdirs:
                for dir in dirs:
                    newdirs.append(dir + chardir)

        else:
            newdirs = dirdirs

        dirs = newdirs
        posnow = dirpositions[char]

    return dirs



num_bots = 2
total = 0
for code in lines:
    print(code)
    dircodes = get_dirs_for_num_code(code, charpositions["A"])
    for i in range(num_bots):
        print(dircodes)
        print(i)
        newdircodes = []
        for dircode in dircodes:
            newdircodes += get_dirs_for_dir_code(dircode, dirpositions["A"])
        
        mini = min(len(c) for c in newdircodes)
        dircodes = [c for c in newdircodes if len(c) == mini]

    mini = min(len(c) for c in dircodes)
    total += mini * int(re.findall("\d+", code)[0])

print(total)



# def parse_dirs(dirs):
#     res = ""
#     pos0 = dirpositions["A"]
#     pos1 = dirpositions["A"]
#     pos2 = charpositions["A"]
#     pos3 = 0 + 0j
#     for dir in dirs:
#         if dir == "A":
#             if inv_dirpositions[pos0] == "A":
#                 if inv_dirpositions[pos1] == "A":
#                     res += inv_charpositions[pos2]
#                 else:
#                     pos2 += dirmovements[inv_dirpositions[pos1]]
#             else:
#                 pos1 += dirmovements[inv_dirpositions[pos0]]
#         else:
#             pos0 += dirmovements[dir]

#     return res

# print(parse_dirs("<vA<AA>>^AA<Av>A^AvA^Av<<A>>^AAvA^A<vA>^AA<A>A<vA<A>>^AAAvA<^A>A"))
# print(parse_dirs("<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))

