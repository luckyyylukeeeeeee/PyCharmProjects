from studentClassFile import create_student_objects
from coursesClassFile import create_course_objects
from courseRegClassFile import create_registration_objects

student_objects = create_student_objects() #Kallar på funktionen som skapar objekten från studentClassFile
course_objects = create_course_objects() #Kallar på funktionen som skapar objekten från coursesClassFile
registration_objects = create_registration_objects() #Kallar på funktionen som skapar objekten från courseRegFile

def calculate_hp_per_student():
    """Beräknar hur många högskolepoäng varje student har klarat
    baserat på studentens kursregistreringar.
    :return: En dictionary med studenternas namn och totala antal högskolepoäng.
    """
    all_students_points = {}
    for students in student_objects:
        all_students_points[students.get_name()] = 0 # Lägger till alla studenter i en dictionary och börjar på 0 poäng.
    for each_reg_course in registration_objects: # Går igenom alla kursregistreringar
        for students in student_objects:
            if students.get_student_id() == each_reg_course.get_reg_student_id(): # Kontrollerar vilken student kursregistreringen tillhör.
                for courses in course_objects:
                    if courses.get_course_id() == each_reg_course.get_reg_course_id(): # Kontrollerar vilken kurs som kursregistreringen gäller.
                        all_students_points[students.get_name()] += courses.get_hp() # Lägger till kursens högskolepoäng till studenten.
    return all_students_points

def calculate_total_course_points():
    """Beräknar det totala antalet högskolepoäng för alla obligatoriska kurser.
    :return: Det totala antalet högskolepoäng.
    """
    total_amount_of_course_points = 0
    # Går igenom alla kurser och summerar deras högskolepoäng.
    for each_course in course_objects:
        total_amount_of_course_points += each_course.get_hp()
    return total_amount_of_course_points

def main():
    """Kör programmets huvudfunktion och beräknar hur stor andel
    av de obligatoriska högskolepoängen varje student har klarat.
    """
    tot_course_points = calculate_total_course_points()
    st_points = calculate_hp_per_student()
    total_courses_cleared = {}
    # Beräknar procentandelen av de obligatoriska poängen som varje student har klarat.
    for each_student in st_points:
        points = (st_points[each_student] / tot_course_points) * 100
        total_courses_cleared[each_student] = f"{points:.1f}%"
    print(f"Antal obligatoriska poäng: {tot_course_points}")
    print("-"*32)
    for student in total_courses_cleared:
        print(f"{student} har klarat ", total_courses_cleared[student])

if __name__ == "__main__":
    main() # Påbörjar programmet






