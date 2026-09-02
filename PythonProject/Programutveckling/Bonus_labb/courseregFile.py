import sqlite3

def get_course_reg():
    con = sqlite3.connect("eecs.sqlite")
    cur = con.cursor()
    classes_rows = cur.execute("SELECT * FROM Kursregistrering")
    return [{"student_id": r[0], "kurs_id": r[1]} for r in classes_rows]

course_reg = get_course_reg()
print(course_reg)