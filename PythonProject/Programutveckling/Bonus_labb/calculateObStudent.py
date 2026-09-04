from courseFile import create_course_objects
from courseRegiFile import create_registration_objects
from programFile import create_program_objects
from studentFile import create_student_objects
from obcourseFile import create_ob_course_objects

student_objects = create_student_objects() #Kallar på funktionen som skapar objekten från studentClassFile
course_objects = create_course_objects() #Kallar på funktionen som skapar objekten från coursesClassFile
registration_objects = create_registration_objects() #Kallar på funktionen som skapar objekten från courseRegFile
program_objects = create_program_objects() #Kallar på funktionen som skapar objekten från programFile
ob_course_objects = create_ob_course_objects() #Kallar på funktionen som skapar objekten från obcourseFile

def find_and_calculate_ob_course_points():
    """Funktionens syfte är att hitta vilka kurser som är obligatoriska för vilka program,
    samt räkna ut hur många hp poöng som just är obligatoriska för varje program.
    :return Ett dictionary med varje programs och dess obligatoriska kurser (kurs_id) där nyckeln programnamnet
    :return Ett dictiomary med varje program och hur många obligatoriska hp programmet innehåller
    dör nyckeln är programnamnet.
    """
    ob_courses_for_programmes = {} #Dic för alla ob kurser per program
    for each_prog in program_objects: #Loppar igenom programmen
        ob_courses_for_programmes[each_prog.get_name()] = [] #Programmen blir nyckeln till en lista med ob kurser som data
        for each_ob_course in ob_course_objects: #Loppar igenom ob kurserna
            if each_ob_course.get_program_id() == each_prog.program_id: #Om ob program id är lika med program id från programmen
                ob_courses_for_programmes[each_prog.get_name()].append(each_ob_course.get_course_id()) #Då lägger du till ob kursen i dic med programnamn som nyckel
    programme_points = {} #Dic för hur många ob poöng varje program har
    for programme, ob_courses in ob_courses_for_programmes.items(): #Hämtar nyckeln och dess data
        total_hp = 0 #Nollställer hp räkningen för varje program
        for each_ob_course in ob_courses: #Loppar igenom ob kurserna
            for course in course_objects: #Loppar igenom alla kurserna
                if course.get_course_id() == each_ob_course: #Om kurs kurs-id är like med ob kurs kurs-id
                    total_hp += course.get_hp() #Plussa ihop alla dom hp poängen
        programme_points[programme] = total_hp #Lägg till den total hp som data med varje programnamn som nyckel
    return ob_courses_for_programmes, programme_points #Returnerar båda dictionaries

#print(find_and_calculate_ob_course_points())

def find_programme_students():
    """Funktionens syfte är att hitta vilka kurser som är obligatoriska för vilka program,
    samt räkna ut hur många hp poöng som just är obligatoriska för varje program.
    :return Ett nested dictionary där programnamnet är första nyckeln och sen student namnet är andra nyckeln
    med datan antal ob hp avklarade av just den specifika studenten. Typ såhär ser det ut:
        {
        ├──── 'Media': {
        │       ├── 'Eleven' : - Antal ob hp avklarade
        │       ├── 'Steve' :    -||-
        │       }
        ├──── 'Data': {
        │       ├── 'Mike' : - Antal ob hp avklarade
        │       ├── 'Lucas':   -||-
        │       ├── 'Nancy':   -||-
                }
        }
    """
    ob_courses_for_each_programme, _ = find_and_calculate_ob_course_points() #Hämtar ob kurserna i varje program
    students_per_programme = {} #Dic för varje program
    for programme in program_objects: #Loppar igenom programmen
        students_per_programme[programme.get_name()] = {} #Programmen blir nyckeln till en dic med studenter som data
        for each_student in student_objects: #Loppar igenom studenterna
            if each_student.get_programe_id() == programme.get_program_id(): #Om studentens program id är lika med program id från programmen
                students_per_programme[programme.get_name()][each_student.get_name()] = 0 #Studenten blir nyckeln till 0 hp som data
                for each_reg_course in registration_objects: #Loppar igenom kursregistreringarna
                    if each_reg_course.get_student_id() == each_student.get_student_id(): #Om studentens id är lika med student id från kursregistreringen
                        for each_course in course_objects: #Loppar igenom alla kurserna
                            if each_reg_course.get_course_id() == each_course.get_course_id(): #Om kurs-id är lika med kurs-id från kursregistreringen
                                for each_ob_c_id in ob_courses_for_each_programme[programme.get_name()]: #Loppar igenom ob kurserna för programmet
                                    if each_course.get_course_id() == each_ob_c_id: #Om kurs-id är lika med ob kursens kurs-id
                                        students_per_programme[programme.get_name()][each_student.get_name()] += each_course.get_hp() #Plussa ihop alla dom avklarade ob hp poängen
    return students_per_programme #Returnerar dictionaryn med program, studenter och avklarade ob hp

#print(find_programme_students())

def main():
    """Beräknar hur stor andel av programmets obligatoriska hp som
    varje student har klarat och skriver ut resultatet.
    :return: Ett dictionary med program som nyckel och studenter med
    deras % andel av avklarade obligatoriska hp som data.
    """
    get_programmes = find_programme_students() #Hämtar studenterna och deras avklarade ob hp för varje program
    _, programme_points = find_and_calculate_ob_course_points() #Hämtar den totala mängden ob hp för varje program
    for programme, students in get_programmes.items(): #Loppar igenom programmen och dess studenter
        print(f"{programme}:") #Skriver ut programmets namn
        for each_person, hp in students.items(): #Loppar igenom studenterna och deras avklarade ob hp
            points = (hp / programme_points[programme]) * 100 #Räknar ut studentens procentuella andel av programmets ob hp
            students[each_person] = f"{points:.1f}%" #Byter ut studentens hp mot den procentuella andelen
            print (f"  {each_person} {students[each_person]}") #Skriver ut studentens namn och procentuella andel
    return get_programmes #Returnerar dictionaryn med program, studenter och deras procentuella andel

if __name__ == "__main__":
    main() # Påbörjar programmet

