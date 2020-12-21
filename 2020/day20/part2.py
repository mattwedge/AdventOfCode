import numpy as np
import collections

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
                return (pos, pos2, -1)
            if edge == edge2[::-1]:
                return (pos, pos2, 1)
    return False

def get_subarray(arr, i, j, shape):
    return arr[i:i+shape[0], j:j+shape[1]]

if __name__ == "__main__":
    tiles = open("./input.txt", "r").read().split("\n\n")
    tiles = [tile.split("\n") for tile in tiles]
    tiles = {
        tile[0].replace(":", "").replace("Tile ", ""): {
            "image": np.array([list(row) for row in tile[1:]])
        }
        for tile in tiles
    }

    orientated_tiles = [list(tiles.keys())[0]]
    last_orientated_tiles = [list(tiles.keys())[0]]
    while last_orientated_tiles:
        new_orientated_tiles = []
        for tile_id in last_orientated_tiles:
            tile = tiles[tile_id]
            tile["matches"] = {}
            for tile_id2 in tiles:
                if tile_id2 in orientated_tiles:
                    continue
                tile2 = tiles[tile_id2]
                if not tile_id == tile_id2:
                    match = check_match(tile["image"], tile2["image"])
                    if match:
                        pos1, pos2, orientation = match
                        rotation_needed = (180 + pos1 - pos2) % 360
                        num_90_rots = rotation_needed // 90
                        for i in range(num_90_rots):
                            tile2["image"] = np.rot90(tile2["image"], -1)
                        if orientation == -1:
                            if pos1 in [0, 180]:
                                tile2["image"] = np.fliplr(tile2["image"])
                            else:
                                tile2["image"] = np.flipud(tile2["image"])
                        orientated_tiles.append(tile_id2)
                        new_orientated_tiles.append(tile_id2)
                        tile["matches"][pos1] = tile_id2

        last_orientated_tiles = new_orientated_tiles

    positioned_tile_ids = { list(tiles.keys())[0]: (50, 50) }
    last_positioned_tiles = list(positioned_tile_ids.keys())
    while last_positioned_tiles:
        new_positioned_tiles = []
        for tile_id in last_positioned_tiles:
            for pos, tile_id2 in tiles[tile_id]["matches"].items():
                if tile_id2 in positioned_tile_ids:
                    continue
                tile_pos = positioned_tile_ids[tile_id]
                if pos == 0:
                    tile_2_pos = (tile_pos[0], tile_pos[1] - 1)
                elif pos == 90:
                    tile_2_pos = (tile_pos[0] + 1, tile_pos[1])
                elif pos == 180:
                    tile_2_pos = (tile_pos[0], tile_pos[1] + 1)
                elif pos == 270:
                    tile_2_pos = (tile_pos[0] - 1, tile_pos[1])
                positioned_tile_ids[tile_id2] = tile_2_pos
                new_positioned_tiles.append(tile_id2)
        last_positioned_tiles = new_positioned_tiles

    min_lr = min([a[0] for a in positioned_tile_ids.values()])
    min_ud = min([a[1] for a in positioned_tile_ids.values()])
    for tile_id in positioned_tile_ids:
        old_pos = positioned_tile_ids[tile_id]
        positioned_tile_ids[tile_id] = (old_pos[0] - min_lr, old_pos[1] - min_ud)

    max_lr = max([a[0] for a in positioned_tile_ids.values()])
    max_ud = max([a[1] for a in positioned_tile_ids.values()])
    full_image = np.full(
        (
            (max_lr + 1) * list(tiles.values())[0]["image"].shape[0],
            (max_ud + 1) * list(tiles.values())[0]["image"].shape[1],
        ), "."
    )

    for tile_id, pos in positioned_tile_ids.items():
        full_image[pos[1] * 10 : 10 + pos[1] * 10, pos[0] * 10 : 10 + pos[0] * 10] = tiles[tile_id]["image"]

    full_image = np.delete(full_image, [10 * a for a in range(12)] + [10 * a - 1 for a in range(12)], axis=0)
    full_image = np.delete(full_image, [10 * a for a in range(12)] + [10 * a - 1 for a in range(12)], axis=1)

    monster_arr = np.array([list(a) for a in open("./monster.txt", "r").read().splitlines()])

    found_monster = False
    num_monsters = 0
    for rotation in range(4):
        if found_monster:
            break
        full_image = np.rot90(full_image)
        for flip in range(2):
            if found_monster:
                break
            full_image = np.fliplr(full_image)
            for i in range(full_image.shape[0] - monster_arr.shape[0]):
                for j in range(full_image.shape[1] - monster_arr.shape[1]):
                    if np.all(np.logical_or((monster_arr != "#"), (get_subarray(full_image, i, j, monster_arr.shape) == monster_arr))):
                        found_monster = True
                        num_monsters += 1

    num_hash = collections.Counter(full_image.flatten())["#"]
    num_hash_in_monster = collections.Counter(monster_arr.flatten())["#"]

    print(num_hash - num_monsters * num_hash_in_monster)
