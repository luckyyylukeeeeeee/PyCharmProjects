from MusicInfoFile import Musicinfo
from collections import defaultdict
import timeit

def read_file(file):
    music_list = []
    with open(file, "r", encoding="utf-8") as music_file:
        for row in music_file:
            music_info = row.strip().split("<SEP>")
            one_song = Musicinfo(*music_info)
            music_list.append(one_song)
    return music_list

# ------------------- Kod från AI ------------------------ #
def build_dict(music_list):
    """
    Bygger en hashtabell (dictionary) där varje artistnamn pekar på en lista med låtar.
    Parametrar:
        music_list: en lista av låtobjekt som har attributet 'artistname'
    Returnerar:
        En dictionary där key = artistnamn, value = lista med låtar av den artisten
    """
    music_dict = defaultdict(list) # Skapa en dictionary där varje värde är en lista som standard
    for song in music_list: # Loopar igenom alla låtar i listan
        music_dict[song.artistname].append(song) # Lägg till låten i listan för den artist som matchar song.artistname
    return music_dict # Returnera den färdiga dictionaryn


def dict_search(music_dict, artist_name):
    """
    Söker efter alla låtar för en given artist i dictionaryn.
    Parametrar:
        music_dict: dictionary byggd med build_dict
        artist_name: sträng med artistens namn
    Returnerar:
        Lista med alla låtar av den artisten, eller tom lista om ingen finns
    """
    # Använd .get() för att hämta listan för artist_name, om artist_name inte finns returneras en tom lista []
    return music_dict.get(artist_name, [])


# --------------------------------------------------------- #

def main():
    filename = "unique_tracks.txt"
    lista = read_file(filename)
    n = len(lista)
    print("Antal element =", n)

    # Bygg hashtabell
    music_dict = build_dict(lista)

    testartist = "Bananarama"
    print("Testartist:", testartist)

    # Mät tiden för 1000 sökningar i hashtabellen
    dicttid = timeit.timeit(stmt=lambda: dict_search(music_dict, testartist), number=1000)
    print("Total tid för 1000 sökningar:", round(dicttid, 12), "sekunder")
    print("Genomsnitt per sökning:", round(dicttid / 1000, 15), "sekunder")

    # Visa antal låtar hittade
    results = dict_search(music_dict, testartist)
    print("Antal låtar hittade:", len(results))

if __name__ == "__main__":
    main()

# ---- Kommentar på tidskomplexiteten -----
# Tidskomplexiteten för qsort algoritmen är: O(1) konstant tidskomplexitet, det betyder att antalet operationer inte beror på storleken av n
# Tidsfaktorn = T(n_2) / T(n_1) = (n_2) / (n_1)
# Tidsfaktorn = T(1 000 000) / T(500 000) = 1 / 1 = 1
# Tidsfaktorn mellan exmepelvis n = 1000 och n = 10 000 var: 1.0966627e^-7 / 1.093379e^-7 = 1.0030003259
# Resultaten från tidtagningen stämmer alltså väldigt bra med den tidsfaktor för de n som är valda!
