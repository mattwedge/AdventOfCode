if __name__ == "__main__":
    player_hands = open("./input.txt", "r").read().split("\n\n")
    players = {}
    for i, hand in enumerate(player_hands):
        players[i] = [int(a) for a in hand.splitlines()[1:]]
    
    while players[0] and players[1]:
        c0 = players[0][0]
        c1 = players[1][0]
        players[0] = players[0][1:] + [c0, c1] if c0 > c1 else players[0][1:]
        players[1] = players[1][1:] + [c1, c0] if c1 > c0 else players[1][1:]

    winning_hand = [hand for hand in players.values() if hand][0]
    score = 0
    for i, card in enumerate(winning_hand[::-1]):
        score += (i+1) * card
    print(score)
