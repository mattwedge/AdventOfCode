def get_nth_num(starting_numbers, n):
    all_nums = starting_numbers.copy()
    pos_hash = {
        num: all_nums.index(num)
        for num in all_nums[:-1]
    }

    num_nums = len(all_nums)
    last_num = all_nums[-1]
    while True:
        if last_num in pos_hash:
            new_num = num_nums - pos_hash[last_num] - 1
        else:
            new_num = 0

        pos_hash[last_num] = num_nums - 1
        num_nums += 1

        last_num = new_num
        if num_nums == n:
            break

    return last_num

if __name__=="__main__":
    starting_nums = [int(num) for num in open("./input.txt", "r").read().split(",")]
    print(get_nth_num(starting_nums, 2020))
    print(get_nth_num(starting_nums, 30000000))
