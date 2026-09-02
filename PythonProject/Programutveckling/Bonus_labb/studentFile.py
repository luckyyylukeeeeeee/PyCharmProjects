import sqlite3

def get_students():
    con = sqlite3.connect("eecs.sqlite")
    cur = con.cursor()
    classes_rows = cur.execute("SELECT * FROM Student")
    return [{"student_id": r[0], "kurs_id": r[1] , "program_id":r[2]} for r in classes_rows]

course_reg = get_students()
print(course_reg)