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
