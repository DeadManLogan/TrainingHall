import math

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

    best_student_obj = make_student(reader.readline())

    for line in reader:
        student_obj = make_student(line)

        if student_obj.gpa() > best_student_obj.gpa():
            best_student_obj = student_obj
    reader.close()

    print(f"Best sudent: {best_student_obj.get_name()}\nGPA: {best_student_obj.gpa()}\nCredits: {best_student_obj.get_hours()}")


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

best_student()

