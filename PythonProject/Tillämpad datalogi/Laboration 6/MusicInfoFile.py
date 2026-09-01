class Musicinfo:
    def __init__(self, trackid, time, artistname, title):
        self.trackid = trackid
        self.time = time
        self.artistname = artistname
        self.title = title

    def __lt__(self, other):
        return self.artistname < other.artistname

    def __str__(self):
        return f" TrackID: {self.trackid},Tid: {self.time}, Artist namn: {self.artistname}, Sång titel: {self.title}"

def read_file(file):
    music_list = []
    with open(file, "r", encoding="utf-8") as music_file:
        for row in music_file:
            music_info = row.strip().split("<SEP>")
            one_song = Musicinfo(*music_info) # * Är ett“unpacking operator”. Används för att packa upp en lista så att varje element skickas som ett separat argument
            music_list.append(one_song)
    return music_list

def make_file(input_file="unique_tracks.txt", output_file="output.txt"):
    with open(output_file, "w", encoding="utf-8") as out:
        for song in read_file(input_file):
            out.write(str(song) + "\n")

#make_file()

"""all_songs = read_file("unique_tracks.txt")

artist_songs = [song for song in all_songs if song.artistname == "Juice Leskinen"]
for s in artist_songs:
    print(s.title)"""
