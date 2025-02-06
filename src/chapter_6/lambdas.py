import random

health = xp = 10

def attempt2(action, min_roll, success_outcome, failure_outcome):
    global health, xp
    roll = random.randint(1, 20)
    
    if roll >= min_roll:
        print(f"{action} SUCCEEDED.")
        result = True
        health_change, xp_change = success_outcome
    else:
        print(f"{action} FAILED.")
        result = False
        health_change, xp_change = failure_outcome
    
    health += health_change
    xp += xp_change

    print(f"Health is now {health}")
    print(f"Experience is now {xp}")

    return result

def attempt(action, min_roll, outcome):
    global health, xp
    roll = random.randint(1, 20)
    
    if roll >= min_roll:
        print(f"{action} SUCCEEDED.")
        result = True
    else:
        print(f"{action} FAILED.")
        result = False
    scores = outcome(result)
    health = health + scores[0]
    print(f"Health is now {health}")
    xp = xp + scores[1]
    print(f"Experience is now {xp}")

    return result

attempt("Eating bread", 5,
        lambda success: (1, 0) if success else (-1, 0))
attempt2("Fighting ice weasel", 15, (0, 10), (-10, 5))