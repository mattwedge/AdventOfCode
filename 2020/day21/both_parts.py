import functools
import collections

if __name__ == "__main__":
    input_data = open("./input.txt", "r").read().splitlines()
    allergens_arr = []
    for line in input_data:
        ingredients = line.split(" (")[0].split(" ")
        allergens = line.split(" (contains ")[1].replace(")", "").split(", ")
        allergens_arr.append({
            "ingr": ingredients,
            "allergens": allergens
        })

    all_allergens = set(functools.reduce(lambda x, y: x + y, [a["allergens"] for a in allergens_arr], []))
    all_ingredients = set(functools.reduce(lambda x, y: x + y, [a["ingr"] for a in allergens_arr], []))

    possibilities = {}
    for allergen in all_allergens:
        relevant_lists = [d for d in allergens_arr if allergen in d["allergens"]]
        possible_ingredients = functools.reduce(lambda a, b: a.intersection(b["ingr"]), relevant_lists, set(all_ingredients))
        possibilities[allergen] = possible_ingredients

    all_possible = functools.reduce(lambda a, b: a.union(b), possibilities.values(), set())
    all_impossible = [a for a in all_ingredients if not a in all_possible]

    ingr_counts = collections.Counter(functools.reduce(lambda x, y: x + y, [a["ingr"] for a in allergens_arr], []))
    print(functools.reduce(lambda a, b: a + b, [ingr_counts[ingr] for ingr in all_impossible], 0))
    
    while not all([len(possibilities[p]) == 1 for p in possibilities]):
        for p in possibilities:
            if len(possibilities[p]) == 1:
                known = list(possibilities[p])[0]
                for q in possibilities:
                    if not p == q:
                        if known in possibilities[q]:
                            possibilities[q].remove(known)

    possibilities = {
        p: list(possibilities[p])[0]
        for p in possibilities
    }

    res_arr = []
    for ingr in sorted(possibilities):
        res_arr.append(possibilities[ingr])

    print(",".join(res_arr))
