import sqlite3

def get_students():
    con_1 = sqlite3.connect("medieteknik.sqlite")
    cur_1 = con_1.cursor()

    students_rows = cur_1.execute("SELECT * FROM Student")
    return [{"student_id": r[0], "name": r[1]} for r in students_rows]

student_list = get_students()

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def print_info(self):
        print(self.student_id, self.name)

def create_student_objects():
    student_object_list = []
    for each_student in student_list:
        student_object = Student(
            student_id=each_student["student_id"],
            name=each_student["name"])
        student_object_list.append(student_object)
    return student_object_list





