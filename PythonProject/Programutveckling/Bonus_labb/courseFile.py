import sqlite3
import unittest

def get_courses():
    """Hämtar information om kurser från SQLite databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med kurs-ID, kurskod, kursnamn och högskolepoäng för varje kurs.
    """
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    course_rows = cur_2.execute("SELECT * FROM Kurs")
    return [{"course_id": r[0], "course_code":r[1], "course_name":r[2], "hp":r[3]} for r in course_rows]


class Course:
    """Representerar en kurs som hämtats från databasen.
    Klassen innehåller kursens ID, kurskod, kursnamn och högskolepoäng som attribut.
    """

    def __init__(self, course_id, course_code, course_name, hp):
        self.course_id = course_id
        self.course_code = course_code
        self.course_name = course_name
        self.hp = hp

    def get_course_id(self):
        """Metod som returnerar kursens ID."""
        return self.course_id

    def get_course_name(self):
        """Metod som returnerar kursens namn."""
        return self.course_name

    def get_course_code(self):
        """Metod som returnerar kursens kod."""
        return self.course_code

    def get_hp(self):
        """Metod som returnerar kursens högskolepoäng."""
        return self.hp


def create_course_objects():
    """Skapar Course objekt utifrån informationen från databasen.
    :return: En lista med Course-objekt.
    """
    course_object_list = []
    for each_course in get_courses():
        course_object = Course(
            course_id=each_course["course_id"],
            course_code=each_course["course_code"],
            course_name=each_course["course_name"],
            hp=each_course["hp"]
        )
        course_object_list.append(course_object)
    return course_object_list


class TestCourse(unittest.TestCase):
    """Testar att Course klassen skapar objekt med rätt kurs-ID, kurskod, kursnamn och högskolepoäng."""

    def test_student(self):
        """Kontrollerar att getters returnerar rätt kurs-ID, kurskod, kursnamn och högskolepoäng."""
        student = Course(1, "SF1624", "Envariabelanalys", 7.5)
        self.assertEqual(student.get_course_id(), 1)
        self.assertEqual(student.get_course_code(), "SF1624")
        self.assertEqual(student.get_course_name(), "Envariabelanalys")
        self.assertEqual(student.get_hp(), 7.5)


if __name__ == '__main__':
    unittest.main()