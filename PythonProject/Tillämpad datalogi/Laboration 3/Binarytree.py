class Node:
    def __init__(self, word_data):
        self.word_data = word_data
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None # Startpunkt 'roten' för det binära trädet

    def put(self, new_word): # Sorterar in new_word i trädet, som sen pekar på andra noder med höger och vänster
        self.root = putta(self.root, new_word) # Från self.root.().().() kommer pekarna säga höger höger vänster t.e.x

    def __contains__(self, new_word):
        return finns(self.root, new_word) # True om new_word finns i trädet, False annars

    def write(self): # Skriver ut trädet genom hjälpfunktionen skriv
        print("-- Ordträd --")
        skriv(self.root)

#-------------------------------------------------------------------------------------------------#

"""Här kollar funktionen om det finns en nod, om noden pekar på None ska det bara lägga till annars,
ska det göra en jämförelse. Efter jämförelsen är klar kallar den på sig själv går tillbaka till toppen, och eftersom
rekursion kommer ihåg sin plats kommer den nu ISTÄLLET inte starta från rooten utan från den senaste jämförelsen.
Den börjar alltså inte om från början. 
Rekursionen ser bara till att köra samma commandon igen fast nu på en "uppdaterad" plats i trädet!"""
def putta(current_node, new_word):
    if current_node is None:
        return Node(new_word) # Skapar nya noder som innehåller; ett ord, en höger pekare och en vänster pekare
    elif new_word > current_node.word_data:
        current_node.right = putta(current_node.right, new_word) # Ger self.root.right och om nästa är None sparas en där,
    elif new_word < current_node.word_data:
        current_node.left = putta(current_node.left,new_word) # Om den inte blivit None än, läggs till self.root.left.right.left t.e.x tills noden pekar på None
    return current_node

def finns(current_node,word):
        if current_node is None:  # Om vi når en tom nod → ordet finns inte
            return False
        if word == current_node.word_data: #Om vi hittar ordet → returnera True
            return True
        elif word > current_node.word_data: # word är större än current_node.word → gå höger
            return finns(current_node.right,word) # Sparar värdet True eller False
        elif word < current_node.word_data: # Om ordet är mindre current_node.word → gå vänster
            return finns(current_node.left, word) # Sparar värdet True eller False

def skriv(phrase):   # Funktion som gör själva jobbet att skriva ut trädet
    if phrase is not None: # Om phrase (self.root) INTE pekare på NONE
        skriv(phrase.left) # Går från toppen self.root --> self.root.left --> Kommer ihåg platsen --> kollar om
        print("Ord:",phrase.word_data) # Då printas det om nu phrase
        skriv(phrase.right)
   #Else:
        #continue



svenska_lexikon = Bintree()   # Skapar ett trädobjekt
svenska_lexikon.put("Sill")
svenska_lexikon.put("Banan")
svenska_lexikon.put("Gurka")
svenska_lexikon.put("Gummisnodd")
svenska_lexikon.put("Äpple")
svenska_lexikon.write()

if "Gurka" in svenska_lexikon:
    print("True")
else:
    print("False")

# *** Rekursion ***
# Den första instansen “vet” inte att värdet finns förrän det rekursiva anropet returnerar.
# Varje instans kontrollerar bara sin egen nod, sedan låter den rekursionen hantera nästa nivå.
# Alltså kommer den kolla vad som gäller för if satsen sen kalla på sig själv igen och då "går till toppen",
# med den informationen det redan vet kör igenom igen men nu vet den redan en av noderna så den går hoppa över allt innan och går
# direkt till nästa jämförelse, detta på grund av att ett rekursivt anrop "kommer ihåg sin plats"

