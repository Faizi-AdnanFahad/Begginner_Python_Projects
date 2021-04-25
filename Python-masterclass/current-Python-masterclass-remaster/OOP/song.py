class Song:
    """Class to represent a song

    Attributes:
    title (str): The title of  the song
    artist: (Artist): An artist object representing the song creator
    duration (int): The duration of the song is in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
            name (str): The name of the album.
            year (int): The year the album was released.
            artist (Artist): The artist responsible for the album.
                If not specified, the artist will default to an artist
                with the name "Various Artists".
                tracks (List(Song)): A list of the songs on the album.

    Methods:
        add_Song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        self.tracks = []
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

    # Mutator
    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional(int)): If specified, the song will be added to the position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """
        if position is not None:
            self.tracks.insert(position, song)
        else:
            self.tracks.append(song)


class Artist:
    """" Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (listAlbum): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): album object ot add to the list.
                If the album is already present, it will no be added again (although this is yet to be implemented)
        """
        self.albums.append(album)













