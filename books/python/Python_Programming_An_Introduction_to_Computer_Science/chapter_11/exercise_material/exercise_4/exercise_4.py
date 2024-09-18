from graphics import *
from button import Button
class InputDialog:
    def __init__(self):
        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0, 4.5, 4, 0.5)

        self.gpa_asc = Button(win, Point(1, 1), 1.75, 0.5, "GPA ASC")
        self.gpa_asc.activate()
        self.gpa_desc = Button(win, Point(3, 1), 1.75, 0.5, "GPA DESC")
        self.gpa_desc.activate()

        self.name_asc = Button(win, Point(1, 2), 1.75, 0.5, "NAME ASC")
        self.name_asc.activate()
        self.name_desc = Button(win, Point(3, 2), 1.75, 0.5, "NAME DESC")
        self.name_desc.activate()

        self.credits_asc = Button(win, Point(1, 3), 1.75, 0.5, "CRED ASC")
        self.credits_asc.activate()
        self.credits_desc = Button(win, Point(3, 3), 1.75, 0.5, "CRED DESC")
        self.credits_desc.activate()

        self.quit = Button(win, Point(2, 4), 1.25, 0.5, "Quit")
        self.quit.activate()

    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit", ""
            if self.gpa_asc.clicked(pt):
                return "gpa", "asc"
            if self.gpa_desc.clicked(pt):
                return "gpa", "desc"
            if self.name_asc.clicked(pt):
                return "name", "asc"
            if self.name_desc.clicked(pt):
                return "name", "desc"
            if self.credits_asc.clicked(pt):
                return "credits", "asc"
            if self.credits_desc.clicked(pt):
                return "credits", "desc"
    
    def get_values(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a, v, h
    
    def close(self):
        self.win.close()

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

def read_students():
    filename = "chapter_11/exercise_material/exercise_4/students_4.txt"
    reader = open(filename, "r")
    students = []
    for (line) in reader:
        students.append(make_student(line))
    reader.close()
    return students

def write_students(students):
    filename = "chapter_11/exercise_material/exercise_4/output_4.txt"
    writer = open(filename, "w")
    for (s) in students:
        print(f"{s.get_name()}\n{s.get_hours()}\n{s.get_qpoints()}", file=writer)
    writer.close()

def use_gpa(a_student):
    return a_student.gpa()

def get_sorting_field(data, field, order):
    if field == "gpa":
        key_func = Student.gpa
    elif field == "name":
        key_func = Student.get_name
    elif field == "credits":
        key_func = Student.get_qpoints

    if order.lower() == "asc":
        data.sort(key=key_func)
    else:
        data.sort(key=key_func, reverse=True)
    
    return data
    
    
def main():
    data = read_students()

    while True:
        inputwin = InputDialog()
        field, order = inputwin.interact()
        inputwin.close()

        result = get_sorting_field(data, field, order)
        write_students(result)

        if field == "Quit":
            break

main()