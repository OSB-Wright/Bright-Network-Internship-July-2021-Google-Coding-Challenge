"""A video playlist class."""
from .video_library import VideoLibrary

class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_name):
        self.name = str(playlist_name) #stores name of playlist
        self.playlist_video_ids = [] # stores video ids for videos in the playlist

        
