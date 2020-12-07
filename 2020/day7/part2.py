if __name__ == "__main__":
    f = open("./input.txt", "r")
    rule_strings = f.read().splitlines()

    all_rules = {}
    for rule_string in rule_strings:
        bag_color, containing_bags = rule_string.split(" bags contain ")
        containing_bags_list = containing_bags.replace(".", "").split(", ")
        if "no other bags" in containing_bags_list:
            all_rules[bag_color] = {}
        else:
            all_rules[bag_color] = {
                containing_bag[containing_bag.index(" ") + 1:].replace(" bags", "").replace(" bag", ""): int(containing_bag[:containing_bag.index(" ")])
                for containing_bag in containing_bags_list
            }

    recursive_list = []
    current_layer = {"shiny gold": 1}
    num_bags = 0
    while True:
        new_layer = {}
        for color in current_layer:
            quantity = current_layer[color]
            for new_color in all_rules[color]:
                if new_color in new_layer:
                    new_layer[new_color] += all_rules[color][new_color] * quantity
                else:
                    new_layer[new_color] = all_rules[color][new_color] * quantity

        if not new_layer:
            break
        else:
            print(new_layer.values())
            num_bags += sum(new_layer.values())
            current_layer = new_layer

    print(num_bags)
