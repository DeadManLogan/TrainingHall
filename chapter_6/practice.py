import math
from graphics import *

def square(x):
    return x**2

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def triangle():
    win = GraphWin("Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText(f"The perimeter is: {perim}")

    win.getMouse()
    win.close()

def happy():
    return "Happy Birthday to you. "

def song(name):
    lyrics = happy()*2 + f"Happy Birthday dear {name}. " + happy()
    return lyrics

def people_birthday():
    for p in ['Bob', 'Alice']:
        print(song(p))


def add_interest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    add_interest(amounts, rate)
    print(amounts)

test()