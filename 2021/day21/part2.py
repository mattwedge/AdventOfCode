# 38:24

import json
import numpy as np
from functools import lru_cache

@lru_cache(maxsize=None)
def calculate_num_wins(player_positions=json.dumps([0, 0]), player_scores=json.dumps([0, 0]), to_play=0):
    player_positions = json.loads(player_positions)
    player_scores = json.loads(player_scores)
    if player_scores[0] >= 21:
        return np.array([1, 0])
    if player_scores[1] >= 21:
        return np.array([0, 1])

    res = np.array([0, 0])
    # These are the counts of the number of ways to get 3, 4, ..., 9 from 3 dice rolls
    for total_roll, combos in enumerate([1, 3, 6, 7, 6, 3, 1]):
        total_roll += 3
        player_positions_copy = list(player_positions)
        player_positions_copy[to_play] = ((player_positions_copy[to_play] + total_roll - 1) % 10) + 1

        player_scores_copy = list(player_scores)
        player_scores_copy[to_play] += player_positions_copy[to_play]

        res += combos * calculate_num_wins(player_positions=json.dumps(player_positions_copy), player_scores=json.dumps(player_scores_copy), to_play=1 - to_play)

    return res

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read().splitlines()
    player_1_pos = int(input[0][-1])
    player_2_pos = int(input[1][-1])

    print(max(calculate_num_wins(player_positions=json.dumps([player_1_pos, player_2_pos]), player_scores=json.dumps([0, 0]), to_play=0)))
