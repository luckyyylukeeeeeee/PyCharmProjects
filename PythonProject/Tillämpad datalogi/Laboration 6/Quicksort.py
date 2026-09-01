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

# ---- Quicksort algoritm som sär taken från föreläsning 8 -----
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)


def qsort(data, low, high):
    pivotindex = (low + high) // 2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low - 1, high, data[high])

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid - low > 1:
        qsort(data, low, pivotmid - 1)
    if high - pivotmid > 1:
        qsort(data, pivotmid + 1, high)


def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v


def main():
    filename = "unique_tracks.txt"
    lista = read_file(filename)
    # För n = 1000, n = 10 000, n = 100 000 och n = 1 000 000
    lista_1000 = lista[0:1000]
    lista_10000 = lista[0:10000]
    lista_100000 = lista[0:100000]
    n = len(lista)
    print("Antal element =", n)

    # Mäter tiden för sorteringen
    tid = timeit.timeit(stmt=lambda: qsort(lista_10000,0,9999), number=1)
    print("Total tid för sorteringen:", round(tid, 8), "sekunder")

    #for each_info in lista_100000:
        #print(each_info.artistname)

if __name__ == "__main__":
    main()

# ---- Kommentar på tidskomplexiteten -----
# Tidskomplexiteten för qsort algoritmen är: O(n*log n)
# tidsfaktorn = T(n_2) / T(n_1) = (n_2 * log(n_2)) / (n_1 * log(n_1))
# tidsfaktorn = T(10 000) / T(1000) = (10 000 * log(10 000)) / (1000 * log(1000)) = 13.33333
# Tidsfaktorn mellan exmepelvis n = 1000 och n = 10 000 var: 0.02954225 / 0.00221654 = 13.6428
# Resultaten från tidtagningen stämmer alltså väldigt bra med den tidsfaktor för de n som är valda!