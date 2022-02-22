from TrackFile import Track
import timeit

def create_track_list():
    track_list = []
    with open("unique_tracks.txt", "r", encoding="utf-8") as file:
        for line in file:
            tmp = line.split("<SEP>")
            track_list.append(Track(tmp[0], tmp[1], tmp[2], tmp[3]))
    return track_list


def create_lesser_list(n):
    lesser_list = create_track_list()[0:n]
    last_track = lesser_list[-1]
    return lesser_list, last_track


def linear_search(list, test_track):
    for tracks in list:
        if test_track == tracks.tracktitle:
            break


def get_track(obj):
    return obj.tracktitle


def binarysearch(list, test_track):
    low = 0
    high = len(track_list) - 1
    found = False

    while low <= high and not found:
        middle = (low + high) // 2
        if list[middle].tracktitle == test_track:
            found = True
        else:
            if test_track < list[middle].tracktitle:
                high = middle - 1
            else:
                low = middle + 1



def create_hash_table(list):
    hash_table = {}

    for tracks in list:
        hash_table[tracks.trackid] = tracks.tracktitle

    return hash_table


def bubblesort(list):
    i = 0
    j = len(list)-1
    while j != 0:
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
        if i < j-1:
            i = i+1
        else:
            i = 0
            j = j-1

    return list
def mergesort(data):
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


n = 1000000
track_list, last_track = create_lesser_list(n)
# hash_table = create_hash_table(track_list)
# time_linear = timeit.timeit(stmt = lambda: linear_search(track_list, last_track.tracktitle), number = 10000)
# time_hash = timeit.timeit(stmt = lambda: hash_table[last_track.trackid], number = 10000)
# track_list.sort()
# time_binary = timeit.timeit(stmt = lambda: binarysearch(track_list, last_track.tracktitle), number = 10000)
# print("linear "+str(time_linear))
# print("binary "+str(time_binary))
# print("hash "+str(time_hash))
#time_bubble = timeit.timeit(stmt = lambda: bubblesort(track_list), number = 1)
time_merge = timeit.timeit(stmt = lambda: mergesort(track_list), number = 1)
#print("bubble "+str(time_bubble))
print("merge "+str(time_merge))
print("hej")
# %%

#%%

#%%

#%%

#%%
