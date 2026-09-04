import sqlite3
import unittest

def get_course_registration():
    """Hämtar information om kursregistreringar från SQLite databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med student-ID och kurs-ID för varje kursregistrering.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    course_rows = cur_2.execute("SELECT * FROM Kursregistrering")
    return [{"student_id": r[0], "kurs_id": r[1]} for r in course_rows]


class CourseRegistration:
    """Representerar en kursregistrering som hämtats från databasen.
    Klassen innehåller studentens ID och kursens ID som attribut.
    """

    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    def get_student_id(self):
        """Metod som returnerar studentens ID."""
        return self.student_id

    def get_course_id(self):
        """Metod som returnerar kursens ID."""
        return self.course_id


def create_registration_objects():
    """Skapar CourseRegistration objekt utifrån informationen från databasen.
    :return: En lista med CourseRegistration objekt.
    """
    registration_objects = []
    for registration in get_course_registration():
        registration_object = CourseRegistration(
            student_id=registration["student_id"],
            course_id=registration["kurs_id"])
        registration_objects.append(registration_object)
    return registration_objects


class TestCourseReg(unittest.TestCase):
    """Testar att CourseRegistration-klassen skapar objekt med rätt student-ID och kurs-ID."""

    def test_student(self):
        """Kontrollerar att getters returnerar rätt student-ID och kurs-ID."""
        student = CourseRegistration(1, 1)
        self.assertEqual(student.get_student_id(), 1)
        self.assertEqual(student.get_course_id(), 1)


if __name__ == '__main__':
    unittest.main()