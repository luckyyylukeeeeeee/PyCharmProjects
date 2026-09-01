from studentClassFile import Student, create_student_objects
from coursesClassFile import Course, create_course_objects


import sqlite3
def get_course_reg():
    con = sqlite3.connect("medieteknik.sqlite")
    cur = con.cursor()
    classes_rows = cur.execute("SELECT * FROM Kursregistrering")
    return [{"student_id": r[0], "kurs_id": r[1]} for r in classes_rows]

course_reg = get_course_reg()
print(course_reg)

class CourseRegistration:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

def create_registration_objects():
    registration_objects = []
    for registration in course_reg:
        registration_object = CourseRegistration(
            student_id=registration["student_id"],
            course_id=registration["kurs_id"])
        registration_objects.append(registration_object)
    return registration_objects













