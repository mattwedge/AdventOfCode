# 1:22:00

f = open("./input.txt", "r")
input = [int(a) for a in f.read().split()]


def calculate_stones(a):
    if a == 0:
        return [1]

    a_len = len(str(a))
    if a_len % 2 == 0:
        return [int("".join(str(a)[:int(a_len / 2)])), int("".join(str(a)[int(a_len / 2):])), ]

    return [a * 2024]

print("BUILDING WEB")
web = {}
for a in input:
    curr = [a]
    while True:
        new_curr = []
        for digit in curr:
            if digit in web:
                continue
            split = calculate_stones(digit)
            web[digit] = calculate_stones(digit)
            new_curr += split
        
        if not new_curr:
            break

        curr = new_curr

print("CALCULATING 25s")
next_25s = {}
total_25s = {}
for a in web.keys():
    curr = [a]
    for i in range(25):
        next = []
        for c in curr:
            next += web[c]

        curr = next

    total_25s[a] = len(curr)
    next_25s[a] = curr

total_25 = 0
total_75 = 0

for a in input:
    print(a)
    total_25 += total_25s[a]
    next = next_25s[a]
    for n in next:
        nnext = next_25s[n]
        for m in nnext:
            total_75 += total_25s[m]

print(total_25)
print(total_75)