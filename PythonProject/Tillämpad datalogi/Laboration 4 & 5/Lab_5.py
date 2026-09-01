from bintreeFile import Bintree
from linkedQFile import LinkedQ

swedish_bintree = Bintree()
gamla = Bintree()
que = LinkedQ()

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def get_swedish_words(file):
    with open(file, "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in swedish_bintree:
                pass
            else:
                swedish_bintree.put(ordet)

alfabet = (["a","b","c","d","e","f","g","h","i",
            "j","k","l","m","n","o","p","q","r",
            "s","t","u","v","w","x","y","z","å","ä","ö"])

def make_children(start_ord,slut_ord):
    gamla.put(start_ord.word)
    for bokstav in alfabet:
        for each_letter in range(len(start_ord.word)):
            new_word = start_ord.word[:each_letter] + bokstav + start_ord.word[each_letter+1:]
            if new_word in swedish_bintree:
                if new_word not in gamla:
                    parent_node = ParentNode(new_word,start_ord)
                    que.enqueue(parent_node)
                    gamla.put(new_word)
                    if new_word == slut_ord:
                        print(f"Det finns en väg till '{slut_ord}'")
                        print(f"Det här är vägen:")
                        writechain(parent_node)
                        return True

def writechain(slutordsnod):
    if slutordsnod is not None:
        writechain(slutordsnod.parent)
        print(slutordsnod.word)

def huvudprogram():
    get_swedish_words("svenska.txt")
    start_ord = input("Ge ett startord på 3 bokstäver: ")
    starting_parent_node = ParentNode(start_ord)
    slut_ord = input("Get ett slutord på 3 bokstäver: ")
    make_children(starting_parent_node,slut_ord)
    while not que.isEmpty():
        barn_nod = que.dequeue()
        if make_children(barn_nod,slut_ord):
            return
    print(f"Det finns ingen väg till '{slut_ord}'")

huvudprogram()