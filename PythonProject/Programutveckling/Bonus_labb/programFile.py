import sqlite3


def get_program():
    con_2 = sqlite3.connect("eecs.sqlite")
    cur_2 = con_2.cursor()
    program_rows = cur_2.execute("SELECT * FROM Program")
    return [{"id": r[0], "program_name": r[1]} for r in program_rows]

class Program:
    def __init__(self, program_id, program_name):
        self.program_id = program_id
        self.program_name = program_name

    def get_info(self):
        return print(self.program_id,self.program_name)

    def get_name(self):
        return self.program_name

    def get_program_id(self):
        return self.program_id

def create_program_objects():
    program_object_list = []
    for each_program in get_program():
        program_object = Program(
            program_id=each_program["id"],
            program_name=each_program["program_name"])
        program_object_list.append(program_object)
    return program_object_list

