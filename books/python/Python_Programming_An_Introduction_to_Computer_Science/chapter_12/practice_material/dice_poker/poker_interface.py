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
        self.add_dice_buttons(Point(300, 170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
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

    def show_result(self, msg, score):
        if score > 0:
            text = f"{msg}! You win {score}"
        else:
            text = f"You rolled {msg}"
        self.msg.setText(text)

    def set_dice(self, values):
        for i in range(5):
            self.dice[i].set_value(values[i])