import re

def add_brackets(rule):
    return ("(" + rule.replace(" ", ")(") + ")").replace("(|)", "|")

def generate_repeat_regex(n1, n2, max_num_repeats):
    """Generate regex that matches n1 repeated N times and then n2 repeated N times
        i.e. the same number of times.
        Args:
            n1: The first number
            n2: The first number
            max_num_repeats: the maximum number of repeats that we will capture
    """
    regex = ""
    for i in range(max_num_repeats):
        if i > 0:
            regex += "|"
        regex += "("  + f"({n1})" * (i + 1) + f"({n2})" * (i + 1) + ")"

    return "({})".format(regex)

if __name__ == "__main__":
    input_data = open("./input.txt", "r").read().splitlines()

    all_rules = {
        num: add_brackets(unparsed_rule).replace("\"", "")
        for (num, unparsed_rule) in [line.split(": ") for line in input_data if ":" in line]
    }

    for num in all_rules:
        ### The new rule amounts to repeated (42) any number of times
        all_rules[num] = all_rules[num].replace("(8)", "((42)+)")
        ### The new rule amounts to (42) repeated any number of times and then
        ### (31) the same number of times
        all_rules[num] = all_rules[num].replace("(11)", generate_repeat_regex(42, 31, 4))

    while any([re.search("[0-9]", rule.replace("(8)", "").replace("(11)", "")) for rule in all_rules.values()]):
        for num, rule in all_rules.items():
            if not re.search(r"[0-9]", rule):
                for num2, rule2 in all_rules.items():
                    search = re.search(r"\({}\)".format(num), rule2)
                    if search:
                        start = search.start()
                        end = search.end()
                        all_rules[num2] = all_rules[num2][:start + 1] + rule + all_rules[num2][end - 1:]

    print(len([line for line in input_data if not ":" in line and re.match(all_rules["0"] + "$", line)]))
