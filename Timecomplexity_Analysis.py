from TrackFile import Track


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


def linear_search(track_list, last_track):
    found = False
    for tracks in track_list:
        if last_track.tracktitle == tracks.tracktitle:
            print("found track " + tracks.tracktitle)
            found = True
            break
    return found

def get_track(obj):
    return obj.tracktitle


def binarysearch(track_list, last_track):
    track_list.sort(key=get_track)
    low = 0
    high = len(track_list) - 1
    found = False

    while low <= high and not found:
        middle = (low + high) // 2
        if track_list[middle].tracktitle == last_track.tracktitle:
            found = True
            print("found track " + track_list[middle].tracktitle)
            break
        else:
            if last_track.tracktitle < track_list[middle].tracktitle:
                high = middle - 1
            else:
                low = middle + 1
    return found


def hashsearch(track_list, last_track):
    hash_table = {}

    for tracks in track_list:
        hash_table[tracks.trackid] = tracks.tracktitle

    if last_track.trackid in hash_table:
        print("found track ", hash_table[last_track.trackid])
        return True
    else:
        return False


n = 20
track_list, last_track = create_lesser_list(n)
linear_search(track_list, last_track)
binarysearch(track_list,last_track)
hashsearch(track_list,last_track)
#%%
