from PyLyrics import *
import pandas as pd

# set of stopwords made from string split by whitespace
stopwords = set('i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now'.split())

smithsAlbums = PyLyrics.getAlbums(singer='The Smiths')
joyDivAlbums = PyLyrics.getAlbums(singer='Joy Division')

smithsTrackList = [(album, album.tracks()) for album in smithsAlbums]
joyDivTrackList = [(album, album.tracks()) for album in joyDivAlbums if album.__str__() == 'Unknown Pleasures' or album.__str__() == 'Closer']

smithsLyricsDocument = [[(album, song.__str__(), song.getLyrics()) for song in trackList] for album, trackList in smithsTrackList]
joyDivLyricsDocument = [[(album, song.__str__(), song.getLyrics()) for song in trackList]for album, trackList in joyDivTrackList]

# Cleaned lyrics with no escape characters

flatDoc = [(album, name, lyrics.replace('\n', ' ')) for song in smithsLyricsDocument for album, name, lyrics in song]
flatDocJV = [(album, name, lyrics.replace('\n', ' ')) for song in joyDivLyricsDocument for album, name, lyrics in song]

# DataFrame only contains the bands unique songs, with no repeats from re-released versions

smithsLyricsFrame = pd.DataFrame(flatDoc, columns=['Album', 'Title', 'Lyrics']).drop_duplicates(subset=['Lyrics']).dropna()
smithsLyricsFrame = smithsLyricsFrame[smithsLyricsFrame['Title'] != 'Oscillate Wildly'] # Instrumental Track we want to take out
joyDivLyricsFrame = pd.DataFrame(flatDocJV, columns=['Album', 'Title', 'Lyrics']).drop_duplicates(subset=['Lyrics']).dropna()

