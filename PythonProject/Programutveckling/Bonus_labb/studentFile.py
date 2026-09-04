import sqlite3
import unittest

def get_students():
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    student_rows = cur_2.execute("SELECT * FROM Student")
    return [{"student_id": r[0], "name":r[1], "program_id":r[2]} for r in student_rows]

class Student:
    def __init__(self, student_id, name, program_id):
        self.student_id = student_id
        self.name = name
        self.program_id = program_id

    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_programe_id(self):
        return self.program_id

def create_student_objects():
    student_object_list = []
    for each_student in get_students():
        student_object = Student(
            student_id=each_student["student_id"],
            name=each_student["name"],
            program_id = each_student["program_id"])
        student_object_list.append(student_object)
    return student_object_list

class TestStudent(unittest.TestCase):
    """Testar att Student-klassen skapar objekt med rätt student-ID, namn och program-ID."""
    def test_student(self):
        """Kontrollerar att getters returnerar rätt student-ID, namn och program-ID."""
        student = Student(1, "Eleven", 1)
        self.assertEqual(student.get_student_id(), 1)
        self.assertEqual(student.get_name(), "Eleven")
        self.assertEqual(student.get_programe_id(), 1)

if __name__ == '__main__':
    unittest.main()