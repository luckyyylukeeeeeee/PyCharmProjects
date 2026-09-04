import sqlite3
import unittest

def get_course_reg():
    """Hämtar information om kursregistreringar från SQLite-databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med student_id och kurs_id för varje kursregistrering.
    """
    con = sqlite3.connect("medieteknik.sqlite")
    cur = con.cursor()

    classes_rows = cur.execute("SELECT * FROM Kursregistrering")
    return [{"student_id": r[0], "kurs_id": r[1]} for r in classes_rows]


course_reg = get_course_reg()

class CourseRegistration:
    """Representerar en kursregistrering som hämtats från databasen.
    Klassen innehåller studentens ID och kursens ID som attribut.
    """
    def __init__(self, reg_student_id, reg_course_id):
        self.reg_student_id = reg_student_id
        self.reg_course_id = reg_course_id

    def get_reg_student_id(self):
        """Metod som returnerar studentens ID."""
        return self.reg_student_id

    def get_reg_course_id(self):
        """Metod som returnerar kursens ID."""
        return self.reg_course_id

def create_registration_objects():
    """Skapar CourseRegistration objekt utifrån informationen från databasen.
    :return: En lista med CourseRegistration objekt.
    """
    registration_objects = []
    for registration in course_reg:
        registration_object = CourseRegistration(
            reg_student_id=registration["student_id"],
            reg_course_id=registration["kurs_id"])
        registration_objects.append(registration_object)
    return registration_objects

class TestCourseReg(unittest.TestCase):
    """Testar att CourseRegistration-klassen skapar objekt med rätt student-ID och kurs-ID."""
    def test_student(self):
        """Kontrollerar att getters returnerar rätt student-ID och kurs-ID."""
        student = CourseRegistration(1, 8)
        self.assertEqual(student.get_reg_student_id(), 1)
        self.assertEqual(student.get_reg_course_id(), 8)

if __name__ == '__main__':
    unittest.main()