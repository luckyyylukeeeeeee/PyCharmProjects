import sqlite3


def get_program():
    con = sqlite3.connect("eecs.sqlite")
    cur = con.cursor()
    classes_rows = cur.execute("SELECT * FROM Program")
    return [{"program_id": r[0], "program_namn": r[1]} for r in classes_rows]

programs = get_program()
print(programs)