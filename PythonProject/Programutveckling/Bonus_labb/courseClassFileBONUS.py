import unittest


class Course:
    """Representerar en kurs som hämtats från databasen.
    Klassen innehåller kursens ID, namn och antal högskolepoäng.
    """

    def __init__(self, course_id, course_name, hp):
        self.course_id = course_id
        self.course_name = course_name
        self.hp = hp

    def get_course_id(self):
        """Metod som returnerar kursens ID."""
        return self.course_id

    def get_name(self):
        """Metod som returnerar kursens namn."""
        return self.course_name

    def get_hp(self):
        """Metod som returnerar kursens högskolepoäng."""
        return self.hp


class TestCourse(unittest.TestCase):
    """Testar att Course-klassen skapar objekt med rätt information."""

    def test_course(self):
        """Kontrollerar att getters returnerar rätt kurs-ID,
        kursnamn och högskolepoäng.
        """

        course = Course(1, "Envariabelanalys", 7.5)

        self.assertEqual(course.get_course_id(), 1)
        self.assertEqual(course.get_name(), "Envariabelanalys")
        self.assertEqual(course.get_hp(), 7.5)


if __name__ == '__main__':
    unittest.main()