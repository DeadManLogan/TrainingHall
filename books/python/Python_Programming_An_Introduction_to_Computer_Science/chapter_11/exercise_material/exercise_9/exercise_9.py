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
    filename = "chapter_11/exercise_material/exercise_9/students_9.txt"
    reader = open(filename, "r")
    students = []
    for (line) in reader:
        students.append(make_student(line))
    reader.close()
    return students

def gpa_sort(students):
    decorated = [(s.gpa(), s.get_name()) for s in students]
    decorated.sort()
    return [name for gpa, name in decorated]

def main():
    data = read_students()
    print(gpa_sort(data))

main()