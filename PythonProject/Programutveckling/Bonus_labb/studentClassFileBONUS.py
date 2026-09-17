import unittest

class Student:
    """Representerar en student som hämtats från databasen.
    Klassen innehåller studentens ID och namn som attribut.
    """

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_name(self):
        """Metod som returnerar studentens namn."""
        return self.name

    def get_student_id(self):
        """Metod som returnerar studentens ID."""
        return self.student_id


class ProgramStudent(Student):
    """Representerar en student som är registrerad på ett program.
    Klassen ärver attributen från Student och innehåller även
    studentens program och kurser som studenten har läst.
    """

    def __init__(self, student_id, name, program):
        """Skapar en ProgramStudent med ID, namn och program."""
        super().__init__(student_id, name)
        self.program = program
        self.courses = []

    def add_course(self, course):
        """Lägger till en kurs som studenten har läst."""
        self.courses.append(course)

    def get_program_id(self):
        """Metod som returnerar studentens program-ID."""
        return self.program.get_program_id()


class TestStudent(unittest.TestCase):
    """Testar Student-klassen."""

    def test_student(self):
        """Kontrollerar att Student skapas med rätt information."""

        student = Student(7, "Dave")

        self.assertEqual(student.get_student_id(), 7)
        self.assertEqual(student.get_name(), "Dave")


class TestProgramStudent(unittest.TestCase):
    """Testar ProgramStudent-klassen."""

    def test_program_student(self):
        """Kontrollerar att ProgramStudent skapas korrekt."""

        student = ProgramStudent(7, "Dave", "Datateknik")

        self.assertEqual(student.get_student_id(), 7)
        self.assertEqual(student.get_name(), "Dave")
        self.assertEqual(student.program, "Datateknik")
        self.assertEqual(student.courses, [])

    def test_add_course(self):
        """Kontrollerar att en kurs kan läggas till."""

        student = ProgramStudent(7, "Dave", "Datateknik")

        student.add_course(8)

        self.assertEqual(student.courses, [8])


if __name__ == '__main__':
    unittest.main()