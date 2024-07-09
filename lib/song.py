class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre) -> None:

        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        
        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)
        
        Song.add_to_artists(artist)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in Song.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genres:
            cls.genre_count[genre] =cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        
        if artist in cls.artists:
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1





