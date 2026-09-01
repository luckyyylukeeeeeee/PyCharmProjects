import csv

class Drama:
    def __init__(self,drama_name,rating,actors,
    viewship_rate, genre, director, writer, year, no_of_episodes, network):
        self.drama_name = drama_name #I klassen använd 'self.drama_name' utanför klassen bara drama_name
        self.rating = float(rating)
        self.actors = actors
        self.viewship_rate = float(viewship_rate)
        self.genre = genre
        self.director =  director
        self.writer= writer
        self.year = int(year)
        self.no_of_episodes = int(no_of_episodes)
        self.network = network

    def __str__(self):
        return (f"{self.drama_name} ({self.year}) - Genre: {self.genre}, "
                f"Rating: {self.rating}, Viewership: {self.viewship_rate}, Writer: {self.writer},"
                f"No of episodes: {self.no_of_episodes}, Network: {self.network}")

    def __lt__(self,other):
        return self.rating < other.rating

    def kdramas_after_2018(self):
        if self.year >= 2018:
            print(f"{self.drama_name} ({self.year})")
        else:
            pass

    def get_sbs_network(self):
        if self.network == "SBS":
            return print(self.drama_name)
        else:
            pass

def read_kdramas(filename):
    with open(filename, "r",encoding="utf-8") as file:
        all_kdramas = csv.reader(file, delimiter=",", quotechar='"') #När du loopar över reader får du varje rad som en lista, en rad i CSV = en lista med strängar.
        next(all_kdramas) #Skippar första headern
        kdrama_object_list = []
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
            kdrama_object_list.append(kdrama_info) #Här sparas alla obejkt i en stor lista av listor
        return kdrama_object_list #Från index 1 till slutet av listan

def find_bestrated_kdrama(all_kdrama):
    rating = 0
    for kdrama in all_kdrama:
        if kdrama.rating > rating:
            rating = kdrama.rating
            bestrated_kdrama = kdrama
        else:
            pass
    return print(f"K-drama med bäst rating är: {bestrated_kdrama.drama_name} ({bestrated_kdrama.rating})")

# --- Testar klassen Drama att den funkar ---
first_drama = Drama("Legend of the Blue Sea",8.1,"Jun Ji-hyun, Lee Min-ho",17.6,"Fantasy,Romance,Comedy","Jin Hyuk, Park Seon-Ho","Park Ji-eun",2016,21,"SBS")
second_drama = Drama("The Heirs",7.5,"Lee Min-ho, Park Shin-hye, Kim Woo-bin, Park Hyung-sik",16.7,"Romance, Drama, Teen","Kang Shin-hyo, Boo Sung-chul","Kim Eun-sook",2013,20,"SBS")
print(f"Testar första insatsen av Drama-objekt:{first_drama.drama_name} har ratingen {second_drama.rating} \n")
print(f"Testar andra insatsen av Drama-objekt: {second_drama.drama_name} har skådespelarna: {second_drama.actors} \n")

def main():
    get_kdrama_list = read_kdramas("kdrama.csv")

    #for every_kdrama in kd:
        #print(every_kdrama)

    print("-"*8,"\n")
    print("Alla K-dramas som är gjorda efter 2018 är:")
    for drama_1 in get_kdrama_list:
        drama_1.kdramas_after_2018() #Första frivilla metoden

    print("-"*8,"\n")
    print("All K-dramas från 'SBS network' är:")
    for drama_2 in get_kdrama_list:
        drama_2.get_sbs_network() #Andra frivilliga metoden

    print("-"*8)
    find_bestrated_kdrama(get_kdrama_list)

main()





