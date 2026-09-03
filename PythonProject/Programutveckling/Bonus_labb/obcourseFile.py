import sqlite3

def get_ob_course():
    con_2 = sqlite3.connect("eecs-2.sqlite")
    cur_2 = con_2.cursor()
    ob_course_rows = cur_2.execute("SELECT * FROM Obligatoriska_Kurser")
    return [{"kurs_id": r[0], "program_id":r[1]} for r in ob_course_rows]

class OC:
    def __init__(self, course_id, program_id):
        self.course_id = course_id
        self.program_id = program_id

def create_ob_course_objects():
    course_ob_list = []
    for each_course in get_ob_course():
        student_object = OC(
            course_id=each_course["kurs_id"],
            program_id=each_course["program_id"]
                            )
        course_ob_list.append(student_object)
    return course_ob_list