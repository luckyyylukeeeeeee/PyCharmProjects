import unittest

class Course:
    """Representerar en kurs som hämtats från databasen.
    Klassen innehåller kursers ID, kurskod, kursnamn och antal hp som attribut.
    """
    def __init__(self, course_id, course_code, course_name,hp):
        self.course_id = course_id
        self.course_code = course_code
        self.course_name=course_name
        self.hp=hp

    def get_course_id(self):
        """Metod som returnerar course_id."""
        return self.course_id

    def get_course_code(self):
        """Metod som returnerar course_code."""
        return self.course_code

    def get_course_name(self):
        """Metod som returnerar course_name."""
        return self.course_name

    def get_hp(self):
        """Metod som returnerar kursen hp."""
        return self.hp

class TestStudent(unittest.TestCase):
    """Testar att Course klassen skapar objekt med rätt course_id, course_code, course_name och hp."""
    def test_student(self):
        """Kontrollera att getters returnerar rättinformation."""
        student = Course(1, "DM1581", "Introduktion till medieteknik", 6.0)
        self.assertEqual(student.get_course_id(), 1)
        self.assertEqual(student.get_course_code(), "DM1581")
        self.assertEqual(student.get_course_name(), "Introduktion till medieteknik")
        self.assertEqual(student.get_hp(), 6.0)

if __name__ == '__main__':
    unittest.main()

