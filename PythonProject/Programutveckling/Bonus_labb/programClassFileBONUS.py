import unittest

class Program:
    """Representerar ett program som hämtats från databasen.
    Klassen innehåller programmets ID, namn och obligatoriska kurser.
    """

    def __init__(self, program_id, program_name):
        self.program_id = program_id
        self.program_name = program_name
        self.mandatory_courses = []

    def get_name(self):
        """Metod som returnerar programmets namn."""
        return self.program_name

    def get_program_id(self):
        """Metod som returnerar programmets ID."""
        return self.program_id

    def add_mandatory_course(self, course):
        """Lägger till en kurs som är obligatorisk för programmet."""
        self.mandatory_courses.append(course)

class TestProgramme(unittest.TestCase):
    """Testar att Program klassen skapar objekt med rätt program-ID och programnamn."""

    def test_student(self):
        """Kontrollerar att getters returnerar rätt program-ID och programnamn."""
        student = Program(2, "Datateknik")
        self.assertEqual(student.get_program_id(), 2)
        self.assertEqual(student.get_name(), "Datateknik")


if __name__ == '__main__':
    unittest.main()