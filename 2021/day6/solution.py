# 52:17

from functools import lru_cache

@lru_cache(maxsize=None)
def total_spawn(days, days_to_first_birth):
    if days < days_to_first_birth:
        return 1

    return total_spawn(days - days_to_first_birth, 7) + total_spawn(days - days_to_first_birth, 9)

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = f.read().splitlines()
    times = [int(n) for n in input_lines[0].split(",")]
    
    for num_days in [80, 256]:
        print(sum([total_spawn(num_days, time + 1) for time in times]))
