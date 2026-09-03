import sqlite3

def get_course_registration():
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    course_rows = cur_2.execute("SELECT * FROM Kursregistrering")
    return [{"student_id": r[0], "kurs_id":r[1]} for r in course_rows]

class CourseRegistration:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    def get_student_id(self):
        return self.student_id

    def get_course_id(self):
        return self.course_id

def create_registration_objects():
    registration_objects = []
    for registration in get_course_registration():
        registration_object = CourseRegistration(
            student_id=registration["student_id"],
            course_id=registration["kurs_id"])
        registration_objects.append(registration_object)
    return registration_objects