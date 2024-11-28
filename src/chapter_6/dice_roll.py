import random

def roll_dice(sides, dice=1):
    return tuple(random.randint(1, sides) for _ in range(dice))

print("Roll for initiative...")

result, = roll_dice(20)
print(result)

# if player1 >= player2:
#     print("Player 1")
# else:
#     print("Player 2")
