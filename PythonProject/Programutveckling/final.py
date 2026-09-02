from studentClassFile import Student, create_student_objects
from coursesClassFile import Course, create_course_objects
from courseRegFile import CourseRegistration, create_registration_objects

student_objects = create_student_objects()
course_objects = create_course_objects()
registration_objects = create_registration_objects()

total_amount_of_course_points = 0
for each_course in course_objects:
    total_amount_of_course_points += each_course.hp

all_students = {}
for students in student_objects:
    all_students[students.name] = []

for each_reg_course in registration_objects:
    for students in student_objects:
        if students.student_id == each_reg_course.student_id:
            for courses in course_objects:
                if courses.course_id == each_reg_course.course_id:
                    all_students[students.name].append(courses)

for students in all_students:
    print(students, all_students[students])

student_points = {}
for students in student_objects:
    tot_course_points = 0
    for each_course in all_students[students.name]:
        tot_course_points += each_course.hp
    student_points[students.name] = tot_course_points

total_courses_cleared = {}
for each_student in student_points:
    points = (student_points[each_student] / total_amount_of_course_points) * 100
    total_courses_cleared[each_student] = f"{points:.1f}%"

for student in total_courses_cleared:
    print(student, total_courses_cleared[student])

