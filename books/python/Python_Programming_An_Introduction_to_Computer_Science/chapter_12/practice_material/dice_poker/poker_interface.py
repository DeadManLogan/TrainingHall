class TextInterface:
    def __init__(self):
        print("Welcome to video poker.")

    def set_money(self, amount):
        print(f"You currently have ${amount}")

    def set_dice(self, values):
        print(f"Dice: {values}")

    def want_to_play(self):
        ans = input("Do you want to continue to play? (y or n)")
        return ans[0] in "yY"
    
    def close(self):
        print("Thanks for playing.")

    def show_result(self, msg, score):
        print(f"{score}. You win ${score}.")

    def choose_dice(self):
        return eval(input("Enter list of which to change ([] to stop) "))