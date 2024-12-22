# 43:05
from collections import Counter, deque

lines = [int(a) for a in open("./input.txt", "r").read().splitlines()]

def calc(secret):
    sec = secret
    sec = ((sec << 6) ^ sec) % 16777216
    sec = ((sec >> 5) ^ sec) % 16777216
    sec = ((sec << 11) ^ sec) % 16777216
    return sec

total_secrets = 0
seq_banana_totals = Counter()
for sec in lines:
    line_banana_totals = Counter()
    last4 = deque([None, None, None, None])
    prev = int(str(sec)[-1])
    for i in range(2000):
        sec = calc(sec)
        new_prev = int(str(sec)[-1])
        diff = new_prev - prev
        last4.popleft()
        last4.append(diff)

        if None not in last4 and str(last4) not in line_banana_totals:
            line_banana_totals[str(last4)] = new_prev

        prev = new_prev

    seq_banana_totals += line_banana_totals
    total_secrets += sec

max_bananas = max(seq_banana_totals.values())

print(total_secrets)
print(max_bananas)
