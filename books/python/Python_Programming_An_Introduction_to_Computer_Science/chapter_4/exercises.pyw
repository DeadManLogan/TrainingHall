from graphics import *

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