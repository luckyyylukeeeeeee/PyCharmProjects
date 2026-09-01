from MusicInfoFile import Musicinfo
import timeit

def read_file(file):
    music_list = []
    with open(file, "r", encoding="utf-8") as music_file:
        for row in music_file:
            music_info = row.strip().split("<SEP>")
            one_song = Musicinfo(*music_info) # * Är e “unpacking operator”. Används för att packa upp en lista så att varje element skickas som ett separat argument
            music_list.append(one_song)
    return music_list

def binary_search_all(music_list_sorted, artist_name):
    left = 0
    right = len(music_list_sorted) - 1
    results = [] # Här samlas alla träffar (alla låtar med samma artistnamn)

    # Hitta en matchning först
    found_index = -1
    while left <= right:
        mid = (left + right) // 2 # Mittenindex
        if music_list_sorted[mid].artistname == artist_name: # Om vi hittar artistnamnet → spara index och bryt loopen
            found_index = mid
            break
        elif music_list_sorted[mid].artistname < artist_name: # Om artistnamnet på mitten är "alfabetiskt mindre" → sök i högra halvan
            left = mid + 1
        else:
            right = mid - 1 # Om artistnamnet på mitten är "alfabetiskt mindre" → sök i vänstra halvan

    if found_index == -1:
        return results  # Tom lista om ingen matchning

    # Sök åt vänster
    i = found_index
    # Så länge vi inte gått utanför listan (i >= 0) och artistnamnet på plats i är samma som det vi söker:
    while i >= 0 and music_list_sorted[i].artistname == artist_name:
        results.append(music_list_sorted[i])  # Lägg till låten i resultatlistan
        i -= 1  # Gå ett steg åt vänster (mot mindre index)

    # Sök åt höger
    i = found_index + 1
    # Så länge vi inte gått förbi slutet av listan (i < len(listan)) och artistnamnet på plats i är samma som det vi söker:
    while i < len(music_list_sorted) and music_list_sorted[i].artistname == artist_name:
        results.append(music_list_sorted[i])  # Lägg till låten i resultatlistan
        i += 1  # Gå ett steg åt höger (mot större index)

    return results

# --------------------------------------------------------- #

def main():
    filename = "unique_tracks.txt"
    lista = read_file(filename)
    lista.sort(key=lambda x: x.artistname)
    n = len(lista)
    print("Antal element =", n)

    testartist = "Bananarama"
    print("Testartist:",testartist)

    # Mät tiden för 1000 sökningar
    linjtid = timeit.timeit(stmt=lambda: binary_search_all(lista, testartist), number=1000)
    print("Total tid för 1000 sökningar:", round(linjtid,8), "sekunder")
    print("Genomsnitt per sökning:", round(linjtid / 1000,8), "sekunder")

    # Visa antal låtar hittade
    results = binary_search_all(lista, testartist)
    print("Antal låtar hittade:", len(results))

if __name__ == "__main__":
    main()

# ---- Kommentar på tidskomplexiteten -----
# Tidskomplexiteten för binär sökning algoritmen är: O(log(n))
# Tidsfaktorn = T(n_2) / T(n_1) = (log(n_2)) / (log(n_1))
# Tidsfaktorn = T(500 000) / T(250 000) = (log(500 000)) / (log(250 000)) = 1.075
# Tidsfaktorn mellan exmepelvis n = 250 000 och n = 500 0000 var: 2.51e^(-6) / 2.31e^(-6) = 1.08658
# Resultaten från tidtagningen stämmer alltså väldigt bra med den tidsfaktor för de n som är valda!