# 38:24

if __name__ == "__main__":
    f = open("./input.txt", "r")
    input = f.read().splitlines()
    player_1_pos = int(input[0][-1])
    player_2_pos = int(input[1][-1])

    player_positions = [player_1_pos, player_2_pos]

    scores = [0, 0]

    num_rolls = 0
    player_number = 0
    current_dice = 1
    while True:
        player_pos = player_positions[player_number]
        for roll in range(3):
            num_rolls += 1
            player_pos += current_dice
            player_pos = ((player_pos - 1) % 10) + 1
            current_dice += 1
            current_dice = ((current_dice - 1) % 100) + 1

        player_positions[player_number] = player_pos
        scores[player_number] += player_pos

        if scores[player_number] >= 1000:
            break
        
        player_number = 1 - player_number

    print(scores[1 - player_number] * num_rolls)

        


