#Track class
class Track:
    #track init med alla attribute
    def __init__(self, trackid, tracktime, artistname, tracktitle):
        self.trackid = trackid
        self.tracktime = tracktime
        self.artistname = artistname
        self.tracktitle = tracktitle
    #returnerar True om other är större än tracktitle
    def __lt__(self, other):
        return self.tracktitle < other
    #retunerar True om tracktitle är större en other
    def __gt__(self, other):
        return self.tracktitle > other
