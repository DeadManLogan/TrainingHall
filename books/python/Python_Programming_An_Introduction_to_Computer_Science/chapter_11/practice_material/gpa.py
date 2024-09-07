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
    filename = "chapter_11/practice_material/students.txt"
    reader = open(filename, "r")
    students = []
    for (line) in reader:
        students.append(make_student(line))
    reader.close()
    return students

def write_studetns(students):
    filename = "output.txt"
    writer = open(filename, "w")
    for (s) in students:
        print(f"{s.get_name()}\n{s.get_hours()}\n{s.get_qpoints()}", file=writer)
    writer.close()

def use_gpa(a_student):
    return a_student.gpa()
    
def best_student():
    reader = open("chapter_10/practice_material/students.txt", "r")

    best_students = []

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