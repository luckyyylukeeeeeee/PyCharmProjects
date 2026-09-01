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
            #print("Kön är tom!")
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








