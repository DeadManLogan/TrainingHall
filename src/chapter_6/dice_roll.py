import random

def roll_dice(sides, dice=1):
    return tuple(random.randint(1, sides) for _ in range(dice))

def variadic_roll_dice(*dice):
    if dice:
        roll = random.randint(1, dice[0])
        return (roll,) + variadic_roll_dice(*dice [1:])
    return()

def keyword_only_roll_dice(*, sides=6, dice=1):
    return tuple(random.randint(1, sides) for _ in range(dice))

print("Roll for initiative...")

result = keyword_only_roll_dice(sides=4, dice=2)
print(result)

# result = roll_dice(20)
# print(result)

# result = variadic_roll_dice(20, 4)
# print(callable(result))