from graphics import *
from cannon import InputDialog, ShotTracker
from button import Button

# EXERCISE 1
def exercise_1():
    win = GraphWin("Projectile Animation - Max Height", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    Line(Point(-10, 0), Point(210, 0)).draw(win)

    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    angle, vel, height = 45, 40, 2
    while True:
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()

        if choice == "Quit":
            break

        angle, vel, height = inputwin.get_values()
        shot = ShotTracker(win, angle, vel, height)

        while 0 <= shot.get_y() and -10 < shot.get_x() <= 210:
            shot.update(1/50)
            update(50)
        print(f"Max Height: {shot.get_max_height()}")
    win.close()

# EXERCISE 2
class StartStop:
    def __init__(self, win):
        # self.win = win = GraphWin("Buttons", 200, 300)
        # win.setCoords(0, 4.5, 4, 0.5)

        # self.start_button = Button(win, Point(1, 4), 1.25, 0.5, "Start")
        # self.start_button.activate()

        # self.stop_button = Button(win, Point(3, 4), 1.25, 0.5, "Stop")
        # self.stop_button.activate()
        self.win = win

        self.start_button = Button(win, Point(100, 100), 100, 50, "Start")
        self.start_button.activate()

        self.stop_button = Button(win, Point(200, 100), 100, 50, "Stop")
        self.stop_button.activate()

    def start(self, pt):
        if self.start_button.clicked(pt):
            return True
        
    def stop(self, pt):
        if self.stop_button.clicked(pt):
            return True

def exercise_2():
    win = GraphWin("Exercise 2 (4.1)", 500, 500)

    buttons = StartStop(win)
    pt = win.getMouse()

    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setOutline('red')
    shape.setFill('red')

    while True:
        if buttons.start(pt):
            p = win.getMouse()
            if buttons.stop(p):
                break
            cloned_shape = shape.clone()
            cloned_shape.draw(win)
            c = cloned_shape.getCenter()
            dx = p.getX() - c.getX()
            dy = p.getY() - c.getY()
            cloned_shape.move(dx, dy)
        elif buttons.stop(pt):
            break
        else:
            pt = win.getMouse()
    win.close()
exercise_2()