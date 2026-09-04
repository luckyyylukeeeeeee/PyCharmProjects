import sqlite3
import unittest

def get_students():
    """Hämtar information om studenter från SQLite-databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med student_id, namn och program_id för varje student.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    student_rows = cur_2.execute("SELECT * FROM Student")
    return [{"student_id": r[0], "name":r[1], "program_id":r[2]} for r in student_rows]


class Student:
    """Representerar en student som hämtats från databasen.
    Klassen innehåller studentens ID, namn och program-ID som attribut.
    """
    def __init__(self, student_id, name, program_id):
        self.student_id = student_id
        self.name = name
        self.program_id = program_id

    def get_student_id(self):
        """Metod som returnerar studentens ID."""
        return self.student_id

    def get_name(self):
        """Metod som returnerar studentens namn."""
        return self.name

    def get_programe_id(self):
        """Metod som returnerar studentens program-ID."""
        return self.program_id

def create_student_objects():
    """Skapar Student objekt utifrån informationen från databasen.
    :return: En lista med Student objekt.
    """
    student_object_list = []
    for each_student in get_students():
        student_object = Student(
            student_id=each_student["student_id"],
            name=each_student["name"],
            program_id=each_student["program_id"])
        student_object_list.append(student_object)
    return student_object_list

class TestStudent(unittest.TestCase):
    """Testar att Student klassen skapar objekt med rätt student-ID, namn och program-ID."""
    def test_student(self):
        """Kontrollerar att getters returnerar rätt student-ID, namn och program-ID."""
        student = Student(1, "Eleven", 1)
        self.assertEqual(student.get_student_id(), 1)
        self.assertEqual(student.get_name(), "Eleven")
        self.assertEqual(student.get_programe_id(), 1)

if __name__ == '__main__':
    unittest.main()