from LinkedQFileCopy import LinkedQ

class Syntaxfel(Exception):
    pass

def read_formula(input_element):
    elementq = LinkedQ()
    for each_symbol in input_element:
        elementq.enqueue(each_symbol)
    while not elementq.isEmpty():
        read_molecule(elementq)
    return

def read_molecule(elementq):
    read_group(elementq)
    while not elementq.isEmpty() and elementq.peek() != ")":  # När en ")" hittas avbryts och hoppar tillbaka till group
        read_molecule(elementq)

def read_group(elementq):
    symbol = elementq.peek()
    if symbol == '(':
        rest = ""
        elementq.dequeue()
        read_molecule(elementq)  # Kommer ihåg platsen --> Hoppar tillbaka till read molekyl fram till ")" hittas
        if elementq.isEmpty() or elementq.peek() != ')':  # Icke försluten grupp
            func_syntax_error(elementq,"Saknad högerparentes vid radslutet " + rest)
        elementq.dequeue()
        if elementq.isEmpty() or not elementq.peek().isdigit():  # Icke siffra efter grupp
            func_syntax_error(elementq,"Saknad siffra vid radslutet ")
        read_nummer(elementq)
    elif symbol.isupper() or symbol.islower():
        read_atom(elementq)
        if not elementq.isEmpty() and elementq.peek().isdigit():
            read_nummer(elementq)
    else:
        func_syntax_error(elementq,"Felaktig gruppstart vid radslutet ")

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
        elementq.dequeue()
        next_symbol = elementq.peek()
        if symbol == "0":
            func_syntax_error(elementq,"För litet tal vid radslutet ")
        num_str = symbol
        if symbol == "1" and (elementq.isEmpty() or not next_symbol.isdigit()):
            func_syntax_error(elementq,"För litet tal vid radslutet ")
        while not elementq.isEmpty() and elementq.peek().isdigit():
            num_str += elementq.dequeue()
        number = int(num_str)
        if number < 2:
            func_syntax_error(elementq,"För litet tal vid radslutet ")
    else:
        return

def kolla_syntax(input_element):
    try:
        read_formula(input_element)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel)

def func_syntax_error(elementq, message):
    rest = ""
    while not elementq.isEmpty():
        rest += elementq.dequeue()
    raise Syntaxfel(message + rest)

test_formler = [
    "Na",
    "H2O",
    "Si(C3(COOH)2)4(H2O)7",
    "Na332",
    "C(Xx4)5",
    "C(OH4)C",
    "C(OH4C",
    "H2O)Fe",
    "H0",
    "H1C",
    "H02C",
    "Nacl",
    "a",
    "(Cl)2)3",
    ")",
    "2",]

for formel in test_formler:
    resultat = kolla_syntax(formel)
    print(f"{formel} --> {resultat}")

"""def main():
    while True:
        test = input()
        if test == "#":
            break
        resultat = kollasyntax(test)
        print(resultat)

if __name__ == "__main__":
    main()"""

"""
class SyntaxTest(unittest.TestCase):
   #Testar rätt fall
   def test_one_capital_letter(self):
       self.assertEqual(check_syntax("Na"), "Formeln är syntaktiskt korrekt")
   def test_one_capital_one_lowercase(self):
       self.assertEqual(check_syntax("H2O"), "Formeln är syntaktiskt korrekt")
   def test_right_number_one_capital(self):
       self.assertEqual(check_syntax("S(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
   def test__right_number_one_capital_one_lowercase(self):
       self.assertEqual(check_syntax("Na332"), "Formeln är syntaktiskt korrekt")


class SyntaxTest2(unittest.TestCase):
   #Testar fel
   def test_wrong_number(self):
       self.assertEqual(check_syntax("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
   def test_wrong_number2(self):
       self.assertEqual(check_syntax("C(OH4)1"), "Saknad siffra vid radslutet C")
   def test_wrong_number3(self):
       self.assertEqual(check_syntax("C(OH4C"), "Saknad högerparentes vid radslutet ")
   def test_wrong_number4(self):
       self.assertEqual(check_syntax("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")
   def test_wrong_letter(self):
       self.assertEqual(check_syntax("H0"), "För litet tal vid radslutet ")
   def test_wrong_letter2(self):
       self.assertEqual(check_syntax("H1C"), "För litet tal vid radslutet C")
   def test_wrong_letter2(self):
       self.assertEqual(check_syntax("H02C"), "För litet tal vid radslutet 2C")
   def test_wrong_letter2(self):
       self.assertEqual(check_syntax("Nacl"), "Saknad stor bokstav vid radslutet cl")
   def test_wrong_letter2(self):
       self.assertEqual(check_syntax("a"), "Saknad stor bokstav vid radslutet a")
   def test_wrong_letter2(self):
       self.assertEqual(check_syntax("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
   def test_wrong_letter2(self):
       self.assertEqual(check_syntax(")"), "Felaktig gruppstart vid radslutet )")
   def test_wrong_letter2(self):
       self.assertEqual(check_syntax("2"), "Felaktig gruppstart vid radslutet 2")

if __name__ == '__main__':
   unittest.main()
"""




