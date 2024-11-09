from random import randrange
from graphics import *
from button import Button
from die_view import DieView

def main():
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    roll_button = Button(win, Point(5.4, 5), 6, 1, "Roll Dice")
    roll_button.activate()
    quit_button = Button(win, Point(5, 1), 2, 1, "Quit")

    pt = win.getMouse()
    while not quit_button.clicked(pt):
        if roll_button.clicked(pt):
            value1 = randrange(1, 7)
            die1.set_value(value1)
            value2 = randrange(1, 7)
            die2.set_value(value2)
            quit_button.activate()
        pt = win.getMouse()
    win.close()

main()
    