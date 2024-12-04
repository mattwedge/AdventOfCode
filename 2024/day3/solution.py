# 12:08

import re

def calculate_section(section):
    matches = re.findall(r"mul\((\d+)\,(\d+)\)", section)
    return sum(int(match[0]) * int(match[1]) for match in matches)    

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read()
    
    part_1_res = calculate_section(input)
    
    do_sections = [section.split("don't()")[0] for section in input.split("do()")]
    part_2_res = sum(calculate_section(section) for section in do_sections)

    print(f"{part_1_res = }")
    print(f"{part_2_res = }")