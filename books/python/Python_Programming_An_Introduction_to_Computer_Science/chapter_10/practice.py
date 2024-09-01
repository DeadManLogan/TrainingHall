import math
from graphics import *

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def get_name(self):
        return self.name
    
    def get_hours(self):
        return self.hours
    
    def get_qpoints(self):
        return self.qpoints
    
    def gpa(self):
        return self.qpoints / self.hours
    
def make_student(info):
    info = info.split("    ")
    return Student(info[0], info[1], info[2])
    
def best_student():
    reader = open("chapter_10/practice_material/students.txt", "r")

    best_students = []
    best_gps = 0.0

    for (line) in reader:
        student_obj = make_student(line)
        student_gpa = student_obj.gpa()

        if len(best_students) == 0 or student_gpa > best_gpa:
            # we create a new list with the current top student
            best_students = [student_obj]
            best_gpa = student_gpa
        elif student_gpa == best_gpa:
            best_students.append(student_obj)
    
    reader.close()

    for i in best_students:
        print(f"Best student: {i.get_name()}\nGPA: {i.gpa()}\nCredits: {i.get_hours()}")

class Projectile:
    def __init__(self, angle, velocity, height):
        self.x_pos = 0.0
        self.y_pos = height
        theta = math.radians(angle)
        self.x_vel = velocity * math.cos(theta)
        self.y_vel = velocity * math.sin(theta)

    def get_x(self):
        return self.x_pos
    
    def get_y(self):
        return self.y_pos
    
    def update(self, time):
        self.x_pos += time * self.x_vel
        y_vel1 = self.y_vel - time * 9.8
        self.y_pos += time * (self.y_vel + y_vel1) / 2.0
        self.y_vel = y_vel1

def cannonball():
    angle = float(input("Enter the angle of the cannon: "))
    vel = float(input("Enter the initial velocity: "))
    time = float(input("Enter the time interval between calculations: "))
    h0 = float(input("Enter the initial height: "))

    c_ball = Projectile(angle, vel, h0)
    while c_ball.get_y() >= 0:
        c_ball.update(time)
    print(c_ball.get_x())


class Button:
    def __init__(self, win, center, width, height, label):
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def get_label(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, p):
        return(self.active and 
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)


