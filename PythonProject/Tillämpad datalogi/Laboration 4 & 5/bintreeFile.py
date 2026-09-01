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
        print("")
        skriv(self.root)

#-------------------------------------------------------------------------------------------------#

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
        print(phrase.word_data) # Då printas det om nu phrase
        skriv(phrase.right)


""" Varför går det snabbt att söka i ett binärträd?
Ett binärt sökträd (BST) har idén att alla noder till vänster innehåller mindre värden än noden, 
och alla noder till höger innehåller större värden. När man söker efter ett ord behöver man därför inte titta på hela trädet, 
utan bara följa rätt “gren”:
- Om ordet är mindre än nuvarande nod → gå vänster.

- Om ordet är större → gå höger.

- Om ordet är lika → klart, vi hittade det!

Detta gör att sökningen är väldigt effektiv Istället för att jämföra med alla element (som i en lista), 
halverar man sökutrymmet för varje steg. I bästa fall tar det O(log n) steg (logaritmisk tid).
Det sämsta fallet (om trädet blir “snedvridet” som en lång kedja) tar O(n), men det kan undvikas om trädet hålls balanserat."""

""" Enkelt gränssnitt: Användaren ska bara behöva kalla på put("hej").
Rekursiv logik i separat funktion: putta behöver ta emot en nod att börja från,
ibland är det roten, ibland är det en undernod. Det gör koden renare och mer generell."""