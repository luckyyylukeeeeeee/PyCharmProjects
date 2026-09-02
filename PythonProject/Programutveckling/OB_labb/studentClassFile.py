import sqlite3
import unittest

def get_students():
    con_1 = sqlite3.connect("medieteknik.sqlite")
    cur_1 = con_1.cursor()

    students_rows = cur_1.execute("SELECT * FROM Student")
    return [{"student_id": r[0], "name": r[1]} for r in students_rows]

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.name

def create_student_objects():
    student_object_list = []
    for each_student in get_students():
        student_object = Student(
            student_id=each_student["student_id"],
            name=each_student["name"])
        student_object_list.append(student_object)
    return student_object_list


class TestStudent(unittest.TestCase):
    def test_student(self):
        student = Student(7, "Dave")
        self.assertEqual(student.get_student_id(), 7)
        self.assertEqual(student.get_name(), "Dave")

if __name__ == '__main__':
    unittest.main()

