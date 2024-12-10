######################################################################
# Author: Alpha Nyabuto
# Username: Nyabutoa
#
# Assignment: Final Project (Project Manager)
#
# Purpose:
# The Playlist Manager project is a program that allows users to manage
# and organize playlists. It provides functionality to:
# - Add, remove, and shuffle songs
# - Sort songs by genre, artist, or mood
# - Search for songs based on specific keywords (title, artist, genre, mood)
#
# This project is designed to improve user experience in managing their
# music library, making it easier to sort, search, and maintain a collection of songs.
#
######################################################################
# Acknowledgements:
# - The implementation of this project is based on various resources,
#   including Python documentation and third-party libraries.
#  https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
#  https://www.w3schools.com/python/python_lambda.asp
# License:
# Licensed under a Creative Commons Attribution-Noncommercial-Share Alike 3.0
# United States License.
#
# This license allows others to remix, tweak, and build upon the work non-commercially,
# as long as they credit the author and license their new creations under the same terms.
######################################################################


import random
import tkinter as tk
from tkinter import filedialog, messagebox

class Song:
    def __init__(self, title, artist, genre, mood, filepath):
        self.title = title
        self.artist = artist
        self.mood = mood
        self.genre = genre
        self.filepath = filepath

    def __str__(self):
        return f"{self.title} by {self.artist} | Genre: {self.genre}, Mood: {self.mood}"

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist, genre, mood, filepath):
        song = Song(title, artist, genre, mood, filepath)
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                self.songs.remove(song)
                print(f"Removed: {song}")
                return
        print(f"Song title '{title}' not found in the playlist.")

    def show_songs(self):
        if not self.songs:
            print("The playlist is empty.")
        else:
            print("\nPlaylist:")
            for song in self.songs:
                print(f"- {song}")

    def search_song(self, keyword):
        keyword = keyword.lower()
        results = []
        for song in self.songs:
            if (keyword in song.title.lower() or
                keyword in song.artist.lower() or
                keyword in song.genre.lower() or
                keyword in song.mood.lower()):
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
            print("Playlist has been shuffled!")
        else:
            print("We cannot shuffle an empty playlist.")

    def sort_songs(self, key):
        if key not in ("genre", "artist", "mood"):
            print(f"Invalid sort key: {key}. Use 'genre', 'artist', or 'mood'.")
            return
        self.songs.sort(key=lambda song: getattr(song, key).lower())

class PlaylistManagerGui:
    def __init__(self, root, playlist):
        self.root = root
        self.root.title("Playlist Manager")
        self.playlist = playlist

        self.song_listbox = tk.Listbox(root, width=60, height=15)
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

    def display_songs(self):
        # Clear the Listbox
        self.song_listbox.delete(0, tk.END)
        # Add songs from the playlist to the Listbox
        for song in self.playlist.songs:
            self.song_listbox.insert(tk.END, str(song))

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

    def shuffle_playlist(self):
        self.playlist.playlist_shuffle()
        self.display_songs()

    def search_song(self):
        keyword = simple_input("Enter keyword to search:")
        result = self.playlist.search_song(keyword)
        self.show_search_results(result)

    def sort_playlist(self):
        key = simple_input("Sort by (genre/artist/mood):")

        if key:  # Check if the input is not None or empty
            key = key.strip().lower()  # Clean up the input

            # Ensure the key is valid before attempting to sort
            if key in ("genre", "artist", "mood"):
                self.playlist.sort_songs(key)
                self.display_songs()
            else:
                messagebox.showerror("Invalid Sort Key", f"Invalid sort key: '{key}'. Use 'genre', 'artist', or 'mood'.")
        else:
            messagebox.showwarning("No Input", "You must enter a valid sort key (genre/artist/mood).")

    def show_search_results(self, result):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Results")
        text_box = tk.Text(search_window, height=10, width=50)
        text_box.insert(tk.END, result)
        text_box.pack(padx=10, pady=10)


def simple_input(prompt):
    input_window = tk.Toplevel()
    input_window.title(prompt)

    label = tk.Label(input_window, text=prompt)
    label.pack(padx=10, pady=5)

    user_input_var = tk.StringVar()  # This variable holds the user's input
    entry = tk.Entry(input_window, textvariable=user_input_var)
    entry.pack(padx=10, pady=5)

    def on_submit():
        input_window.destroy()  # Close the window when the user clicks Submit

    submit_button = tk.Button(input_window, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    input_window.wait_window()  # Wait until the window is destroyed
    return user_input_var.get()  # Return the value from the StringVar


def main():
    root = tk.Tk()
    playlist = Playlist()
    PlaylistManagerGui(root, playlist)
    root.mainloop()

if __name__ == "__main__":
    main()
