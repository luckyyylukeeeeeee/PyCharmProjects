from bintreeFile import Bintree
from linkedQFile import LinkedQ

swedish_bintree = Bintree()
gamla = Bintree()
que = LinkedQ()

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
    """Så fort vi har bytt en bokstav ska det ordet lägga in
    i gamla Bintree dvs bintree med alla dumbarn"""
    gamla.put(start_ord)
    for bokstav in alfabet:
        for each_letter in start_ord:
            new_word = start_ord.replace(each_letter,bokstav)
            if new_word in swedish_bintree:
                if new_word not in gamla:
                    que.enqueue(new_word)
                    gamla.put(new_word)
                    if new_word == slut_ord:
                        print(f"Det finns en väg till '{slut_ord}'")
                        return True


def huvudprogram():
    get_swedish_words("svenska.txt")
    start_ord = input("Ge ett startord på 3 bokstäver: ")
    slut_ord = input("Get ett slutord på 3 bokstäver: ")
    que.enqueue(start_ord)
    make_children(start_ord,slut_ord)
    while not que.isEmpty():
        get_children = que.dequeue()
        if make_children(get_children,slut_ord):
            return
    print(f"Det finns ingen väg till '{slut_ord}'")

huvudprogram()
gamla.write()



