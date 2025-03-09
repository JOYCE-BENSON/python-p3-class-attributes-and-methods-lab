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
        
        Song.add_song_to_count()
        
        # Update genre tracking
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
            Song.genres.append(genre)
        Song.genre_count[genre] += 1
        
        # Update artist tracking
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
            Song.artists.append(artist)
        Song.artist_count[artist] += 1
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls):
        # This method is now just for consistency with the requirements
        # The unique genres are already handled in __init__
        pass
    
    @classmethod
    def add_to_artists(cls):
        # This method is now just for consistency with the requirements
        # The unique artists are already handled in __init__
        pass
    
    @classmethod
    def add_to_genre_count(cls):
        # This method is now just for consistency with the requirements
        # The genre count is already handled in __init__
        pass
    
    @classmethod
    def add_to_artist_count(cls):
        # This method is now just for consistency with the requirements
        # The artist count is already handled in __init__
        pass
    pass
