import unittest


class Student:
    """Representerar en student."""

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_student_id(self):
        """Returnerar studentens ID."""
        return self.student_id

    def get_name(self):
        """Returnerar studentens namn."""
        return self.name


class MediaStudent(Student):
    """Representerar en student på Medieteknik.
    MediaStudent är en subklass till Student och
    innehåller även en lista över studentens klarade kurser.
    """

    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.courses = []

    def add_course(self, course):
        """Lägger till en kurs som studenten har klarat."""
        self.courses.append(course)

    def get_courses(self):
        """Returnerar listan över studentens klarade kurser."""
        return self.courses


class TestStudent(unittest.TestCase):
    """Testar Student-klassen."""

    def test_student(self):
        """Kontrollerar att Student skapas med rätt information."""

        student = Student(7, "Dave")
        self.assertEqual(student.get_student_id(), 7)
        self.assertEqual(student.get_name(), "Dave")


class TestMediaStudent(unittest.TestCase):
    """Testar MediaStudent-klassen."""

    def test_media_student(self):
        """Kontrollerar att MediaStudent skapas korrekt."""

        student = MediaStudent(7, "Dave")

        self.assertEqual(student.get_student_id(), 7)
        self.assertEqual(student.get_name(), "Dave")
        self.assertEqual(student.get_courses(), [])

    def test_add_course(self):
        """Kontrollerar att en kurs kan läggas till."""

        student = MediaStudent(7, "Dave")

        student.add_course(8)

        self.assertEqual(student.get_courses(), [8])


if __name__ == '__main__':
    unittest.main()