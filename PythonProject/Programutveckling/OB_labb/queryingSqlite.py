import sqlite3


def get_students():
    """Hämtar studentinformation från databasen."""
    con = sqlite3.connect("medieteknik.sqlite")
    cur = con.cursor()

    students_rows = cur.execute(
        "SELECT * FROM Student"
    )

    students = [
        {
            "student_id": row[0],
            "name": row[1]
        }
        for row in students_rows
    ]

    con.close()

    return students


def get_courses():
    """Hämtar kursinformation från databasen."""

    con = sqlite3.connect("medieteknik.sqlite")
    cur = con.cursor()

    courses_rows = cur.execute(
        "SELECT * FROM Kurs"
    )

    courses = [
        {
            "course_id": row[0],
            "course_code": row[1],
            "course_name": row[2],
            "hp": row[3]
        }
        for row in courses_rows
    ]

    con.close()

    return courses


def get_registrations():
    """Hämtar information om vilka kurser studenter klarat."""

    con = sqlite3.connect("medieteknik.sqlite")
    cur = con.cursor()

    registrations_rows = cur.execute(
        "SELECT student_id, kurs_id FROM Kursregistrering"
    )

    registrations = [
        {
            "student_id": row[0],
            "course_id": row[1]
        }
        for row in registrations_rows
    ]

    con.close()

    return registrations