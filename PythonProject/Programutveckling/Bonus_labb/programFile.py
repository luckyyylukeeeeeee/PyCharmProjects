import sqlite3
import unittest

def get_program():
    """Hämtar information om program från SQLite databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med program-ID och programnamn för varje program.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    program_rows = cur_2.execute("SELECT * FROM Program")
    return [{"id": r[0], "program_name": r[1]} for r in program_rows]


class Program:
    """Representerar ett program som hämtats från databasen.
    Klassen innehåller programmets ID och namn som attribut.
    """

    def __init__(self, program_id, program_name):
        self.program_id = program_id
        self.program_name = program_name

    def get_name(self):
        """Metod som returnerar programmets namn."""
        return self.program_name

    def get_program_id(self):
        """Metod som returnerar programmets ID."""
        return self.program_id


def create_program_objects():
    """Skapar Program objekt utifrån informationen från databasen.
    :return: En lista med Program objekt.
    """
    program_object_list = []
    for each_program in get_program():
        program_object = Program(
            program_id=each_program["id"],
            program_name=each_program["program_name"])
        program_object_list.append(program_object)
    return program_object_list


class TestProgramme(unittest.TestCase):
    """Testar att Program klassen skapar objekt med rätt program-ID och programnamn."""

    def test_student(self):
        """Kontrollerar att getters returnerar rätt program-ID och programnamn."""
        student = Program(2, "Datateknik")
        self.assertEqual(student.get_program_id(), 2)
        self.assertEqual(student.get_name(), "Datateknik")


if __name__ == '__main__':
    unittest.main()