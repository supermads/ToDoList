def tracklist(**entries):
    for band, songs in entries.items():
        print(band)
        for album, track in songs.items():
            print("ALBUM: {} TRACK: {}".format(album, track))
