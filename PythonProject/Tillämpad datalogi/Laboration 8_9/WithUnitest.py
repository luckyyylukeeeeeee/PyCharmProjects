from LinkedQFileCopy import LinkedQ

class Syntaxfel(Exception):
   pass

def read_formula(input_element):
   elementq = LinkedQ()
   for each_symbol in input_element:
       elementq.enqueue(each_symbol)
   # Lägg till en markör i slutet
   #elementq.enqueue('\n')
   while not elementq.isEmpty(): #and elementq.peek() != '\n':
       read_molecule(elementq)
   #if not elementq.isEmpty() and elementq.peek() == '\n':
       #elementq.dequeue()

def read_molecule(elementq):
   read_group(elementq)
   while not elementq.isEmpty() and elementq.peek() not in [')', '\n']:
       read_molecule(elementq)

def read_group(elementq):
   symbol = elementq.peek()
   if symbol == '(':
       elementq.dequeue()
       read_molecule(elementq)
       if elementq.isEmpty() or elementq.peek() != ')':
           elements_left = ""
           while not elementq.isEmpty():
               elements_left += elementq.dequeue()
           raise Syntaxfel("Saknad högerparentes vid radslutet " + elements_left)
       elementq.dequeue()  # ta bort ')'
       if elementq.isEmpty() or not elementq.peek().isdigit():
           elements_left = ""
           while not elementq.isEmpty():
               elements_left += elementq.dequeue()
           raise Syntaxfel("Saknad siffra vid radslutet " + elements_left)
       read_number(elementq)
   elif symbol.isupper() or symbol.islower():
       read_atom(elementq)
       if not elementq.isEmpty() and elementq.peek().isdigit():
           read_number(elementq)
   else:
       elements_left = ""
       while not elementq.isEmpty():
           elements_left += elementq.dequeue()
       raise Syntaxfel("Felaktig gruppstart vid radslutet " + elements_left)

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
        rest = ""
        while not elementq.isEmpty():
            rest += elementq.dequeue()
        raise Syntaxfel("Okänd atom vid radslutet " + rest)
    return atom

def read_stor_bokstav(elementq):
   if elementq.isEmpty() or not elementq.peek().isupper():
       elements_left = ""
       while not elementq.isEmpty():
           elements_left += elementq.dequeue()
       raise Syntaxfel("Saknad stor bokstav vid radslutet " + elements_left)
   return elementq.dequeue()

def read_liten_bokstav(elementq):
   if elementq.isEmpty() or not elementq.peek().islower():
       return ""  # valfritt liten bokstav
   return elementq.dequeue()

def read_number(elementq):
   if elementq.isEmpty() or not elementq.peek().isdigit():
       return
   first_number = elementq.dequeue()
   if first_number == "0":
       numbers_left = ""
       while not elementq.isEmpty():
           numbers_left += elementq.dequeue()
       raise Syntaxfel("För litet tal vid radslutet " + numbers_left)
   elif first_number == "1":
       if elementq.isEmpty() or not elementq.peek().isdigit():
           numbers_left = ""
           while not elementq.isEmpty():
               numbers_left += elementq.dequeue()
           raise Syntaxfel("För litet tal vid radslutet " + numbers_left)
       else:
           # fler siffror efter 1 → läs bort dem
           while not elementq.isEmpty() and elementq.peek().isdigit():
               elementq.dequeue()
   else:
       while not elementq.isEmpty() and elementq.peek().isdigit():
           elementq.dequeue()

def check_syntax(input_element):
   try:
       read_formula(input_element)
       return "Formeln är syntaktiskt korrekt"
   except Syntaxfel as fel:
       return str(fel)

"""
class SyntaxTest(unittest.TestCase):
   #Testar rätt fall
   def test_one_capital_letter(self):
       self.assertEqual(check_syntax("Na"), "Formeln är syntaktiskt korrekt")
   def test_one_capital_one_lowercase(self):
       self.assertEqual(check_syntax("H2O"), "Formeln är syntaktiskt korrekt")
   def test_right_number_one_capital(self):
       self.assertEqual(check_syntax("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
   def test__right_number_one_capital_one_lowercase(self):
       self.assertEqual(check_syntax("Na332"), "Formeln är syntaktiskt korrekt")


class SyntaxTest2(unittest.TestCase):
   #Testar fel
   def test_wrong_number(self):
       self.assertEqual(check_syntax("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
   def test_wrong_number2(self):
       self.assertEqual(check_syntax("C(OH4)"), "Saknad siffra vid radslutet C")
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

