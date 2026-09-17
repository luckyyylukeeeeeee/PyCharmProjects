import sqlite3

def get_students():
    """Hämtar information om studenter från SQLite-databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med student_id, namn och program_id för varje student.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    student_rows = cur_2.execute("SELECT * FROM Student")
    return [{"student_id": r[0], "name":r[1], "program_id":r[2]} for r in student_rows]

def get_program():
    """Hämtar information om program från SQLite databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med program-ID och programnamn för varje program.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    program_rows = cur_2.execute("SELECT * FROM Program")
    return [{"id": r[0], "program_name": r[1]} for r in program_rows]

def get_ob_course():
    """Hämtar information om obligatoriska kurser från SQLite databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med kurs-ID och program-ID för varje obligatorisk kurs.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    ob_course_rows = cur_2.execute("SELECT * FROM Obligatoriska_Kurser")
    return [{"kurs_id": r[0], "program_id": r[1]} for r in ob_course_rows]


def get_course_registration():
    """Hämtar information om kursregistreringar från SQLite databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med student-ID och kurs-ID för varje kursregistrering.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    course_rows = cur_2.execute("SELECT * FROM Kursregistrering")
    return [{"student_id": r[0], "kurs_id": r[1]} for r in course_rows]

def get_courses():
    """Hämtar information om kurser från SQLite databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med kurs-ID, kurskod, kursnamn och högskolepoäng för varje kurs.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    course_rows = cur_2.execute("SELECT * FROM Kurs")
    return [{"course_id": r[0], "course_code":r[1], "course_name":r[2], "hp":r[3]} for r in course_rows]