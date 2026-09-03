from courseFile import Course, create_course_objects
from courseRegiFile import CourseRegistration, create_registration_objects
from programFile import Program, create_program_objects
from studentFile import Student, create_student_objects
from obcourseFile import OC, create_ob_course_objects

student_objects = create_student_objects() #Kallar på funktionen som skapar objekten från studentClassFile
course_objects = create_course_objects() #Kallar på funktionen som skapar objekten från coursesClassFile
registration_objects = create_registration_objects() #Kallar på funktionen som skapar objekten från courseRegFile
program_objects = create_program_objects() #Kallar på funktionen som skapar objekten från programFile
ob_course_projects = create_ob_course_objects() #Kallar på funktionen som skapar objekten från obcourseFile

def find_and_calculate_ob_course_points():
    ob_courses_for_programmes = {}
    for all_courses in program_objects:
        ob_courses_for_programmes[all_courses.get_name()] = []
