from graphics import *
from button import Button
from die_view import DieView

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

    def choose_dice(self, choices):
        buttons = self.buttons
        for b in buttons:
            if b.get_label() in choices:
                b.activate()
            else:
                b.deactivate()

        while True:
            p = self.win.get_mouse()
            for b in buttons:
                if b.clicked(p):
                    return b.get_label()
                
class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300, 30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.create_dice(Point(300, 100), 75)
        self.buttons = []
        self.add_dice_button(Point(300, 170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        b = Button(self.win, Point(30, 375), 40, 30, "Help")
        self.buttons.append(b)
        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def create_dice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)
    
    def add_dice_button(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,6):
            label = f"Die {i}"
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def set_money(self, amount):
        self.money.setText(f"${amount}")

    def choose(self, choices):
        buttons = self.buttons
        for b in buttons:
            if b.get_label() in choices:
                b.activate()
            else:
                b.deactivate()

        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    if b.get_label() == "Help":
                        self.help()
                    else:
                        return b.get_label()

    def show_result(self, msg, score):
        if score > 0:
            text = f"{msg}! You win {score}"
        else:
            text = f"You rolled {msg}"
        self.msg.setText(text)

    def set_dice(self, values):
        for i in range(5):
            self.dice[i].set_value(values[i])

    def want_to_play(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"
    
    def choose_dice(self):
        choices = []
        while True:
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5", "Roll Dice", "Quit", "Help"])

            if b[0] == "D":
                i = int(b[4]) - 1
                if i in choices:
                    choices.remove(i)
                    self.dice[i].set_color("black")
                else:
                    choices.append(i)
                    self.dice[i].set_color("gray")
            else:
                for d in self.dice:
                    d.set_color("black")
                if b == "Score":
                    return []
                elif choices != []:
                    return choices
                
    def help(self):
        self.help_win = GraphWin("Help", 600, 400)
        self.help_win.setBackground("lightyellow")

        title = Text(Point(200, 20), "Game Rules & Payoff Table")
        title.setSize(18)
        title.setStyle("bold")
        title.draw(self.help_win)

        rules = [
            "Dice Poker Rules:",
            "1. Roll the dice up to 3 times.",
            "2. Choose which dice to keep after each roll.",
            "3. The objective is to form the best poker hand.",
            "",
            "Payoffs:",
            "  - Two Pairs: 5x",
            "  - Three of a Kind: 10x",
            "  - Full House: 15x",
            "  - Four of a Kind: 25x",
            "  - Straight: 50x",
            "  - Five of a Kind: 100x"
        ]

        y_offset = 60
        for line in rules:
            rule_text = Text(Point(200, y_offset), line)
            rule_text.draw(self.help_win)
            y_offset += 20

        self.help_win.getMouse()
        self.help_win.close()
                
    def close(self):
        self.win.close()