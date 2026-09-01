import csv

class Drama:
    def __init__(self,drama_name,rating,actors,
    viewship_rate, genre, director, writer, year, no_of_episodes, network):
        self.drama_name = str(drama_name) #I klassen använd 'self.drama_name' utanför klassen bara drama_name
        self.rating = float(rating)
        self.actors = str(actors)
        self.viewship_rate = float(viewship_rate)
        self.genre = str(genre)
        self.director =  str(director)
        self.writer= str(writer)
        self.year = int(year)
        self.no_of_episodes = int(no_of_episodes)
        self.network = str(network)

    def __str__(self):
        return (f"{self.drama_name} ({self.year}) - Genre: {self.genre}, "
                f"Rating: {self.rating}, Viewership:{self.viewship_rate}, Writer:{self.writer},"
                f"No of episodes:{self.no_of_episodes}, Network:{self.network}")

    def __lt__(self,other):
        return self.rating < other.rating

    def kdramas_after_2018(self):
        if self.year >= 2018:
            print(f"{self.drama_name} ({self.year})")
        else:
            pass

    def get_network(self):
        if self.network == "SBS":
            return print (self.drama_name)
        else:
            pass

def read_kdramas(filename):
    with open(filename, "r",encoding="utf-8") as file:
        all_kdramas = csv.reader(file, delimiter=",", quotechar='"') #När du loopar över reader får du varje rad som en lista, en rad i CSV = en lista med strängar.
        next(all_kdramas) #Skippar första headern
        kdrama_list = []
        for each_kdrama in all_kdramas:
            kdrama_info = Drama(drama_name = each_kdrama[0],
            rating = each_kdrama[1],
            actors = each_kdrama[2],
            viewship_rate = each_kdrama[3],
            genre = each_kdrama[4],
            director = each_kdrama[5],
            writer = each_kdrama[6],
            year = each_kdrama[7],
            no_of_episodes = each_kdrama[8],
            network = each_kdrama[9])
            kdrama_list.append(kdrama_info) #Här sparas alla obejkt i en stor lista av listor
        return kdrama_list #Från index 1 till slutet av listan

def find_bestrated_kdrama(kdrama_list):
    find_kdrama_max = max(kdrama_list).drama_name
    maxrating = max(kdrama_list).rating
    return print(f"K-drama med högsta ratingen är: {find_kdrama_max} ({maxrating})")


def main():
    kd = read_kdramas("kdrama.csv")
    for every_kdrama in kd:
        print(every_kdrama)

    print("\n")
    print("Alla kdramas som är gjorda efter 2018 är:")
    for drama_1 in kd:
        drama_1.kdramas_after_2018() #Första frivilla metoden

    print("\n")
    print("All kdramas från SBS network är:\n")
    for drama_2 in kd:
        drama_2.get_network() #Andra frivilliga metoden

    find_bestrated_kdrama(kd)

main()