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

def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]:
                minst = j
        data[minst],data[i] = data[i], data[minst]

def main():
    filename = "unique_tracks.txt"
    # För n = 1000, n = 10 000, n = 100 000 och n = 1 000 000
    lista = read_file(filename)  # n = 1 000 000
    lista_1000 = lista[0:1000] # n = 1000
    lista_10000 = lista[0:10000] # n = 10 000
    lista_100000 = lista[0:100000] # n = 100 000
    n = len(lista)
    print("Antal element =", n)

    # Mäter tiden för sorteringen
    tid = timeit.timeit(stmt=lambda: urvalssortera(lista_100000), number=1)
    print("Total tid för sorteringen:", round(tid, 8), "sekunder")

    #for each_info in lista_10000:
        #print(each_info.artistname)

if __name__ == "__main__":
    main()

# ---- Kommentar på tidskomplexiteten -----
# Tidskomplexiteten för qsort algoritmen är: O(n^2)
# tidsfaktorn = T(n_2) / T(n_1) = (n_2^2 / n_1^2)
# tidsfaktorn = T(10 000) / T_2(1000) = (10 000^2 / 1000^2) = 100
# Tidsfaktorn mellan exmepelvis n = 1000 och n = 10 000 var: 5.89905792 / 0.05194513 = 113.5632 (Det stämmer alltså väldigt bra!)
# Resultaten från tidtagningen stämmer alltså väldigt bra med den tidsfaktor för de n som är valda!