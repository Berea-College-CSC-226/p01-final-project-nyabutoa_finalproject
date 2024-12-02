import random
import tkinter as tk
from tkinter import filedialog

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

def main():
    manager = Playlist()
    while True:
        print ("\nPlaylist Manager:")
        print("1. Add Song")
        print("2. Remove songs")
        print("3. Display Songs")
        print("4. Search Song")
        print("5. Shuffle Playlist")
        print("6. Sort Songs")
        print("7. Exit")

        choice = input ("Enter yur choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            genre = input("Enter genre: ")
            mood = input("Enter mood: ")
            # Ask the user to select a file path
            file_path = filedialog.askopenfilename(title="Select a Music File", filetypes=[("Audio Files", "*.mp3;*.wav;*.flac")])
            if file_path:  # Ensure the file path is valid before adding the song
                manager.add_song(title, artist, genre, mood, file_path)
            else:
                print("No file selected. Song not added.")
        elif choice == "2":
            title = input ("With a title, what song would you like to remove")
            manager.remove_song(title)
        elif choice == "3":
            manager.show_songs()
        elif choice == "4":
            keyword = input("Enter a keyword to search")
            manager.search_song(keyword)
        elif choice == "5":
            manager.playlist_shuffle()
        elif choice == "6":
            key = input("Sort by (genre/artist/mood): ").strip().lower()
            manager.sort_songs(key)
        elif choice == "7":
            print("Exiting The Playlist Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()