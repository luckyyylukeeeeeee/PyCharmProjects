import sqlite3
import unittest

def get_ob_course():
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    ob_course_rows = cur_2.execute("SELECT * FROM Obligatoriska_Kurser")
    return [{"kurs_id": r[0], "program_id":r[1]} for r in ob_course_rows]

class OC:
    def __init__(self, course_id, program_id):
        self.course_id = course_id
        self.program_id = program_id

    def get_info(self):
        return print(self.course_id,self.program_id)

    def get_course_id(self):
        return self.course_id

    def get_program_id(self):
        return self.program_id

def create_ob_course_objects():
    course_ob_list = []
    for each_course in get_ob_course():
        student_object = OC(
            course_id=each_course["kurs_id"],
            program_id=each_course["program_id"]
                            )
        course_ob_list.append(student_object)
    return course_ob_list

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