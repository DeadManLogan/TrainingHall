from graphics import *
import math
import random
from cannon import InputDialog, ShotTracker
from button import Button
from exercise_material.cbutton import CButton
from die_view import DieView, DieView2

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

# EXERCISE 5
class Student:
    def __init__(self, name, hours=0, qpoints=0):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def get_name(self):
        return self.name
    
    def get_hours(self):
        return self.hours
    
    def get_qpoints(self):
        return self.qpoints
    
    def add_grade(self, grade_points, credits):
        self.hours += grade_points
        self.qpoints += grade_points * credits
    
    def gpa(self):
        return self.qpoints / self.hours

def exercise_5():
    name = "Bob, B"
    student = Student(name)

    while True:
        grade_points = float(input("Enter grade points (or -1 to quit): "))
        if grade_points == -1:
            break
        credits = float(input("Enter credits: "))
        student.add_grade(grade_points, credits)

    print(f"GPA for {student.get_name()}: {student.gpa()}")

# EXERCISE 6
class Student2:
    def __init__(self, name, hours=0, qpoints=0):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def get_name(self):
        return self.name
    
    def get_hours(self):
        return self.hours
    
    def get_qpoints(self):
        return self.qpoints
    
    def add_grade(self, grade_points, credits):
        self.hours += grade_points
        self.qpoints += grade_points * credits
    
    def gpa(self):
        return self.qpoints / self.hours
    
    def add_letter_grade(self, letterGrade, credits):
        grade_points = self.get_grade_points(letterGrade)
        if grade_points is not None:
            self.add_grade(grade_points, credits)
        else:
            print(f"Invalid letter grade: {letterGrade}")

    def get_grade_points(self, letterGrade):
        grade_mapping = {
            'A': 4.0,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3.0,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2.0,
            'C-': 1.7,
            'D+': 1.3,
            'D': 1.0,
            'D-': 0.7,
            'F': 0.0
        }
        return grade_mapping.get(letterGrade.upper(), None)

def exercise_6():
    name = "Bob, B"
    student = Student2(name)

    while True:
        letter_grade = input("Enter grade points (or quit): ")
        if letter_grade.lower() == "quit":
            break
        credits = float(input("Enter credits: "))
        student.add_letter_grade(letter_grade, credits)

    print(f"GPA for {student.get_name()}: {student.gpa()}")

# EXERCISE 7
def click(win, roll_button, quit_button):
    pt = win.getMouse()
    roll_button.get_distance(pt)
    quit_button.get_distance(pt)

def exercise_7():
    win = GraphWin("Exercise 7", 400, 400)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    roll_button = CButton(win, Point(5, 4.5), 1.5, "Roll Dice")
    roll_button.activate()
    quit_button = CButton(win, Point(5, 1), 1, "Quit")

    click(win, roll_button, quit_button)
    while not quit_button.clicked():
        if roll_button.clicked():
            value1 = random.randrange(1, 7)
            die1.set_value(value1)
            value2 = random.randrange(1, 7)
            die2.set_value(value2)
            quit_button.activate()
        click(win, roll_button, quit_button)
    win.close()

# EXERCISE 8
def random_color():
    return color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def exercise_8():
    win = GraphWin("Exercise 8", 400, 400)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    die1 = DieView2(win, Point(3, 7), 2)
    die2 = DieView2(win, Point(7, 7), 2)
    roll_button = CButton(win, Point(5, 4.5), 1.5, "Roll Dice")
    roll_button.activate()
    quit_button = CButton(win, Point(5, 1), 1, "Quit")

    click(win, roll_button, quit_button)
    while not quit_button.clicked():
        if roll_button.clicked():
            value1 = random.randrange(1, 7)
            die1.set_value(value1)
            die1.set_color(random_color())
            value2 = random.randrange(1, 7)
            die2.set_value(value2)
            die2.set_color(random_color())
            quit_button.activate()
        click(win, roll_button, quit_button)
    win.close()

# EXERCISE 9
class Sphere:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def surface_area(self):
        self.area = 4 * math.pi * (self.radius ** 2)
        return self.area
    
    def volume(self):
        self.volume = 4/3 * math.pi * (self.radius ** 3)
        return self.volume

def exercise_9():
    radius = float(input("Enter the radius of the sphere: "))

    sphere = Sphere(radius)

    print(f"Area: {sphere.surface_area()}\nVolume: {sphere.volume()}")

exercise_9()