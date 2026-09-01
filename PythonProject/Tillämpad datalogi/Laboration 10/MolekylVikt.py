from molgrafik import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def isEmpty(self):
        return self.__first is None # Om länkade lista är tom returneras None

    def enqueue(self, x):
        new_node = Node(x) # Skapar en nod
        if self.__first is None:  #  Om kön är tom
            self.__first = new_node # self.__first ska vara den nya noden med x data och pekare först i LinkedQ
            self.__last = self.__first # Eftersom kön är tom från början finns bara en nod i den därav ska first och last vara samma
        else: # Om det redan finns något i kön
            self.__last.next = new_node  # Länka ihop sista noden i kön med den nya noden genom att hämta upp pekaren
            self.__last = new_node # self.__last blir då den nya SISTA noden med x data och pekare

    def dequeue(self):
        if self.isEmpty():  # Kön är tom
            return None # Returnera None
        else:
            data_in_node = self.__first.data # Datan i första noden sparas i en varibel
            self.__first = self.__first.next # Första noden ska bli nästkommande länkade nod
            if self.__first is None:  # Om kön blev tom ska self.__last uppdateras för att oxå vara None
                self.__last = None
            return data_in_node

    def size(self):
        count = 0
        current = self.__first # Den noden du är på, börjar på först noden
        while current is not None: # Så länge länkade listan inte pekar på none
            count += 1 # Count ska uppdateras
            current = current.next # Uppdaterar current så att den ska ta nästa nod i den länkade lista
        return count

    def peek(self):
        if self.__first is None:
            return None
        else:
            return self.__first.data

atom_dict = {
    "H": 1.00794,
    "He": 4.002602,
    "Li": 6.941,
    "Be": 9.012182,
    "B": 10.811,
    "C": 12.0107,
    "N": 14.0067,
    "O": 15.9994,
    "F": 18.9984032,
    "Ne": 20.1797,
    "Na": 22.98976928,
    "Mg": 24.3050,
    "Al": 26.9815386,
    "Si": 28.0855,
    "P": 30.973762,
    "S": 32.065,
    "Cl": 35.453,
    "K": 39.0983,
    "Ar": 39.948,
    "Ca": 40.078,
    "Sc": 44.955912,
    "Ti": 47.867,
    "V": 50.9415,
    "Cr": 51.9961,
    "Mn": 54.938045,
    "Fe": 55.845,
    "Ni": 58.6934,
    "Co": 58.933195,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.723,
    "Ge": 72.64,
    "As": 74.92160,
    "Se": 78.96,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.4678,
    "Sr": 87.62,
    "Y": 88.90585,
    "Zr": 91.224,
    "Nb": 92.90638,
    "Mo": 95.96,
    "Tc": 98,
    "Ru": 101.07,
    "Rh": 102.90550,
    "Pd": 106.42,
    "Ag": 107.8682,
    "Cd": 112.411,
    "In": 114.818,
    "Sn": 118.710,
    "Sb": 121.760,
    "I": 126.90447,
    "Te": 127.60,
    "Xe": 131.293,
    "Cs": 132.9054519,
    "Ba": 137.327,
    "La": 138.90547,
    "Ce": 140.116,
    "Pr": 140.90765,
    "Nd": 144.242,
    "Pm": 145,
    "Sm": 150.36,
    "Eu": 151.964,
    "Gd": 157.25,
    "Tb": 158.92535,
    "Dy": 162.500,
    "Ho": 164.93032,
    "Er": 167.259,
    "Tm": 168.93421,
    "Yb": 173.054,
    "Lu": 174.9668,
    "Hf": 178.49,
    "Ta": 180.94788,
    "W": 183.84,
    "Re": 186.207,
    "Os": 190.23,
    "Ir": 192.217,
    "Pt": 195.084,
    "Au": 196.966569,
    "Hg": 200.59,
    "Tl": 204.3833,
    "Pb": 207.2,
    "Bi": 208.98040,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Pa": 231.03588,
    "Th": 232.03806,
    "Np": 237,
    "U": 238.02891,
    "Am": 243,
    "Pu": 244,
    "Cm": 247,
    "Bk": 247,
    "Cf": 251,
    "Es": 252,
    "Fm": 257,
    "Md": 258,
    "No": 259,
    "Lr": 262,
    "Rf": 265,
    "Db": 268,
    "Hs": 270,
    "Sg": 271,
    "Bh": 272,
    "Mt": 276,
    "Rg": 280,
    "Ds": 281,
    "Cn": 285
}

class Syntaxfel(Exception):
    pass

def read_formula(input_element):
    elementq = LinkedQ()
    for each_symbol in input_element:
        elementq.enqueue(each_symbol)
    if not elementq.isEmpty():
        finished_mol = read_molecule(elementq)
        return finished_mol

def read_molecule(elementq):
    mol = read_group(elementq)
    if not elementq.isEmpty() and elementq.peek() != ")":  # När en ")" hittas avbryts och hoppar tillbaka till group
        mol.next = read_molecule(elementq)
    return mol

def read_group(elementq):
    symbol = elementq.peek()
    ruta = Ruta()
    if symbol == '(':
        ruta.atom = elementq.dequeue()
        ruta.down = read_molecule(elementq)  # Kommer ihåg platsen --> Hoppar tillbaka till read molekyl fram till ")" hittas
        if elementq.isEmpty() or elementq.peek() != ')':  # Icke försluten grupp
            func_syntax_error(elementq,"Saknad högerparentes vid radslutet " + rest)
        ruta.atom += elementq.dequeue()
        if elementq.isEmpty() or not elementq.peek().isdigit():  # Icke siffra efter grupp
            func_syntax_error(elementq,"Saknad siffra vid radslutet ")
        ruta.num = read_nummer(elementq)
    elif symbol.isupper() or symbol.islower():
        ruta.atom = read_atom(elementq)
        if not elementq.isEmpty() and elementq.peek().isdigit():
            ruta.num = read_nummer(elementq)
    else:
        func_syntax_error(elementq,"Felaktig gruppstart vid radslutet ")
    return ruta

def read_atom(elementq):
    versal = read_stor_bokstav(elementq)
    gemen = read_liten_bokstav(elementq)
    atom = versal + (gemen or "")
    all_atoms = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V "
                 "Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc "
                 "Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu "
                 "Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi "
                 "Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr "
                 "Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv")
    atom_list = all_atoms.strip().split()
    if atom not in atom_list:
        func_syntax_error(elementq,"Okänd atom vid radslutet ")
    return atom

def read_stor_bokstav(elementq):
    symbol = elementq.peek()
    if elementq.isEmpty() or not symbol.isupper():
        func_syntax_error(elementq,"Saknad stor bokstav vid radslutet ")
    elementq.dequeue()
    return symbol

def read_liten_bokstav(elementq):
    symbol = elementq.peek()
    if elementq.isEmpty():
        return
    if symbol.islower():
        liten_bok = elementq.dequeue()
        return liten_bok

def read_nummer(elementq):
    symbol = elementq.peek()
    if symbol.isdigit():
        first_number = elementq.dequeue()
        next_symbol = elementq.peek()
        if first_number == "0":
            func_syntax_error(elementq,"För litet tal vid radslutet ")
        if first_number == "1" and (elementq.isEmpty() or not next_symbol.isdigit()):
            func_syntax_error(elementq,"För litet tal vid radslutet ")
        while not elementq.isEmpty() and elementq.peek().isdigit():
            first_number += elementq.dequeue()
        comp_number = first_number
        if int(comp_number) < 2:
            func_syntax_error(elementq,"För litet tal vid radslutet ")
        else:
            return int(first_number)
    else:
        return

def func_syntax_error(elementq, message):
    rest = ""
    while not elementq.isEmpty():
        rest += elementq.dequeue()
    raise Syntaxfel(message + rest)

def weight(mol):
    total_weight = 0
    while mol is not None:
        if mol.atom.startswith("("):  # En grupp, t.ex. (OH)2
            group_weight = weight(mol.down) # Gå ner och räkna gruppens innehåll
            total_weight += group_weight * mol.num # Multiplicera med hur många gånger gruppen upprepas
        else:
            total_weight += atom_dict[mol.atom] * (mol.num or 1)
        if mol.next is not None:
            mol = mol.next
        else:
            break
    return total_weight

def kolla_rita_syntax(input_element):
    try:
        mol = read_formula(input_element)
        m_weight = weight(mol)
        print(m_weight)
        bild = Molgrafik()
        bild.show(mol)
        return mol
    except Syntaxfel as e:
        print(e)

if __name__ == "__main__":
    formel = input()
    mol_trad = kolla_rita_syntax(formel)

#O
#H20
#CO2
#(CH3)2(CH2)4
#Si(C3(COOH)2)4(H2O)7







