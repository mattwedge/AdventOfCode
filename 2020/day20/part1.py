import numpy as np

def get_edges(tile):
    return {
        0: list(tile[0]),
        90: [row[-1] for row in tile],
        180: list(tile[-1])[::-1],
        270: [row[0] for row in tile][::-1],
    }

def check_match(tile1, tile2):
    edges1 = get_edges(tile1)
    edges2 = get_edges(tile2)
    for pos, edge in edges1.items():
        for pos2, edge2 in edges2.items():
            if edge == edge2:
                return True
            if edge == edge2[::-1]:
                return True

if __name__ == "__main__":
    tiles = open("./input.txt", "r").read().split("\n\n")
    tiles = [tile.split("\n") for tile in tiles]
    tiles = {
        tile[0].replace(":", "").replace("Tile ", ""): {
            "image": tile[1:]
        }
        for tile in tiles
    }

    for tile_id, tile in tiles.items():
        num_matches = 0
        for tile_id2, tile2 in tiles.items():
            if not tile_id == tile_id2:
                if check_match(tile["image"], tile2["image"]):
                    num_matches += 1
        tiles[tile_id]["num_matches"] = num_matches

    print(np.product([int(tile_id) for tile_id, tile in tiles.items() if tile["num_matches"] < 3]))
