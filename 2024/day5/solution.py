# 17:59

from functools import cmp_to_key

def check_order(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

def order_update(update, rules: list):
    return sorted(update, key=cmp_to_key(lambda a, b: -1 if [b, a] in rules else 1))

def get_middle(arr):
    return arr[int((len(arr) - 1) / 2)]

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read()
    lines = input.splitlines()

    empty_line = lines.index("")
    rules = [[int(n) for n in line.split("|")] for line in lines[:empty_line]]
    updates = [[int(n) for n in line.split(",")] for line in lines[empty_line + 1:]]

    total_sum = sum(get_middle(update) for update in updates if check_order(update, rules))
    total_corrected_sum = sum(get_middle(order_update(update, rules)) for update in updates if not check_order(update, rules))

    print(f"{total_sum = }")    
    print(f"{total_corrected_sum = }")    
