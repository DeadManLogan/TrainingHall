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
        self.sphere_volume = 4/3 * math.pi * (self.radius ** 3)
        return self.sphere_volume

def exercise_9():
    radius = float(input("Enter the radius of the sphere: "))

    sphere = Sphere(radius)

    print(f"Area: {sphere.surface_area()}\nVolume: {sphere.volume()}")

# EXERCISE 10
class Cube:
    def __init__(self, side):
        self.side = side
    
    def get_side(self):
        return self.side
    
    def get_surface_area(self):
        self.area = 6 * (self.side ** 2)
        return self.area
    
    def get_volume(self):
        self.volume = self.side ** 3
        return self.volume

def exercise_10():
    side = float(input("Enter the side of the cube: "))
    cube = Cube(side)
    print(f"Area: {cube.get_surface_area()}\nVolume: {cube.get_volume()}")

# EXERCISE 11
class Card:
    def __init__(self, rank, suit):
        self.rank = int(rank)
        self.suit = suit

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def value(self):
        if self.rank < 11:
            return self.rank
        else:
            return 10
        
    def __str__(self):
        name = ""
        suit_name = ""
        if self.rank == 1:
            name = "Ace"
        elif self.rank == 11:
            name = "Jack"
        elif self.rank == 12:
            name = "Queen"
        elif self.rank == 13:
            name = "King"
        else:
            name = self.rank

        if self.suit == "d":
            suit_name = "Diamonds"
        elif self.suit == "c":
            suit_name = "Clubs"
        elif self.suit == "h":
            suit_name = "Hearts"
        else:
            suit_name = "Spades"

        return f"{name} of {suit_name}"
    
    def draw(self, win, center):
        suit_mapping = {
            'd': 'diamonds',
            'c': 'clubs',
            'h': 'hearts',
            's': 'spades'
        }
        suit_name = suit_mapping[self.suit]
        filename = f"chapter_10/exercise_material/{self.rank}_{suit_name}.ppm"
        card_image = Image(center, filename)
        card_image.draw(win)
        
def exercise_11():
    com = ""
    while com != "quit":
        rank = input("Enter the rank of the card: ")
        suit = input("Enter the suit d, c, h, s: ")

        card = Card(rank, suit)
        print(card)

        com = input("Type quit to quit: ")
    
# EXERCISE 12
def create_random_hand():
    suits = ['d', 'c', 'h', 's']
    ranks = list(range(1, 14))
    hand = []

    for _ in range(5):
        rank = random.choice(ranks)
        suit = random.choice(suits)
        hand.append(Card(rank, suit))
    
    return hand

def exercise_12():
    """
    I only put 3 cards. You can easily put the randomness in play, but you also
    need to manually import all 52 card assets. Feel free to use the create_random_hand
    function from above.
    """
    rank = input("Enter the rank of the card: ")
    suit = input("Enter the suit d, c, h, s: ")

    win = GraphWin("Card Hand", 800, 600)
    win.setBackground("white")

    card = Card(rank, suit)
    card.draw(win, Point(250, 300))

    win.getMouse()
    win.close()

# EXERCISE 15
def exercise_15():
    win = GraphWin("Exercise 15", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    Line(Point(-10, 0), Point(210, 0)).draw(win)

    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    angle, vel, height = 45, 40, 2
    inputwin = InputDialog(angle, vel, height)
    while True:
        choice = inputwin.interact()

        if choice == "Quit":
            break

        angle, vel, height = inputwin.get_values()
        shot = ShotTracker(win, angle, vel, height)

        while 0 <= shot.get_y() and -10 < shot.get_x() <= 210:
            shot.update(1/50)
            update(50)
        print(f"Max Height: {shot.get_max_height()}")
    win.close()

# EXERCISE 16
class Target:
    def __init__(self, win):
        self.p1 = Point(random.uniform(-8, 180), 0)
        self.p2 = Point(random.uniform(-6, 200), 3)
        random_num = random.uniform(1, 3)
        self.target = Rectangle(self.p1, self.p2)
        self.target.draw(win)

def exercise_16():
    win = GraphWin("Exercise 16", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    Line(Point(-10, 0), Point(210, 0)).draw(win)

    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)
    
    target = Target(win)

    angle, vel, height = 45, 40, 2
    inputwin = InputDialog(angle, vel, height)
    while True:
        choice = inputwin.interact()

        if choice == "Quit":
            break

        angle, vel, height = inputwin.get_values()
        shot = ShotTracker(win, angle, vel, height)

        while 0 <= shot.get_y() and -10 < shot.get_x() <= 210:
            shot.update(1/50)
            update(50)
        print(f"Max Height: {shot.get_max_height()}")
    win.close()

# EXERCISE 17
class Regression:
    def __init__(self):
        self.n = 0
        self.sum_x = 0
        self.sum_y = 0
        self.sum_x2 = 0
        self.sum_xy = 0

    def addPoint(self, x, y):
        self.n += 1
        self.sum_x += x
        self.sum_y += y
        self.sum_x2 += x ** 2
        self.sum_xy += x * y

    def slope(self):
        if self.n == 0:
            return 0
        return (self.n * self.sum_xy - self.sum_x * self.sum_y) / (self.n * self.sum_x2 - self.sum_x ** 2)

    def intercept(self):
        if self.n == 0:
            return 0
        return (self.sum_y - self.slope() * self.sum_x) / self.n

    def predict(self, x):
        return self.slope() * x + self.intercept()

def exercise_17():
    # Create a graphics window
    win = GraphWin("Regression Line Plotter", 600, 400)
    win.setBackground("white")

    # Draw the "Done" rectangle
    done_rect = Rectangle(Point(10, 10), Point(60, 30))
    done_rect.setFill("lightgray")
    done_rect.draw(win)
    done_text = Text(Point(35, 20), "Done")
    done_text.draw(win)

    # Create a Regression object
    regression = Regression()

    # Collect points until "Done" is clicked
    while True:
        click_point = win.getMouse()

        # Check if the click is inside the "Done" rectangle
        if (10 <= click_point.getX() <= 60) and (10 <= click_point.getY() <= 30):
            break

        # Add the point to the regression object
        regression.addPoint(click_point.getX(), click_point.getY())

        # Draw the point
        point_circle = Circle(click_point, 3)
        point_circle.setFill("blue")
        point_circle.setOutline("blue")
        point_circle.draw(win)

    # Calculate the regression line endpoints
    x_left = 0
    y_left = regression.predict(x_left)
    x_right = win.getWidth()
    y_right = regression.predict(x_right)

    # Draw the regression line
    regression_line = Line(Point(x_left, y_left), Point(x_right, y_right))
    regression_line.setOutline("red")
    regression_line.setWidth(2)
    regression_line.draw(win)

    # Wait for another click before closing
    win.getMouse()
    win.close()

exercise_17()