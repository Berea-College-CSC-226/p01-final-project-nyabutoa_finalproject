import random
import tkinter as tk
from tkinter import filedialog, messagebox

class Song:
    def __init__(self, title, artist, genre, mood, filepath):
        self.title=title
        self.artist=artist
        self.mood=mood
        self.genre=genre
        self.filepath = filepath

def __str__(self):
    return f"{self.title} by {self.artist} | Genre: {self.genre}, Mood: {self.mood}"

class Playlist:
    def __init__(self):
        self.songs= []

    def add_song(self, title, artist, genre, mood, filepath):
        song = Song(title, artist, genre, mood, filepath)
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
        keyword = keyword.lower()
        results = []
        for song in self.songs:
            if keyword in song.title.lower() or keyword in song.artist.lower() or keyword in song.genre.lower() or keyword in song.mood.lower():
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

class PlaylistManagerGui:
    def __init__(self, root, playlist):
        self.root = root
        self.root.title ("Playlist Manager")
        self.playlist = playlist

        self.song_listbox = tk.Listbox (root, width=60, height=15)
        self.song_listbox.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Song", command=self.remove_song)
        self.remove_button.pack(pady=5)

        self.shuffle_button = tk.Button(root, text="Shuffle Playlist", command=self.shuffle_playlist)
        self.shuffle_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Song", command=self.search_song)
        self.search_button.pack(pady=5)

        self.sort_button = tk.Button(root, text="Sort Playlist", command=self.sort_playlist)
        self.sort_button.pack(pady=5)

        self.display_songs()

    def add_song(self):
        title = simple_input("Enter song title:")
        artist = simple_input("Enter artist name:")
        genre = simple_input("Enter genre:")
        mood = simple_input("Enter mood:")

        file_path = filedialog.askopenfilename(title="Select a Music File",
                                               filetypes=[("Audio Files", "*.mp3;*.wav;*.flac")])
        if file_path:
            self.playlist.add_song(title, artist, genre, mood, file_path)
            self.display_songs()
        else:
            messagebox.showwarning("No File Selected", "No file selected. Song not added.")

    def remove_song(self):
        title = simple_input("Enter song title to remove:")
        self.playlist.remove_song(title)
        self.display_songs()
    def shuffle_playlist



def main():
    root = tk.Tk()
    playlist = Playlist()
    app = PlaylistManagerGui(root, playlist)
    root.mainloop()

if __name__ == "__main__":
    main()