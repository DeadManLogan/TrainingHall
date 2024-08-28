from random import random, randrange

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
        while (score_a < 15 or score_b < 15) and (abs(score_a - score_b) < 2):
            counter += 1
            winner = random()
            
            if counter % 2 != 0:
                if winner < team_a:
                    score_a += 1
            else:
                if winner < team_b:
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

    a, b, shut_a, shut_b = volleyball(games_n, team_a, team_b)
    
    print(f"Games: {games_n}")
    print(f"Player A: {a} ({a*100 / games_n})\nShutouts: {shut_a} ({shut_a*100 / a})")
    print(f"Player B: {b} ({b*100 / games_n})\nShutouts: {shut_b} ({shut_b*100 / b})")

# EXERCISE 4
def volleyball_rally(games_n, team_a, team_b):
    game_a = 0
    game_b = 0
    shut_a = shut_b = 0

    for i in range(games_n):
        counter = 0
        score_a = 0
        score_b = 0
        while (score_a < 25 or score_b < 25) and (abs(score_a - score_b) < 2):
            counter += 1
            winner = random()
            
            if counter % 2 != 0:
                if winner < team_a:
                    score_a += 1
            else:
                if winner < team_b:
                    score_b += 1
        if score_a == 25 and score_b == 0:
            shut_a += 1
        elif score_b == 25 and score_a == 0:
            shut_b += 1
        if score_a > score_b:
            game_a += 1
        else:
            game_b += 1
    return (game_a, game_b, shut_a, shut_b)

def exercise_4():
    team_a = float(input("Enter service probability of team A: "))
    team_b = float(input("Enter service probability of team B: "))
    games_n = int(input("Enter the number of games to simulate: "))

    a, b, shut_a, shut_b = volleyball_rally(games_n, team_a, team_b)
    
    print(f"Games: {games_n}")
    print(f"Player A: {a} ({a*100 / games_n})\nShutouts: {shut_a} ({shut_a*100 / a})")
    print(f"Player B: {b} ({b*100 / games_n})\nShutouts: {shut_b} ({shut_b*100 / b})")

# EXERCISE 5
def game_comparison(a, b, a_rally, b_rally):
    print(f"Regular A: {a}\nRally A: {a_rally}")
    print(f"Regular B: {b}\nRally B: {b_rally}")

def exercise_5():
    """
        To test the rally vs regular volleyball games we need
        to use the same input and then compare the results.
    """
    team_a = float(input("Enter service probability of team A: "))
    team_b = float(input("Enter service probability of team B: "))
    games_n = int(input("Enter the number of games to simulate: "))

    a, b, shut_a, shut_b = volleyball(games_n, team_a, team_b)
    a_rally, b_rally, shut_a_rally, shut_b_rally = volleyball_rally(games_n, team_a, team_b)

    team_a_percentage = a*100 / games_n
    team_b_percentage = b*100 / games_n
    team_a_rally_percentage = a_rally*100 / games_n
    team_b_rally_percentage = b_rally*100 / games_n

    game_comparison(team_a_percentage, team_b_percentage, team_a_rally_percentage, team_b_rally_percentage)

# EXERCISE 6
def table_tennis(games_n, team_a, team_b):
    game_a = 0
    game_b = 0
    shut_a = shut_b = 0

    for i in range(games_n):
        counter = 0
        score_a = 0
        score_b = 0
        while (score_a < 10 or score_b < 10) and (abs(score_a - score_b) < 2):
            counter += 1
            winner = random()
            
            if counter % 2 != 0:
                if winner < team_a:
                    score_a += 1
            else:
                if winner < team_b:
                    score_b += 1
        if score_a == 10 and score_b == 0:
            shut_a += 1
        elif score_b == 10 and score_a == 0:
            shut_b += 1
        if score_a > score_b:
            game_a += 1
        else:
            game_b += 1
    return (game_a, game_b, shut_a, shut_b)

def exercise_6():
    team_a = float(input("Enter service probability of team A: "))
    team_b = float(input("Enter service probability of team B: "))
    games_n = int(input("Enter the number of games to simulate: "))

    a, b, shut_a, shut_b = table_tennis(games_n, team_a, team_b)
    
    print(f"Games: {games_n}")
    print(f"Player A: {a} ({a*100 / games_n})\nShutouts: {shut_a} ({shut_a*100 / a})")
    print(f"Player B: {b} ({b*100 / games_n})\nShutouts: {shut_b} ({shut_b*100 / b})")

# EXERCISE 7
def roll_dices():
    roll = randrange(2, 13)
    return roll

def craps(games):
    lose_roll = [2, 3, 12]
    win_roll = [7, 11]
    wins = 0

    for i in range(games):
        roll = roll_dices()
        if roll in lose_roll:
            continue
        elif roll in win_roll:
            wins += 1
        else:
            while True:
                roll_point = roll_dices()
                if roll_point == 7:
                    break
                elif roll_point == roll:
                    wins += 1
                    break
    return wins

def exercise_7():
    games = int(input("Enter the number of simulated games: "))

    wins = craps(games)
    print(f"Your probability is: {wins/games}")

# EXERCISE 8
def blackjack():
    count_ten = [10, 11, 12, 13]
    has_ace = False
    points = 0

    while points < 17:
        card = randrange(1, 14)

        if card in count_ten:
            points += 10
        elif card == 1:
            points += 1
            has_ace = True
        else:
            points += card
        
        if has_ace and points > 21:
            points -= 10
            has_ace = False
    if points > 21:
        return True
    else:
        return False

def simulate_games(games):
    losses = 0
    for i in range(games):
        res = blackjack()
        if res:
            losses += 1
    return losses

def exercise_8():
    games = int(input("Enter the number of simulated games: "))

    losses = simulate_games(games)
    print(f"The probability of the dealer busting is: {losses/games}")

# EXERCISE 9
def blackjack(starting_points):
    count_ten = [10, 11, 12, 13]
    has_ace = False
    points = 0

    if starting_points in count_ten:
        points += 10
    elif starting_points == 1:
        points += 10
        has_ace = True
    else:
        points += starting_points

    while points < 17:
        card = randrange(1, 14)

        if card in count_ten:
            points += 10
        elif card == 1:
            points += 1
            has_ace = True
        else:
            points += card
        
        if has_ace and points > 21:
            points -= 10
            has_ace = False
    if points > 21:
        return True
    else:
        return False

def simulate_games(games, starting_points):
    losses = 0
    for i in range(games):
        res = blackjack(starting_points)
        if res:
            losses += 1
    return losses

def exercise_9():
    games = int(input("Enter the number of simulated games: "))

    for starting_points in range(1, 14):
        losses = simulate_games(games, starting_points)
        print(f"The probability of the dealer busting starting with {starting_points} is: {losses/games}")

exercise_9()