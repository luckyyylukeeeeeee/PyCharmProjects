from courseClassFileBONUS import Course
from programClassFileBONUS import Program
from studentClassFileBONUS import ProgramStudent
from queryingSqliteBONUS import (get_course_registration, get_courses,get_students,get_ob_course,get_program)

# Hämtar data från databasen
student_data = get_students()
course_data = get_courses()
registration_objects = get_course_registration()
ob_course_objects = get_ob_course()
program_data = get_program()

# Skapar Program-objekt
program_objects = []
for program in program_data:
    program_object = Program(
        program["id"],
        program["program_name"])
    program_objects.append(program_object)


# Skapar Course-objekt
course_objects = []
for course in course_data:
    course_object = Course(
        course["course_id"],
        course["course_name"],
        course["hp"])
    course_objects.append(course_object)


# Skapar ProgramStudent-objekt
student_objects = []
for student in student_data:
    for program in program_objects:
        # Kontrollerar vilket program studenten tillhör
        if student["program_id"] == program.get_program_id():
            student_object = ProgramStudent(
                student["student_id"],
                student["name"],
                program)
            student_objects.append(student_object)


def find_and_calculate_ob_course_points():
    """Funktionens syfte är att hitta vilka kurser som är obligatoriska
    för vilka program, samt räkna ut hur många HP-poäng som är obligatoriska
    för varje program.
    :return: Ett dictionary med varje program och dess obligatoriska kurser
    där nyckeln är programnamnet.
    :return: Ett dictionary med varje program och hur många obligatoriska
    HP programmet innehåller där nyckeln är programnamnet.
    """
    ob_courses_for_programmes = {}  # Dictionary för alla obligatoriska kurser per program
    for each_prog in program_objects:  # Loopar igenom alla program
        ob_courses_for_programmes[each_prog.get_name()] = []  # Programmet blir nyckel till en lista med ob-kurser
        for each_ob_course in ob_course_objects:  # Loopar igenom alla obligatoriska kurser
            # Kontrollerar om den obligatoriska kursen tillhör programmet
            if each_ob_course["program_id"] == each_prog.get_program_id():
                ob_courses_for_programmes[each_prog.get_name()].append(each_ob_course["kurs_id"])

    programme_points = {}  # Dictionary för hur många obligatoriska HP varje program har
    for programme, ob_courses in ob_courses_for_programmes.items():
        total_hp = 0
        for each_ob_course in ob_courses:  # Loopar igenom programmets obligatoriska kurser
            for each_course in course_objects:  # Loopar igenom alla kursobjekt
                # Kontrollerar om kursen är samma som den obligatoriska kursen
                if each_course.get_course_id() == each_ob_course:
                    total_hp += each_course.get_hp()
        programme_points[programme] = total_hp
    return ob_courses_for_programmes, programme_points


def find_programme_students():
    """Funktionens syfte är att hitta vilka kurser som är obligatoriska
    för vilka program, samt räkna ut hur många obligatoriska HP-poäng
    varje specifik student har klarat.
    :return: Ett nested dictionary där programnamnet är första nyckeln
    och sedan studentnamnet är andra nyckeln med datan antal obligatoriska
    HP avklarade av just den specifika studenten.
    Typ såhär ser det ut:
    {
        'Medieteknik': {
            'Eleven': - Antal obligatoriska HP avklarade,
            'Steve':  -||-
        },
        'Datateknik': {
            'Mike':  - Antal obligatoriska HP avklarade,
            'Lucas': -||-
            'Nancy': -||-
        }
    }
    """
    ob_courses_for_each_programme, _ = find_and_calculate_ob_course_points()
    students_per_programme = {}
    for programme in program_objects:  # Loopar igenom alla program
        students_per_programme[programme.get_name()] = {}
        for each_student in student_objects:  # Loopar igenom alla studenter
            # Kontrollerar om studenten tillhör det aktuella programmet
            if each_student.get_program_id() == programme.get_program_id():
                students_per_programme[programme.get_name()][each_student.get_name()] = 0
                for each_reg_course in registration_objects:  # Loopar igenom alla kursregistreringar
                    # Kontrollerar om kursregistreringen tillhör studenten
                    if each_reg_course["student_id"] == each_student.get_student_id():
                        for each_course in course_objects:  # Loopar igenom alla kurser
                            # Kontrollerar om kursregistreringen gäller den aktuella kursen
                            if each_reg_course["kurs_id"] == each_course.get_course_id():
                                for each_ob_c_id in ob_courses_for_each_programme[programme.get_name()]:  # Loopar igenom programmets obligatoriska kurser
                                    # Kontrollerar om kursen är obligatorisk för studentens program
                                    if each_course.get_course_id() == each_ob_c_id:
                                        students_per_programme[programme.get_name()][each_student.get_name()] += each_course.get_hp()
    return students_per_programme

def main():
    """Beräknar hur stor andel av programmets obligatoriska HP som
    varje student har klarat och skriver ut resultatet.
    :return: Ett dictionary med program som nyckel och studenter med
    deras procentuella andel av avklarade obligatoriska HP som data.
    """
    get_programmes = find_programme_students()
    _, programme_points = find_and_calculate_ob_course_points()
    for programme, students in get_programmes.items():
        print(f"{programme}:")
        for each_person, hp in students.items():
            points = (hp / programme_points[programme]) * 100
            students[each_person] = f"{points:.1f}%"
            print(f"  {each_person}: {students[each_person]}")
    return get_programmes

if __name__ == "__main__":
    main()  # Påbörjar programmet

