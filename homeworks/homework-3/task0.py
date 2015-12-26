__author__ = 'salmon-the-wise'
class Song:
    def __init__(self, artist, name, album, track, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.track = track
        self.year = year
        self.duration = duration

    def __repr__(self):
        song = "%s\t%s\t%s\t%s\t%s\t%s" % (self.name, self.artist, self.album, self.track, self.year, self.duration)
        return song

    # def __lt__(self, other):
    #     if self.artist < other.artist:
    #         return True
    #     if self.artist == other.artist and self.name < other.name:
    #         return True
    #     return False

input_file = open("songs1.txt", "r", encoding='utf-8')

songs = []
for line in input_file:
    name, artist, album, track, year, duration = line[:-1].split("\t")
    songs.append(Song(name, artist, album, track, year, duration))

print(songs)
