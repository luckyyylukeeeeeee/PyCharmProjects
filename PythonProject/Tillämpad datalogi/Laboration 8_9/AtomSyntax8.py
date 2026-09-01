from LinkedQFileCopy import LinkedQ as Queue
import unittest

class Syntaxfel(Exception):
    pass

def read_stor_bokstav(elementq):
    symbol = elementq.dequeue()
    if symbol.isupper():
        return
    while not elementq.isEmpty():
        symbol += elementq.dequeue()
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + symbol)

def read_liten_bokstav(elementq):
    symbol = elementq.peek()
    if elementq.isEmpty() or symbol.isdigit():
        return
    if symbol.islower():
        elementq.dequeue()
        return
    elementq.dequeue()
    while not elementq.isEmpty():
        symbol += elementq.dequeue()
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + symbol)

def read_nummer(elementq):
    if elementq.isEmpty():
        return
    symbol = elementq.dequeue()
    next_symbol = elementq.peek()
    if symbol.isdigit():
        if int(symbol) == 0 and next_symbol is None:
            raise Syntaxfel("För litet tal vid radslutet ")
        if int(symbol) == 0 and next_symbol is not None:
            rest = ""
            while not elementq.isEmpty():
                rest += elementq.dequeue()
            raise Syntaxfel("För litet tal vid radslutet " + rest)
        else:
            num_str = symbol
            while not elementq.isEmpty():
                num_str += elementq.dequeue()
            number = int(num_str)
            if number < 2:
                raise Syntaxfel("För litet tal vid radslutet")
            else:
                return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")

def read_atom(elementq):
    read_stor_bokstav(elementq)
    read_liten_bokstav(elementq)

def read_molekyl(inp_element):
    elementq = Queue()
    for each_symbol in inp_element:
        elementq.enqueue(each_symbol)
    read_atom(elementq)
    symbol = elementq.peek()
    if symbol is None:
        return
    else:
        read_nummer(elementq)
        return

def kollasyntax(inp_element):
    try:
        read_molekyl(inp_element)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel)

class SyntaxTest(unittest.TestCase):
    def test_capital_letter_first(self):
        self.assertEqual(kollasyntax("N"), "Formeln är syntaktiskt korrekt")

    def test_capital_letter_first_and_lowecase(self):
        self.assertEqual(kollasyntax("Au"), "Formeln är syntaktiskt korrekt")

    def test_capital_letter_first_and_number(self):
        self.assertEqual(kollasyntax("H2"), "Formeln är syntaktiskt korrekt")

    def test_capital_letter_first_and_numbers(self):
        self.assertEqual(kollasyntax("P1"), "För litet tal vid radslutet")

    def test_capital_letter_first_and_lowecase_and_number(self):
        self.assertEqual(kollasyntax("Ag3"), "Formeln är syntaktiskt korrekt")

    def test_capital_letter_first_and_lowecase_and_several_number(self):
        self.assertEqual(kollasyntax("Fe12"), "Formeln är syntaktiskt korrekt")

    def test_capital_letter_first_and_lowecase_and_several_number_again(self):
        self.assertEqual(kollasyntax("XX5"), "Saknad stor bokstav vid radslutet X5")

if __name__ == '__main__':
    unittest.main()

 
