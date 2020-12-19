import re

def add_brackets(rule):
    return ("(" + rule.replace(" ", ")(") + ")").replace("(|)", "|")

if __name__ == "__main__":
    input_data = open("./input.txt", "r").read().splitlines()

    all_rules = {
        num: add_brackets(unparsed_rule).replace("\"", "")
        for (num, unparsed_rule) in [line.split(": ") for line in input_data if ":" in line]
    }

    while any([re.search("[0-9]", rule) for rule in all_rules.values()]):
        for num, rule in all_rules.items():
            if not re.search(r"[0-9]", rule):
                for num2, rule2 in all_rules.items():
                    search = re.search(r"\({}\)".format(num), rule2)
                    if search:
                        start = search.start()
                        end = search.end()
                        all_rules[num2] = all_rules[num2][:start + 1] + rule + all_rules[num2][end - 1:]

    print(len([line for line in input_data if not ":" in line and re.match(all_rules["0"] + "$", line)]))
