from graphics import *
import time

def shapes():
    win = GraphWin('Shapes')

    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)

    label = Text(center, 'Red Circle')
    label.draw(win)

    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)

    line = Line(Point(20,30), Point(180, 165))
    line.draw(win)

    oval = Oval(Point(20, 150), Point(180, 199))
    oval.draw(win)

    time.sleep(5)
    win.close()

def eyes():
    win = GraphWin('Smiley Face')
    leftEye = Circle (Point (80 , 50) , 5)
    leftEye . setFill ('yellow')
    leftEye . setOutline ('red')
    rightEye = leftEye.clone()
    rightEye.move(20, 0)
    leftEye.draw(win), rightEye.draw(win)
    time.sleep(5)

eyes()

