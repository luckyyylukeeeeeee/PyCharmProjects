from HashDict import readfile

class HashNode:
   def __init__(self, key = "", data = None):
      self.key = key
      self.data = data

class Hashtable:
   def __init__(self, size=29):
        self.size = size
        self.table = [[] for _ in range(size)]

   def store(self, key, data):
        hashed_index = self.hashfunction(key)
        place = self.table[hashed_index]
        for node in place:  # För varje nod på den platsen (iterar över)
            if node.key == key: # Om vi skickar in en key som redan finns ska vi uppdatera keys data
                node.data = data # Här uppdateras keys data
                return
        place.append(HashNode(key,data)) # Om vi har samma hash index läggs det till i en listan (plats redan finns) men med olika keys
                                         # Om vi har olika has index lägga den oxå till i en listan (ny plats)
   def search(self, key):
        try:
           hashed_index = self.hashfunction(key)
           place = self.table[hashed_index]
           for node in place:
               if node.key == key:
                   print(f"{key} finns med i listan!")
                   print(f"Datan för {key} är: {node.data}")
                   print(f"Ligger på plats: {hashed_index}")
                   return node.data
           raise KeyError
        except KeyError:
           print(f"'{key}' finns inte i tabellen")


   def hashfunction(self, key):
       key = key.strip().lower()
       result = 0
       for letter in key:
           result = result * 32 + ord(letter)
       return result % self.size

def main():
    info = readfile("kdramaMini.txt")
    drama_dict = Hashtable()
    for each_kd in info:
        first = each_kd.drama_name
        after = (each_kd.rating,each_kd.actors,each_kd.viewship_rate,each_kd.genre,
        each_kd.director,each_kd.writer,each_kd.year,each_kd.no_of_episodes,each_kd.network)
        drama_dict.store(first, after)
    test = input("Vad vill du hitta? ")
    drama_dict.search(test)
main()




