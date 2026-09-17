from studentClassFileOB import MediaStudent
from coursesClassFileOB import Course
from queryingSqliteOB import get_students, get_courses, get_registrations

def create_student_objects():
    """Skapar MediaStudent-objekt från databasen."""
    student_object_list = []
    for student in get_students():
        student_object = MediaStudent(
            student_id=student["student_id"],
            name=student["name"])
        student_object_list.append(student_object)
    return student_object_list

def create_course_objects():
    """Skapar Course-objekt från databasen."""
    course_object_list = []
    for course in get_courses():
        course_object = Course(
            course_id=course["course_id"],
            course_code=course["course_code"],
            course_name=course["course_name"],
            hp=course["hp"])
        course_object_list.append(course_object)
    return course_object_list

def add_courses_to_students(student_objects, course_objects):
    """Lägger till studenternas klarade kurser."""
    registrations = get_registrations()
    for registration in registrations:
        student_id = registration["student_id"]
        course_id = registration["course_id"]
        for student in student_objects:
            if student.get_student_id() == student_id:
                for course in course_objects:
                    if course.get_course_id() == course_id:
                       student.add_course(course)

def calculate_hp_per_student(student_objects):
    """Beräknar hur många högskolepoäng varje student har klarat."""
    all_students_points = {}
    for student in student_objects:
        total_hp = 0
        for course in student.get_courses():
            total_hp += course.get_hp()
        all_students_points[student.get_name()] = total_hp
    return all_students_points

def calculate_total_course_points(course_objects):
    """Beräknar det totala antalet högskolepoäng."""
    total_amount_of_course_points = 0
    for course in course_objects:
        total_amount_of_course_points += course.get_hp()
    return total_amount_of_course_points


def main():
    """Kör programmet."""
    student_objects = create_student_objects()   # Skapar student- och kursobjekt från databasen.
    course_objects = create_course_objects()     # Lägger studenternas kurser i deras MediaStudent-objekt.
    add_courses_to_students(student_objects,course_objects)
    tot_course_points = calculate_total_course_points(course_objects)  # Beräknar totalt antal obligatoriska poäng.
    st_points = calculate_hp_per_student(student_objects)     # Beräknar varje students poäng.
    total_courses_cleared = {}
    # Beräknar procentandel klarade poäng.
    for each_student in st_points:
        points = (st_points[each_student] / tot_course_points) * 100
        total_courses_cleared[each_student] = f"{points:.1f}%"
    print(f"Antal obligatoriska poäng: {tot_course_points}")
    print("-" * 32)
    for student in total_courses_cleared:
        print(f"{student} har klarat "f"{total_courses_cleared[student]}")

if __name__ == "__main__":
    main()