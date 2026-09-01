from MusicInfoFile import Musicinfo
import timeit

def read_file(file):
    music_list = []
    with open(file, "r", encoding="utf-8") as music_file:
        for row in music_file:
            music_info = row.strip().split("<SEP>")
            one_song = Musicinfo(*music_info)
            music_list.append(one_song)
    return music_list

# ---- Linjärsökning ----
def linsok(music_list, artist_name):
    results = []
    for song in music_list:
        if song.artistname == artist_name:
            results.append(song)
    return results


def main():
    filename = "unique_quarter.txt"
    lista = read_file(filename)
    lista_1000 = lista[0:1000]
    n = len(lista)
    print("Antal element =", n)

    testartist = "Bananarama"
    print("Testartist:",testartist)

    # Mät tiden för 1000 sökningar
    linjtid = timeit.timeit(stmt=lambda: linsok(lista, testartist), number=1000)
    print("Total tid för 1000 sökningar:", round(linjtid, 6), "sekunder")
    print("Genomsnitt per sökning:", round(linjtid / 1000, 8), "sekunder")

    # Visa antal låtar hittade
    results = linsok(lista, testartist)
    print("Antal låtar hittade:", len(results))

if __name__ == "__main__":
    main()


# ---- Kommentar på tidskomplexiteten -----
# Tidskomplexiteten för linjörsökning algoritmen är: O(n)
# Tidsfaktorn = T(n_2) / T(n_1) = (n_2) / (n_1)
# Tidsfaktorn = T(500 000) / T(250 000) = (500 000) / (250 000) = 2
# Tidsfaktorn mellan exmepelvis n = 500 000 och n = 250 000 var: 0.0419847 / 0.00725354 = 1.95745387
# Resultaten från tidtagningen stämmer alltså väldigt bra med den tidsfaktor för de n som är valda!