from random import random

# EXERCISE 1
def play_game(games_n, player_a, player_b):
    game_a = 0
    game_b = 0

    for i in range(games_n):
        counter = 0
        score_a = 0
        score_b = 0
        while score_a < 15 or score_b < 15:
            counter += 1
            winner = random()
            
            if counter % 2 != 0:
                if winner < player_a:
                    score_a += 1
            else:
                if winner < player_b:
                    score_b += 1
        if score_a > score_b:
            game_a += 1
        else:
            game_b += 1
    return (game_a, game_b)
    
def exercise_1():
    player_a = float(input("Enter service probability of player A: "))
    player_b = float(input("Enter service probability of player B: "))
    games_n = int(input("Enter the number of games to simulate: "))

    a, b = play_game(games_n, player_a, player_b)
    
    print(f"Games: {games_n}\nPlayer A: {a} ({a*100 / games_n})\nPlayer B: {b} ({b*100 / games_n})")

# EXERCISE 2
def play_game_2(games_n, player_a, player_b):
    game_a = 0
    game_b = 0
    shut_a = shut_b = 0

    for i in range(games_n):
        counter = 0
        score_a = 0
        score_b = 0
        while score_a < 15 or score_b < 15:
            counter += 1
            winner = random()
            
            if counter % 2 != 0:
                if winner < player_a:
                    score_a += 1
            else:
                if winner < player_b:
                    score_b += 1
        if score_a == 15 and score_b == 0:
            shut_a += 1
        elif score_b == 15 and score_a == 0:
            shut_b += 1
        if score_a > score_b:
            game_a += 1
        else:
            game_b += 1
    return (game_a, game_b, shut_a, shut_b)
    
def exercise_2():
    player_a = float(input("Enter service probability of player A: "))
    player_b = float(input("Enter service probability of player B: "))
    games_n = int(input("Enter the number of games to simulate: "))

    a, b, shut_a, shut_b = play_game_2(games_n, player_a, player_b)
    
    print(f"Games: {games_n}")
    print(f"Player A: {a} ({a*100 / games_n})\nShutouts: {shut_a} ({shut_a*100 / a})")
    print(f"Player B: {b} ({b*100 / games_n})\nShutouts: {shut_b} ({shut_b*100 / b})")

# EXERCISE 3
def volleyball(games_n, team_a, team_b):
    game_a = 0
    game_b = 0
    shut_a = shut_b = 0

    for i in range(games_n):
        counter = 0
        score_a = 0
        score_b = 0
        while (score_a < 15 or score_b < 15) and (score_a >= score_b + 2 or score_b >= score_a + 2):
            counter += 1
            winner = random()
            
            if counter % 2 != 0:
                if winner < team_a:
                    score_a += 1
            else:
                if winner < teamm_b:
                    score_b += 1
        if score_a == 15 and score_b == 0:
            shut_a += 1
        elif score_b == 15 and score_a == 0:
            shut_b += 1
        if score_a > score_b:
            game_a += 1
        else:
            game_b += 1
    return (game_a, game_b, shut_a, shut_b)

def exercise_3():
    team_a = float(input("Enter service probability of team A: "))
    team_b = float(input("Enter service probability of team B: "))
    games_n = int(input("Enter the number of games to simulate: "))

    a, b, shut_a, shut_b = play_game_2(games_n, team_a, team_b)
    
    print(f"Games: {games_n}")
    print(f"Player A: {a} ({a*100 / games_n})\nShutouts: {shut_a} ({shut_a*100 / a})")
    print(f"Player B: {b} ({b*100 / games_n})\nShutouts: {shut_b} ({shut_b*100 / b})")
    
exercise_3()