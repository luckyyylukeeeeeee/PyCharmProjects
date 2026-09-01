from arrayQFile import ArrayQ

def get_cards():
    empty_card_list = []
    cards = input("Ge 10 siffror uppdelat med kommatecken: ")
    empty_card_list.append(cards) # Returnerar en lista med endast ett element ex ["1,2,3,4,5,6,7,8,9"]
    for each_card in empty_card_list:
        list_of_cards = each_card.split(sep=",")  # Siffrorna är strings med ["1","2","3","4","5","6","7","8","9"]
        list_of_card_integers = ArrayQ()  # Skapar en instan av ArrayQ klassen som är en tom array []
        for each_string_card in list_of_cards: # Itererar över listan med string siffror
            numbers = int(each_string_card)  # Gör om alla siffror till intergers
            list_of_card_integers.enqueue(numbers) # Lägger till dom till den tommar arrayen [] med metoden enqueue
        return list_of_card_integers # Returnerar den färdiga lista

def wizardprogram():
    start_order = get_cards()
    finished_order = ArrayQ()
    for n in range(0,start_order.size()*2):
        if n % 2 == 0:
            put_card_behind = start_order.dequeue() #1
            start_order.enqueue(put_card_behind) #Lägger 1 längst bak
        else:
            card_on_table = start_order.dequeue()
            finished_order.enqueue(card_on_table)
    return finished_order

x = wizardprogram()
while not x.isEmpty():
    print(x.dequeue(), end=" ")


