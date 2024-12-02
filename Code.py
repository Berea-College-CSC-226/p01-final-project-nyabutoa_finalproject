import random

class Song:
    def __init__(self, title, artist, genre,mood):
        self.title=title
        self.artis=artist
        self.mood=mood
        self.genre=genre

def __str__(self):
        return f"{self.title} by {self.artist} | Genre: {self.genre}, Mood: {self.mood}"

class Playlist:
    def __init__(self):
        self.songs= []

    def add_song(self, title, artist, genre, mood):
        song = Song(title, artist, genre, mood)
        self.songs.append(song)
        print(f"Added:{song}")
    def remove_song(self,title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                self.songs.remove(song)
                print(f"Removed:{song}")
                return
        print(f"Song title '{title}' not found in the playlist.")
    def show_songs(self):
        if not self.songs:
            print("The playlist is empty.")
        else:
            print("\nPlaylist:")
            for song in self.songs:
                print(f"- {song}")
    def search_song(self,keyword):
        keyword = keyword.lower
        results = []
        for song in self.songs:
            if keyword in song.title.lwoer() or keyword in song.artist.lower() or keyword in song.genre.lower() or keyword in song.mood.lower():
                results.append(song)
        if results:
            print(f"\nSearch results for '{keyword}':")
            for song in results:
                print(f"- {song}")
        else:
            print(f"No songs found for '{keyword}'.")
    def playlist_shuffle(self):
        if self.songs:
            random.shuffle(self.songs)
            print("playlist has been shuffled!")
        else:
            print("We cannot shuffle an empty playlist.")
    def sort_songs(self, key):
        if key not in ("genre","artist","mood"):
            print (f"invalid sort key: {key}. use 'genre', 'artist' or 'mood'.")
            return
        self.songs.sort(key=lambda song:getattr(song, key).lower())

def main():
    manager = Playlist()
if __name__ == "__main__":
    main()