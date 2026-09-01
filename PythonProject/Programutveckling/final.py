from studentClassFile import Student, create_student_objects
from coursesClassFile import Course, create_course_objects
from courseRegFile import CourseRegistration, create_registration_objects

student_objects = create_student_objects()
course_objects = create_course_objects()
registration_objects = create_registration_objects()

"""for student in student_objects:
    student.print_info()
for course in course_objects:
    course.print_info()
print(registration_objects)"""

all_students = {}

for students in student_objects:
    all_students[students.name] = []

for each_reg_course in registration_objects:
    for students in student_objects:
        if students.student_id == each_reg_course.student_id:
            for courses in course_objects:
                if courses.course_id == each_reg_course.course_id:
                    all_students[students.name].append(courses)

print(all_students)
for students in student_objects:
    for each_course in all_students[students.name]:
        each_course.print_info()





"""for each_student in student_objects:
    if each_student.course_id==registration_objects.student_id:

for each_course in course_objects:
    if each_course.course_id==registration_objects.course_id:
"""



