import sqlite3
import unittest

def get_course_reg():
    con = sqlite3.connect("medieteknik.sqlite")
    cur = con.cursor()
    classes_rows = cur.execute("SELECT * FROM Kursregistrering")
    return [{"student_id": r[0], "kurs_id": r[1]} for r in classes_rows]

course_reg = get_course_reg()

class CourseRegistration:
    def __init__(self, reg_student_id, reg_course_id):
        self.reg_student_id = reg_student_id
        self.reg_course_id = reg_course_id

    def get_reg_student_id(self):
        return self.reg_student_id

    def get_reg_course_id(self):
        return self.reg_course_id

def create_registration_objects():
    registration_objects = []
    for registration in course_reg:
        registration_object = CourseRegistration(
            reg_student_id=registration["student_id"],
            reg_course_id=registration["kurs_id"])
        registration_objects.append(registration_object)
    return registration_objects


class TestCourseReg(unittest.TestCase):
    def test_student(self):
        student = CourseRegistration(1,8)
        self.assertEqual(student.get_reg_student_id(), 1)
        self.assertEqual(student.get_reg_course_id(), 8)

if __name__ == '__main__':
    unittest.main()










