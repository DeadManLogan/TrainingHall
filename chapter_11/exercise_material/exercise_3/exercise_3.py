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
    filename = "chapter_11/exercise_material/exercise_3/students_3.txt"
    reader = open(filename, "r")
    students = []
    for (line) in reader:
        students.append(make_student(line))
    reader.close()
    return students

def write_studetns(students):
    filename = "chapter_11/exercise_material/exercise_3/output_3.txt"
    writer = open(filename, "w")
    for (s) in students:
        print(f"{s.get_name()}\n{s.get_hours()}\n{s.get_qpoints()}", file=writer)
    writer.close()

def use_gpa(a_student):
    return a_student.gpa()

def get_sorting_field(data):
    field = input("Choose the field to sort the students: gpa, name or credits.")
    while (field.lower() not in ["gpa", "name", "credits"]):
        field = input("Choose the field to sort the students: gpa, name or credits.")

    order = input("Enter asc or desc for the order: ")
    while (order.lower() not in ["asc", "desc"]):
        order = input("Enter asc or desc for the order: ")

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
    result = get_sorting_field(data)
    write_studetns(result)

main()