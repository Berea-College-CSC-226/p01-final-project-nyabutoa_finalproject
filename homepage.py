import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


def show_home_page():
    def go_to_main():
        home_window.destroy()
        import Code  # Importing from code.py
        Code.main()  # Calling the main function from code.py

    home_window = tk.Tk()
    home_window.title("Welcome to Playlist Manager")

    home_window.geometry("800x600")

    try:
        welcome_image = PhotoImage(file="welcome_image.png")
        image_label = tk.Label(home_window, image=welcome_image)
        image_label.pack(pady=10)
    except Exception as e:
        print(f"Error loading image: {e}")

    label = tk.Label(home_window, text="Welcome to the Playlist Manager!", font=("Arial", 16))
    label.pack(pady=20)

    info = ("The Playlist Manager helps you organize your music library.\n\n"
            "Features include:\n"
            "- Add, remove, and shuffle songs\n"
            "- Sort songs by genre, artist, or mood\n"
            "- Search for songs using keywords\n")
    info_label = tk.Label(home_window, text=info, justify="left")
    info_label.pack(padx=20, pady=10)

    start_button = tk.Button(home_window, text="Start Managing Playlists", command=go_to_main)
    start_button.pack(pady=20)

    home_window.mainloop()


if __name__ == "__main__":
    show_home_page()
