import sqlite3

def get_students():
    con_2 = sqlite3.connect("eecs-2.sqlite")
    cur_2 = con_2.cursor()
    student_rows = cur_2.execute("SELECT * FROM Student")
    return [{"id": r[0], "namn":r[1], "program_id":r[2]} for r in student_rows]

class Student:
    def __init__(self, student_id, name, program_id):
        self.student_id = student_id
        self.name = name
        self.program_id = program_id

def create_student_objects():
    student_object_list = []
    for each_student in get_students():
        student_object = Student(
            student_id=each_student["student_id"],
            name=each_student["name"],
            program_id = each_student["name"])
        student_object_list.append(student_object)
    return student_object_list