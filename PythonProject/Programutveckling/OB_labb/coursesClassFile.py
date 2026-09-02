import sqlite3
import unittest

def get_classes():
    con_2 = sqlite3.connect("medieteknik.sqlite")
    cur_2 = con_2.cursor()
    classes_rows = cur_2.execute("SELECT * FROM Kurs")
    return [{"id": r[0], "course_code": r[1], "course_name": r[2], "hp": r[3]} for r in classes_rows]

course_list = get_classes()

class Course:
    def __init__(self, course_id, course_code, course_name,hp):
        self.course_id = course_id
        self.course_code = course_code
        self.course_name=course_name
        self.hp=hp

    def get_course_id(self):
        return self.course_id

    def get_course_code(self):
        return self.course_code

    def get_course_name(self):
        return self.course_name

    def get_hp(self):
        return self.hp

def create_course_objects():
    course_object_list = []
    for each_course in course_list:
        course_object = Course(
            course_id=each_course["id"],
            course_code=each_course["course_code"],
            course_name=each_course["course_name"],
            hp=each_course["hp"]
        )
        course_object_list.append(course_object)
    return course_object_list



class TestStudent(unittest.TestCase):
    def test_student(self):
        student = Course(1, "DM1581", "Introduktion till medieteknik", 6.0)
        self.assertEqual(student.get_course_id(), 1)
        self.assertEqual(student.get_course_code(), "DM1581")
        self.assertEqual(student.get_course_name(), "Introduktion till medieteknik")
        self.assertEqual(student.get_hp(), 6.0)

if __name__ == '__main__':
    unittest.main()
