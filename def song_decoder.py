def song_decoder(song):
    song = song.replace("WUB", ' ').strip(' ')
    song = ' '.join(song.split())
    return song

print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))