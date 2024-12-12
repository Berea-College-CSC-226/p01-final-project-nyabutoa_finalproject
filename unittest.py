import unittest
from Code import Playlist, Song

class TestPlaylist(unittest.Testcase):
    def setup(self):
        self.playlist = Playlist()

    def test_add_song(self):
        # Test adding a song to the playlist.
        self.playlist.add_song("Song 1", "Artist 1", "Rock", "Happy", )
        self.assertEqual(len(self.playlist.songs), 1)
        self.assertEqual(self.playlist.songs[0].title, "Song 1")
        self.assertEqual(self.playlist.songs[0].artist, "Artist 1")
        self.assertEqual(self.playlist.songs[0].genre, "Rock")
        self.assertEqual(self.playlist.songs[0].mood, "Happy")

    def test_remove_song(self):
        # Test removing a song from the playlist.
        self.playlist.add_song("Song 1", "Artist 1", "Rock", "Happy", )
        self.playlist.remove_song("Song 1")
        self.assertEqual(len(self.playlist.songs), 0)

    def test_search_song(self):
        # Test searching for a song.
        self.playlist.add_song("Song 1", "Artist 1", "Rock", "Happy", )
        result = self.playlist.search_song("song")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Song 1")
        self.assertEqual(result[0].artist, "Artist 1")

    def test_playlist_shuffle(self):
        # Test shuffling the playlist.
        self.playlist.add_song("Song 1", "Artist 1", "Rock", "Happy")
        self.playlist.add_song("Song 2", "Artist 2", "Pop", "Sad")
        original_order = self.playlist.songs[:]
        self.playlist.playlist_shuffle()
        self.assertNotEqual(self.playlist.songs, original_order)

    def test_sort_songs(self):
        #Test sorting the playlist.
        self.playlist.add_song("Song 1", "Artist 1", "Rock", "Happy")
        self.playlist.add_song("Song 2", "Artist 2", "Pop", "Sad")
        self.playlist.sort_songs("artist")  # Sort by artist
        self.assertEqual(self.playlist.songs[0].title, "Song 1")

if __name__ == '__main__':
    unittest.main()


def main():
    return None