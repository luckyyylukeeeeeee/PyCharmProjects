import sqlite3
import unittest

def get_ob_course():
    """Hämtar information om obligatoriska kurser från SQLite databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med kurs-ID och program-ID för varje obligatorisk kurs.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    ob_course_rows = cur_2.execute("SELECT * FROM Obligatoriska_Kurser")
    return [{"kurs_id": r[0], "program_id": r[1]} for r in ob_course_rows]


class OC:
    """Representerar en obligatorisk kurs som hämtats från databasen.
    Klassen innehåller kursens ID och program-ID som attribut.
    """

    def __init__(self, course_id, program_id):
        self.course_id = course_id
        self.program_id = program_id

    def get_info(self):
        """Metod som skriver ut kursens ID och program-ID."""
        return print(self.course_id, self.program_id)

    def get_course_id(self):
        """Metod som returnerar kursens ID."""
        return self.course_id

    def get_program_id(self):
        """Metod som returnerar program-ID."""
        return self.program_id


def create_ob_course_objects():
    """Skapar Ob kurs objekt utifrån informationen från databasen.
    :return: En lista med Ob kurs objekt.
    """
    course_ob_list = []
    for each_course in get_ob_course():
        student_object = OC(
            course_id=each_course["kurs_id"],
            program_id=each_course["program_id"]
        )
        course_ob_list.append(student_object)
    return course_ob_list


class TestStudent(unittest.TestCase):
    """Testar att Ob kurs klassen skapar objekt med rätt kurs-ID och program-ID."""

    def test_student(self):
        """Kontrollerar att getters returnerar rätt kurs-ID och program-ID."""
        student = OC(1, 1)
        self.assertEqual(student.get_course_id(), 1)
        self.assertEqual(student.get_program_id(), 1)


if __name__ == '__main__':
    unittest.main()