import sqlite3

def get_courses():
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    course_rows = cur_2.execute("SELECT * FROM Kurs")
    return [{"course_id": r[0], "course_code":r[1], "course_name":r[2], "hp":r[3]} for r in course_rows]

class Course:
    def __init__(self, course_id, course_code, course_name, hp):
        self.course_id = course_id
        self.course_code = course_code
        self.course_name = course_name
        self.hp = hp

    def get_course_id(self):
        return self.course_id

    def get_hp(self):
        return self.hp


def create_course_objects():
    course_object_list = []
    for each_course in get_courses():
        course_object = Course(
            course_id=each_course["course_id"],
            course_code=each_course["course_code"],
            course_name=each_course["course_name"],
            hp=each_course["hp"]
        )
        course_object_list.append(course_object)
    return course_object_list
