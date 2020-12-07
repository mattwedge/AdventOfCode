def get_colors_containing_color(all_rules, color):
        containing_colors = []
        for key in all_rules:
            if color in all_rules[key]:
                containing_colors.append(key)
        return containing_colors

if __name__ == "__main__":
    f = open("./input.txt", "r")
    rule_strings = f.read().splitlines()

    all_rules = {}
    for rule_string in rule_strings:
        bag_color, containing_bags = rule_string.split(" bags contain ")
        containing_bags_list = containing_bags.replace(".", "").split(", ")
        all_rules[bag_color] = {
            containing_bag[containing_bag.index(" ") + 1:].replace(" bags", "").replace(" bag", ""): containing_bag[:containing_bag.index(" ")]
            for containing_bag in containing_bags_list
        }

    recursive_list = []
    current_list = ["shiny gold"]
    while True:
        new_allowed_containers = sum([get_colors_containing_color(all_rules, color) for color in current_list], [])
        current_list = new_allowed_containers
        if not current_list:
            break
        else:
            recursive_list.append(current_list)

    unique_containing_colors = list(set(sum(recursive_list, [])))
    print(len(unique_containing_colors))
