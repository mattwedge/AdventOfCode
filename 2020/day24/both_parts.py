HEX_NEIGHTBOUR_RELATIVE_POSITIONS = {
    "e": (0, 1),
    "w": (0, -1),
    "sw": (-1, -1),
    "se": (-1, 0),
    "nw": (1, 0),
    "ne": (1, 1)
}

def get_coord(instr):
    pos = (0, 0)
    for step in instr:
        rel_pos = HEX_NEIGHTBOUR_RELATIVE_POSITIONS[step]
        pos = (pos[0] + rel_pos[0], pos[1] + rel_pos[1])
    return pos

def count_neighbours(pos, black_tiles):
    neighbour_positions = [
        (pos[0] + rel_pos[0], pos[1] + rel_pos[1]) for rel_pos in HEX_NEIGHTBOUR_RELATIVE_POSITIONS.values()
    ]

    return len(set(neighbour_positions).intersection(black_tiles))

def expand_tiles(black_tiles):
    tiles_copy = set(black_tiles)
    new_tiles = set()
    for tile in tiles_copy:
        tile_neighbours = [
            (tile[0] + rel_pos[0], tile[1] + rel_pos[1])
            for rel_pos in HEX_NEIGHTBOUR_RELATIVE_POSITIONS.values()
        ]
        for neighbour in tile_neighbours:
            if not neighbour in tiles_copy:
                if not neighbour in new_tiles:
                    new_tiles.add(neighbour)

    return tiles_copy.union(new_tiles)

def run_iter(black_tiles):
    expanded_tiles = expand_tiles(black_tiles)

    tiles_to_flip = set()
    for tile in expanded_tiles:
        adj_black = count_neighbours(tile, black_tiles)
        if tile in black_tiles:
            if not adj_black in [1, 2]:
                tiles_to_flip.add(tile)
        else:
            if adj_black == 2:
                tiles_to_flip.add(tile)

    new_tiles = set(black_tiles)
    for tile in tiles_to_flip:
        if tile in new_tiles:
            new_tiles.remove(tile)
        else:
            new_tiles.add(tile)

    return new_tiles

def parse_instruction(instr):
    line_instructions = []
    last_two_chars = False
    for i, char in enumerate(instr):
        if char in ["e", "w"]:
            if last_two_chars:
                last_two_chars = False
                continue
            line_instructions.append(char)
        elif char in ["s", "n"]:
            line_instructions.append(char + instr[i+1])
            last_two_chars = True
    return line_instructions


if __name__ == "__main__":
    input_data = open("input.txt", "r").read().splitlines()
    all_instructions = [parse_instruction(line) for line in input_data]

    ### Part 1
    black_tiles = set()
    for instr in all_instructions:
        pos = get_coord(instr)
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)
    print(len(black_tiles))

    ### Part 2
    num_iter = 100
    for i in range(num_iter):
        black_tiles = run_iter(black_tiles)

    print(len(black_tiles))
