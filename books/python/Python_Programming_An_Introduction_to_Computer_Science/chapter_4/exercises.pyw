from graphics import *
import random

def exercise_1():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        cloned_shape = shape.clone()
        cloned_shape.draw(win)
        c = cloned_shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        cloned_shape.move(dx, dy)
    
    message = Text(Point(100,100), 'Click again to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

def exercise_2():
    win = GraphWin('Exercise 2', 1000, 1000)

    first_circle = Circle(Point(500,500), 150)
    first_circle.setFill('white')
    first_circle.draw(win)

    circle_colors = ['black', 'blue', 'red', 'yellow']

    for i,color in enumerate(circle_colors):
        i += 1
        new_circle = Circle(first_circle.getCenter(), first_circle.getRadius() - (i*30))
        new_circle.setFill(color)
        new_circle.draw(win)

    win.getMouse()
    win.close()

def exerceise_3():
    win = GraphWin('Exercise 3', 500, 500)

    face = Circle(Point(250,250), 200)
    face.setFill('salmon')
    face.draw(win)

    left_eye = Oval(Point(175,200), Point(200,90))
    left_eye.setFill('black')
    left_eye.draw(win)

    right_eye = Oval(Point(300,200), Point(325,90))
    right_eye.setFill('black')
    right_eye.draw(win)

    win.getMouse()
    win.close()

def draw_die(value):
    background = Rectangle(Point(20, 20), Point(180, 180)) 

    if value == 1:
        number_1 = Circle(Point(100, 100), 10)
        return background, number_1
    elif value == 2:
        number_1 = Circle(Point(50, 50), 10)
        number_2 = Circle(Point(150, 150), 10)
        return background, number_1, number_2
    elif value == 3:
        number_1 = Circle(Point(100, 100), 10)
        number_2 = Circle(Point(50, 150), 10)
        number_3 = Circle(Point(150, 50), 10)
        return background, number_1, number_2, number_3
    elif value == 4:
        number_1 = Circle(Point(50, 50), 10)
        number_2 = Circle(Point(50, 150), 10)
        number_3 = Circle(Point(150, 50), 10)
        number_4 = Circle(Point(150, 150), 10)
        return background, number_1, number_2, number_3, number_4
    elif value == 5:
        number_1 = Circle(Point(50, 50), 10)
        number_2 = Circle(Point(50, 150), 10)
        number_3 = Circle(Point(150, 50), 10)
        number_4 = Circle(Point(150, 150), 10)
        number_5 = Circle(Point(100, 100), 10)
        return background, number_1, number_2, number_3, number_4, number_5
    else:
        number_1 = Circle(Point(50, 50), 10)
        number_2 = Circle(Point(50, 150), 10)
        number_3 = Circle(Point(150, 50), 10)
        number_4 = Circle(Point(150, 150), 10)
        number_5 = Circle(Point(50, 100), 10)
        number_6 = Circle(Point(150, 100), 10)
        return background, number_1, number_2, number_3, number_4, number_5, number_6


def exercise_5():
    win = GraphWin('Exercise 5', 200,200)

    for i in range(15):
        number = random.randint(1, 6)
        elements = draw_die(number)
        [element.draw(win) for element in elements]
        win.getMouse()
        [element.undraw() for element in elements]

    win.getMouse()
    win.close()

exercise_5()