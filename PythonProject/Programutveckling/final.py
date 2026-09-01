from studentClassFile import Student, create_student_objects
from coursesClassFile import Course, create_course_objects
from courseRegFile import CourseRegistration, create_registration_objects

student_objects = create_student_objects()
course_objects = create_course_objects()
registration_objects = create_registration_objects()
for student in student_objects:
    student.print_info()
for course in course_objects:
    course.print_info()
print(registration_objects)


"""for each_student in student_objects:
    if each_student.course_id==registration_objects.student_id:

for each_course in course_objects:
    if each_course.course_id==registration_objects.course_id:
    
    
    { Alice:[6,7,9,10,5]
    for each coruser in courses[Alice]
     """

def

