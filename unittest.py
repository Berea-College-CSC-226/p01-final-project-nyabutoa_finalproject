import unittest
from Code import Playlist

class TestPlaylist(unittest.TestPlaylist):  # Corrected base class name
    def setup(self):
        self.playlist = Playlist()  # Capital "U" in setUp

    def test_add_song(self):
        # Test adding a song to the playlist.
        self.playlist.add_song("Song 1", "Artist 1", "Rock", "Happy", "/path/to/song1.mp3")
        self.assertEqual(len(self.playlist.songs), 1)
        self.assertEqual(self.playlist.songs[0].title, "Song 1")
        self.assertEqual(self.playlist.songs[0].artist, "Artist 1")

    def test_remove_song(self):
        # Test removing a song from the playlist.
        self.playlist.add_song("Song 1", "Artist 1", "Rock", "Happy", "/path/to/song1.mp3")
        self.playlist.remove_song("Song 1")
        self.assertEqual(len(self.playlist.songs), 0)

    def test_search_song(self):
        # Test searching for a song.
        self.playlist.add_song("Song 1", "Artist 1", "Rock", "Happy", "/path/to/song1.mp3")
        result = self.playlist.search_song("song")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Song 1")

if __name__ == '__main__':
    unittest.main()


def main():
    return None