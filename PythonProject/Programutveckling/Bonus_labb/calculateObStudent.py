from courseFile import Course, create_course_objects
from courseRegiFile import CourseRegistration, create_registration_objects
from programFile import Program, create_program_objects
from studentFile import Student, create_student_objects
from obcourseFile import OC, create_ob_course_objects

student_objects = create_student_objects() #Kallar på funktionen som skapar objekten från studentClassFile
course_objects = create_course_objects() #Kallar på funktionen som skapar objekten från coursesClassFile
registration_objects = create_registration_objects() #Kallar på funktionen som skapar objekten från courseRegFile
program_objects = create_program_objects() #Kallar på funktionen som skapar objekten från programFile
ob_course_objects = create_ob_course_objects() #Kallar på funktionen som skapar objekten från obcourseFile

def find_and_calculate_ob_course_points():
    ob_courses_for_programmes = {}
    for each_prog in program_objects:
        ob_courses_for_programmes[each_prog.get_name()] = []
        for each_ob_course in ob_course_objects:
            if each_ob_course.get_program_id() == each_prog.program_id:
                ob_courses_for_programmes[each_prog.get_name()].append(each_ob_course.get_course_id())
    programme_points = {}
    for programme, ob_courses in ob_courses_for_programmes.items():
        total_hp = 0
        for each_ob_course in ob_courses:
            for course in course_objects:
                if course.get_course_id() == each_ob_course:
                    total_hp += course.get_hp()
        programme_points[programme] = total_hp
    return ob_courses_for_programmes, programme_points

print(find_and_calculate_ob_course_points())

def find_programme_students():
    ob_courses_for_each_programme, _ = find_and_calculate_ob_course_points()
    students_per_programme = {}
    for programme in program_objects:
        students_per_programme[programme.get_name()] = {}
        for each_student in student_objects:
            if each_student.get_programe_id() == programme.get_program_id():
                students_per_programme[programme.get_name()][each_student.get_name()] = 0
                for each_reg_course in registration_objects:
                    if each_reg_course.get_student_id() == each_student.get_student_id():
                        for each_course in course_objects:
                            if each_reg_course.get_course_id() == each_course.get_course_id():

                                for each_ob_c_id in ob_courses_for_each_programme[programme.get_name()]:
                                    if each_course.get_course_id() == each_ob_c_id:
                                        students_per_programme[programme.get_name()][each_student.get_name()] += each_course.get_hp()

    return students_per_programme

print(find_programme_students())




    

#def get_each_programme_ob_hp():
