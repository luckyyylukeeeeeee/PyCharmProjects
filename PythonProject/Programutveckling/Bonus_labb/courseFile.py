import sqlite3

def get_courses():
    con = sqlite3.connect("eecs.sqlite")
    cur = con.cursor()
    classes_rows = cur.execute("SELECT * FROM Kurs")
    return [{"kurs_id": r[0], "kurskod": r[1] , "kursnamn":r[2], "hp":r[3]} for r in classes_rows]

course_reg = get_courses()
print(course_reg)