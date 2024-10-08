from dice import Dice

class PokerApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.want_to_play():
            self.play_round()
        self.interface.close()

    def play_round(self):
        self.money -= 10
        self.interface.set_money(self.money)
        self.do_rolls()
        result, score = self.dice.score()
        self.interface.show_result(result, score)
        self.money += score
        self.interface.set_money(self.money)

    def do_rolls(self):
        self.dice.roll_all()
        rolls = 1
        self.interface.set_dice(self.dice.values())
        to_roll = self.interface.choose_dice()
        while rolls < 3 and to_roll != []:
            self.dice.roll(to_roll)
            rolls += 1
            self.interface.set_dice(self.dice.values())

            if rolls < 3:
                to_roll = self.interface.choose_dice()