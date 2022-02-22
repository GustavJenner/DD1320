class Track:
    def __init__(self, trackid, tracktime, artistname, tracktitle):
        self.trackid = trackid
        self.tracktime = tracktime
        self.artistname = artistname
        self.tracktitle = tracktitle

    def __lt__(self, other):
        return self.tracktitle < other

    def __gt__(self, other):
        return self.tracktitle > other
