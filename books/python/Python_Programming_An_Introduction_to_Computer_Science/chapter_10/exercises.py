from graphics import *
import random
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

# EXERCISE 3
class DoorButtons:
    def __init__(self, win):
        self.win = win

        self.door1 = Button(win, Point(2, 8), 2, 2, "Door 1")
        self.door1.activate()

        self.door2 = Button(win, Point(5, 8), 2, 2, "Door 2")
        self.door2.activate()

        self.door3 = Button(win, Point(8, 8), 2, 2, "Door 3")
        self.door3.activate()

        self.winner = random.randint(0, 2)
        self.wins = self.losses = 0

    def won(self):
        self.wins += 1

    def lost(self):
        self.losses += 1
    
    def score(self):
        return self.wins, self.losses
    
    def pick_door(self):
        self.winner = random.randint(0, 2)
    
    def get_winning_door(self):
        if self.winner == 0:
            return "Door 1"
        if self.winner == 1:
            return "Door 2"
        if self.winner == 2:
            return "Door 3"

    def interact(self, pt):
        if self.door1.clicked(pt):
            return "Door 1"
        if self.door2.clicked(pt):
            return "Door 2"
        if self.door3.clicked(pt):
            return "Door 3"

def exercise_3():
    win = GraphWin("Exercise 3", 500, 500)
    win.setCoords(0, 0, 10, 10)

    buttons = DoorButtons(win)
    pt = win.getMouse()
    clicked_door = ""

    while True:
        if buttons.interact(pt) == "Door 1":
            clicked_door = "Door 1"
            break
        elif buttons.interact(pt) == "Door 2":
            clicked_door = "Door 2"
            break
        elif buttons.interact(pt) == "Door 3":
            clicked_door = "Door 3"
            break
        else:
            pt = win.getMouse()

    if buttons.get_winning_door() == clicked_door:
        result = Text(Point(5, 3), "You won!!")
        result.draw(win)
    else:
        result = Text(Point(5, 3), f"You lost...{buttons.get_winning_door()} was the right one.")
        result.draw(win)
            
    win.getMouse()
    win.close()

# EXERCISE 4
class QuitButton:
    def __init__(self, win):
        self.win = win

        self.quit_button = Button(win, Point(5, 5), 2, 2, "Quit")
        self.quit_button.activate()

    def quit(self, pt):
        if self.quit_button.clicked(pt):
            return True


def get_door(win, buttons, pt, quit):
    while True:
        if buttons.interact(pt) == "Door 1":
            return "Door 1"
        elif buttons.interact(pt) == "Door 2":
            return "Door 2"
        elif buttons.interact(pt) == "Door 3":
            return "Door 3"
        elif quit:
            win.close()
        else:
            pt = win.getMouse()

def exercise_4():
    win = GraphWin("Exercise 3", 500, 500)
    win.setCoords(0, 0, 10, 10)

    buttons = DoorButtons(win)
    quit = QuitButton(win)
    pt = win.getMouse()

    while not quit.quit(pt):
        clicked_door = get_door(win, buttons, pt, quit.quit(pt))

        if buttons.get_winning_door() == clicked_door:
            result = Text(Point(5, 3), "You won!!")
            result.draw(win)
            buttons.won()
        else:
            result = Text(Point(5, 3), f"You lost...{buttons.get_winning_door()} was the right one.")
            result.draw(win)
            buttons.lost()
        pt = win.getMouse()
        buttons.pick_door()
        result.undraw()

    wins, losses = buttons.score()
    score = Text(Point(5, 2), f"Wins: {wins}\nLosses: {losses}")
    score.draw(win)

    win.getMouse()
    win.close()

exercise_4()