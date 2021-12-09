# 39:33

from collections import Counter

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input_lines = [[s.split(" ") for s in l.split(" | ") ] for l in f.read().splitlines()]
    
    # Part 1
    print(sum(len([d for d in b if len(d) in [2, 4, 3, 7]]) for [_, b] in input_lines))

    # Part 2
    example_mapping = {
        "cagedb": 0,
        "ab": 1,
        "gcdfa": 2,
        "fbcad": 3,
        "eafb": 4,
        "cdfbe": 5,
        "cdfgeb": 6,
        "dab": 7,
        "acedgfb": 8,
        "cefabd": 9,
    }

    def map_pattern(pattern, all_patterns):
        """Convert the pattern into a shuffle-invariant representation.
        
        By counting the occurences of each letter over all patterns and replacing
        the letter with this count, we get a representation for a pattern that will
        be the same regardless of the shuffling. Fortunately this representation is
        also unique so we can easily match it up with the example mappings.
        """
        counts = Counter("".join(all_patterns))
        return "".join([str(a) for a in sorted([counts[letter] for letter in pattern])])

    updated_example_mapping = {
        map_pattern(k, example_mapping.keys()): v
        for k, v in example_mapping.items()
    }

    total = 0
    for line in input_lines:
        patterns = line[0]
        outputs = line[1]
        updated_outputs = [map_pattern(output, patterns) for output in outputs]
        parsed_outputs = [updated_example_mapping[output] for output in updated_outputs]

        total += int("".join([str(a) for a in parsed_outputs]))

    print(total)
