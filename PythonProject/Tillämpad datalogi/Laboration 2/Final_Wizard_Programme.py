#from arrayQFile import ArrayQ as Queue
from linkedQFile import LinkedQ as Queue

def get_cards():
    cards = input("Vilken ordning ska korten ligga i (separera med kommatecken): ")
    card_values = cards.split(",")  # Dela upp från inputen för varje koma
    deck_of_cards = Queue() # Anropar klassen, en instans av klassen --> kommer vara en system för att spara saker i listor
    for each_value in card_values: # För varje card value i korten som gavs ska gås igenom
        deck_of_cards.enqueue(each_value.strip())  # Tar bort eventuella mellanslag och lägger till i kön, 'kortleke' så att säga
    return deck_of_cards # Returnerar den nyfyllda kortleken

def wizardprogram():
    start_order = get_cards() # Start ordern på korten i handen ska vara givna från importen
    finished_order = Queue() # Instans av Queue() klassen kommer vara en tom kö
    for n in range(0, (start_order.size()) * 2): #Eftersom ett kort läggs lägnst bak kommer allt behövas göra 2x mer
        if n % 2 == 0: # Om det är en udda gång eller jämna
            put_card_behind = start_order.dequeue()
            start_order.enqueue(put_card_behind)
        else:
            card_on_table = start_order.dequeue()
            finished_order.enqueue(card_on_table)
    return finished_order

if __name__ == "__main__":
    result = wizardprogram()
    print("Kort på bordet: ", end="")
    while not result.isEmpty():
        print(result.dequeue(), end=" ")

# LinkedQ kan hantera data med flera olika längder och typer
# ArrayQ kan bara hantera en datatyp och för den datatypen kan den bara hantera data med 1 tecken