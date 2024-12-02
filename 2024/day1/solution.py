# 4:41

from collections import Counter

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()

    list1, list2 = [], []
    for line in input_lines:
        nums = [int(a) for a in line.split()]
        list1.append(nums[0])
        list2.append(nums[1])

    list1 = sorted(list1)
    list2 = sorted(list2)
        
    total_distance = sum(abs(a - b) for a,b in zip(list1, list2))
    similarity = sum(num * Counter(list2)[num] for num in list1)

    print(f"{total_distance = }")
    print(f"{similarity = }")
