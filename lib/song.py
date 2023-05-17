class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count()
        Song.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls, song):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, song):
        cls.genres.append(song.genre)
    
    @classmethod
    def add_to_artists(cls, song):
        cls.artists.append(song.artist)
    
    @classmethod
    def add_to_genre_count(self):
        Song.genre_count = {}
        for genre in Song.genres:
            if genre in Song.genre_count:
                Song.genre_count[genre] += 1
            else:
                Song.genre_count[genre] = 1
        print (Song.genre_count)

    @classmethod
    def add_to_artist_count(self):
        Song.artist_count = {}
        for artist in Song.artists:
            if artist in Song.artist_count:
                Song.artist_count[artist] += 1
            else:
                Song.artist_count[artist] = 1
        print (Song.artist_count)