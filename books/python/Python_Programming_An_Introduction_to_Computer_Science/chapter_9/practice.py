from random import random

def play_game(games_n, player_a, player_b):
    game_a = 0
    game_b = 0

    for i in range(games_n):
        serving = "A"
        score_a = 0
        score_b = 0
        while score_a < 15 or score_b < 15:
            winner = random()
            
            if serving == "A":
                if winner < player_a:
                    score_a += 1
                else:
                    serving = "B"
            else:
                if winner < player_b:
                    score_b += 1
                else:
                    serving = "A"
        if score_a > score_b:
            game_a += 1
        else:
            game_b += 1
    return (game_a, game_b)


def racquet():
    player_a = float(input("Enter service probability of player A: "))
    player_b = float(input("Enter service probability of player B: "))
    games_n = int(input("Enter the number of games to simulate: "))

    a, b = play_game(games_n, player_a, player_b)
    
    print(f"Games: {games_n}\nPlayer A: {a}\nPlayer B: {b}")
racquet()