def hash_players(players):
    return "-".join([str(i) for i in players[0]]) + "^" + "-".join([str(i) for i in players[1]])

def play_game(players):
    saved_positions = set()
    while players[0] and players[1]:
        if hash_players(players) in saved_positions:
            return 0, players[0]

        saved_positions.add(hash_players(players))
        c0 = players[0][0]
        c1 = players[1][0]
        if ((c0 > len(players[0]) - 1) or (c1 > len(players[1]) - 1)):
            round_winner = 0 if c0 > c1 else 1
        else:
            round_winner, _ = play_game({
                0: players[0][1: 1 + c0],
                1: players[1][1: 1 + c1]
            })

        players[0] = players[0][1:] + [c0, c1] if round_winner == 0 else players[0][1:]
        players[1] = players[1][1:] + [c1, c0] if round_winner == 1 else players[1][1:]

    return [a for a in players.items() if a[1]][0]

if __name__ == "__main__":
    player_hands = open("./input.txt", "r").read().split("\n\n")
    players = {}
    for i, hand in enumerate(player_hands):
        players[i] = [int(a) for a in hand.splitlines()[1:]]

    score = 0
    for i, card in enumerate(play_game(players)[1][::-1]):
        score += (i+1) * card
    print(score)
