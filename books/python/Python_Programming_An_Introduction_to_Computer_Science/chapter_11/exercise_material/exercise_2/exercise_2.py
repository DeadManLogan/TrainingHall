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
    filename = "chapter_11/exercise_material/exercise_2/students_2.txt"
    reader = open(filename, "r")
    students = []
    for (line) in reader:
        students.append(make_student(line))
    reader.close()
    return students

def write_studetns(students):
    filename = "chapter_11/exercise_material/exercise_2/output_2.txt"
    writer = open(filename, "w")
    for (s) in students:
        print(f"{s.get_name()}\n{s.get_hours()}\n{s.get_qpoints()}", file=writer)
    writer.close()

def use_gpa(a_student):
    return a_student.gpa()

def get_sorting_field(data):
    field = input("Choose the field to sort the students: gpa, name or credits.")

    while field.lower() not in ["gpa", "name", "credits"]:
        field = input("Choose the field to sort the students: gpa, name or credits.")

    if field == "gpa":
        data.sort(key=Student.gpa)
    elif field == "name":
        data.sort(key=Student.get_name)
    elif field == "credits":
        data.sort(key=Student.get_qpoints)
    
    return data

    
    
def main():
    data = read_students()
    result = get_sorting_field(data)
    write_studetns(result)

main()