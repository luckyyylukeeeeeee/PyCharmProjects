from studentClassFile import Student, create_student_objects
from coursesClassFile import Course, create_course_objects
from courseRegFile import CourseRegistration, create_registration_objects

student_objects = create_student_objects()
course_objects = create_course_objects()
registration_objects = create_registration_objects()

total_amount_of_course_points = 0
for each_course in course_objects:
    total_amount_of_course_points += each_course.get_hp()

all_students_points = {}

for students in student_objects:
    all_students_points[students.get_name()] = 0



for each_reg_course in registration_objects:
    for students in student_objects:
        if students.get_student_id() == each_reg_course.get_reg_student_id():
            for courses in course_objects:
                if courses.get_course_id() == each_reg_course.get_reg_course_id():
                    all_students_points[students.get_name()] += courses.get_hp()


for c in all_students_points:
    print(c, all_students_points[c])

total_courses_cleared = {}
for each_student in all_students_points:
    points = (all_students_points[each_student] / total_amount_of_course_points) * 100
    total_courses_cleared[each_student] = f"{points:.1f}%"

print(f"Antal obligatoriska poäng: {total_amount_of_course_points}")
print("-"*32)
for student in total_courses_cleared:
    print(student, total_courses_cleared[student])

