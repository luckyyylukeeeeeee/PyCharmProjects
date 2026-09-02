import sqlite3

def get_ob_courses():
    con = sqlite3.connect("eecs.sqlite")
    cur = con.cursor()
    classes_rows = cur.execute("SELECT * FROM Obligatoriska_kurser")
    return [{"kurs_id": r[0], "program_id": r[1]} for r in classes_rows]

programs = get_ob_courses()
print(programs)