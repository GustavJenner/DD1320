from TrackFile import Track
import timeit

def create_track_list(): #skapar en lista med alla "tracks" som objekt inuti listan
    track_list = []
    with open("unique_tracks.txt", "r", encoding="utf-8") as file:
        for line in file:
            tmp = line.split("<SEP>")
            track_list.append(Track(tmp[0], tmp[1], tmp[2], tmp[3]))
    return track_list


def create_lesser_list(n): #retunerar en slicad version av listan samt retunerar sista "tracket"
    lesser_list = create_track_list()[0:n]
    last_track = lesser_list[-1]
    return lesser_list, last_track


def linear_search(list, test_track): #linjär sök metod O(n)
    for tracks in list:
        if test_track == tracks.tracktitle:
            print(tracks.tracktitle)
            break




def binarysearch(list, test_track): #binär sökning delvis tagen från föreläsning 2 O(log n)
    low = 0
    high = len(list)-1

    while low <= high:
        middle = (low + high)//2
        if list[middle].tracktitle == test_track:
            break
        else:
            if test_track < list[middle]:
                high = middle - 1
            else:
                low = middle + 1




def create_hash_table(list): #skapar en hash tabell O(1) för sökning i hash tabell
    hash_table = {}

    for tracks in list:
        hash_table[tracks.trackid] = tracks.tracktitle

    return hash_table


def bubblesort(list): #bubblesort från föreläsning 9 O(n^2)
    j = 0
    n = len(list)
    cont = True
    while cont:
        cont = False
        for i in range(n-1-j):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                cont = True
        i += 1

    return list


def mergesort(data): #mergesort tagen från föreläsningen 9 O(n*log(n))
    if len(data) > 1:
        middle = len(data)//2
        left = data[:middle]
        right = data[middle:]

        mergesort(left)
        mergesort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i = i + 1
            else:
                data[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            data[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            data[k] = right[j]
            j = j + 1
            k = k + 1


n = 100000 # Storlek på lista
track_list, last_track = create_lesser_list(n) #objekt lista och test försök (sista låten)
hash_table = create_hash_table(track_list) #skapar hash tabell
#time_linear = timeit.timeit(stmt = lambda: linear_search(track_list, last_track.tracktitle), number = 10000)
# time_hash = timeit.timeit(stmt = lambda: hash_table[last_track.trackid], number = 10000)
#track_list.sort()
#time_binary = timeit.timeit(stmt = lambda: binarysearch(track_list, last_track.tracktitle), number = 10000)
#print("linear "+str(time_linear))
#print("binary "+str(time_binary))
# print("hash "+str(time_hash))
#time_bubble = timeit.timeit(stmt = lambda: bubblesort(track_list), number = 1)
#time_merge = timeit.timeit(stmt = lambda: mergesort(track_list), number = 1)
#print("bubble "+str(time_bubble))
#print("merge "+str(time_merge))

#Analys
#Linjärsökning:
# 214, 487, 867
#Enligt teori ska den dubblas om n dubblas vilket den nästan gör
# 214 428 856
#Binärsökning
# 0.051 0.058 0.060
#Skiljer sig från teori för värsta fall då borde den ge (log(n))
#0.051 0.054 0.057
#ger sämre tid en värsta fall vilket är konstigt
#dock skiljer sig tiden ganska mycket även när man kör samma test
#behöver testas med högre "number" för att få bättre resultat
#Sökning i hash tabell:
#ungefär 0.0009 för alla värden på n:
#vilket stämmer överäns med teori då ökning i n inte påverkar söknings tiden


#bubblesort
#0.354 27.0 4100 (för lång tid på sista, bör ta typ 4 dagar)
#Stämmer enligt teori då med en ökning av 10 gånger på n bör tiden öka med 100 gånger
#0.354 35.4 3540 354000
#Mergesort
#0.009 0.055 0.7 14.8
#stämmer ungefär med teorin
#0.009 0.12 1.5 18
# %%

#%%

#%%

#%%

#%%
