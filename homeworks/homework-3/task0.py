from random import shuffle
from operator import attrgetter
from collections import defaultdict
from collections import Counter
import re


# Необходимо доработать класс Song: теперь instance objects данного класса должны так же иметь атрибуты:
# название альбома, позиция трека внутри альбома (ВАЖНО: позиция внутри альбома -- это, конечно, строка,
# ведь например для винилового издания позицией будет A1, B2 в зависимости от стороны пластинки
# и таких примеров достаточно много), год издания, и продолжительность в секундах

class Song:
    def __init__(self, name, artist, album, track, year, duration):
        self.name = name
        self.artist = artist
        self.album = album
        self.track = track
        self.year = year
        self.duration = duration

    def __repr__(self):
        song = "%s\t%s\t%s\t%s\t%s\t%s" % (self.name, self.artist, self.album, self.track, self.year, self.duration)
        return song


# Необходимо написать функцию import_songs(file_name), которая принимает строковое имя файла
# (в tsv-формате, формат будет приведен ниже) считывает его и возвращает лист instance object'ов класса Song

def import_songs(file_name):
    input_file = open(file_name, "r", encoding='UTF-8')
    playlist = input_file.read()
    items = playlist.split('\n')
    songs = []
    for item in items:
        songs.append(Song(*item.split('\t')))
    return songs

playlist1 = import_songs("songs1.txt")
# print(*playlist1, sep='\n')


# Необходимо написать функцию export_songs(songs, file_names),
# которая принимает список песен и строковое имя файла и записывает в него песни в tsv-формате

def export_songs(songs, file_names):
    thefile = open(file_names, 'w', encoding='UTF-8')
    for item in songs:
        thefile.write("%s\n" % item)
    thefile.close()

# exp = export_songs(playlist1, "answer.txt")

# Написать функцию shuffle_songs(songs), которая принимает список песен и возвращает перемешанный список песен


def shuffle_songs(songs):
    sh_songs = shuffle(songs)
    return sh_songs


shuff_songs = shuffle_songs(playlist1)


# Вывести на экран самого часто встречающегося исполнителя (по числу песен),
# если таких несколько, вывести любого из них (artist_name)

artist_name = []
for song in playlist1:
    artist_name.append(song.artist)


def find_artist(lst):
    elems = {}
    e, em = None, 0
    for i in lst:
        elems[i] = t = elems.get(i, 0) + 1
        if t > em:
            e, em = i, t
    return e


l = find_artist(artist_name)
print(l)

# Вывести на экран самую длинную песню, если таких несколько, вывести любую из них (song_name (TAB) artist_name)

a = str(max(playlist1, key=attrgetter('duration')))
attr = a.split('\t')
print(attr[0]+'\t'+attr[1])

# Вывести на экран самый длинный (по длительности) альбом (песни считаются в одном альбоме,
# если название альбомов и название исполнителей совпадают), если таких несколько,
# вывести любой из них (album_name (TAB) artist_name)

indexed_sums = defaultdict(int)
for song in playlist1:
    indexed_sums[(song.artist, song.album)] += int(song.duration)
longest = max(dict(indexed_sums))
print(longest[0]+'\t'+longest[1])


# Вывести на экран 10 слов наиболее встречающихся в названиях песен,
# если слов меньше вывести все (word1 (TAB) word2 (TAB) ... ). Слова необходимо вывести
# в порядке встречаемости -- от самого частого к самому редкому.
# Слова необходимо вывести в нижнем регистре (lowercase, строчные).

name_list = []
for song in playlist1:
    name_list.append(song.name)
name_list = (str(name_list)).lower()
words = re.findall('[a-z]+', name_list)

word_counter = {}
for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

popular_words = sorted(word_counter, key=word_counter.get, reverse=True)

if len(popular_words) > 10:
    top_10 = popular_words[:10]
    print('\t'.join(top_10))
else:
    top = popular_words
    print('\t'.join(top))

# Вывести на экран исполнителя с наибольшим числом альбомов,
# если таких несколько, то вывести любого из них (artist_name)

album_list1 = []
for song in playlist1:
    album_list1.extend((song.album, song.artist))

def common_album(lst):
    elems = {}
    e, em = None, 0
    for i in lst:
        elems[i] = t = elems.get(i, 0) + 1
        if t > em:
            e, em = i, t
    return e
c_a = str(common_album(album_list1))
print(c_a)
