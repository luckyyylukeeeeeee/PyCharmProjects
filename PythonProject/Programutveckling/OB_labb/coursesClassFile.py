import sqlite3
import unittest

def get_classes():
    """Hämtar kursinformation från SQLite-databasen och sparar
    informationen i en lista med dictionaries.
    :return: En lista med kursernas course_id, course_code, course_name, hp.
    """
    con_2 = sqlite3.connect("medieteknik.sqlite")
    cur_2 = con_2.cursor()
    classes_rows = cur_2.execute("SELECT * FROM Kurs")
    return [{"course_id": r[0], "course_code": r[1], "course_name": r[2], "hp": r[3]} for r in classes_rows]

course_list = get_classes()

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

def create_course_objects():
    """Skapar Course-objekt utifrån informationen från databasen.
    :return: En lista med Course-objekt.
    """
    course_object_list = []
    for each_course in course_list:
        course_object = Course(
            course_id=each_course["course_id"],
            course_code=each_course["course_code"],
            course_name=each_course["course_name"],
            hp=each_course["hp"]
        )
        course_object_list.append(course_object)
    return course_object_list

class TestStudent(unittest.TestCase):
    """Testar att Course-klassen skapar objekt med rätt course_id, course_code, course_name och hp."""
    def test_student(self):
        """Kontrollera att getters returnerar rättinformation."""
        student = Course(1, "DM1581", "Introduktion till medieteknik", 6.0)
        self.assertEqual(student.get_course_id(), 1)
        self.assertEqual(student.get_course_code(), "DM1581")
        self.assertEqual(student.get_course_name(), "Introduktion till medieteknik")
        self.assertEqual(student.get_hp(), 6.0)

if __name__ == '__main__':
    unittest.main()
