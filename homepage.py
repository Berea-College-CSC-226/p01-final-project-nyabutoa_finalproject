######################################################################
# Author: Alpha Nyabuto
# Username: Nyabutoa
#
# Assignment: Final Project - Playlist Manager
#
# Purpose:
# The home page allows users to:
# - Learn about the features of the Playlist Manager
# - Navigate to the main application where they can manage their playlists
#
# The program also utilizes sound and visual elements to create an
# interactive experience, enhancing user engagement with the app from
# the moment it starts.
#
######################################################################
# Acknowledgements:
# - The implementation of this project relies on several Python libraries
#   including Tkinter for the GUI, Pygame for sound playback, and Pillow for image handling.
#   Documentation and resources used:
#   - Pygame Documentation for sound management: https://www.pygame.org/docs/ref/music.html
#   - Pillow Documentation for image handling: https://pillow.readthedocs.io/en/stable/
#   - Python Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
#   - Text-to-Speech service used for generating the welcome sound:
#     https://www.narakeet.com/app/text-to-audio/?projectId=6f94e9ec-821a-460f-a63c-4bd8eb441a37
#
# License:
# Licensed under a Creative Commons Attribution-Noncommercial-Share Alike 3.0
# United States License.
#
# This license allows others to remix, tweak, and build upon the work non-commercially,
# as long as they credit the author and license their new creations under the same terms.
######################################################################

import tkinter as tk
from PIL import Image, ImageTk
import pygame

def show_home_page():
    #Gret the program to have a welcome sound
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("/Users/arphaxadnyabuto/PycharmProjects/p01-final-project-nyabutoa_finalproject/audio/Welcome to the Playl.mp3")
        pygame.mixer.music.play(loops=-1)  # Play the sound in a loop indefinitely
    except pygame.error as e:
        print(f"Error loading sound: {e}")

    def go_to_main():
        pygame.mixer.music.stop()
        home_window.destroy()
        import Code  # Importing from code.py
        Code.main()  # Calling the main function from code.py

    home_window = tk.Tk()
    home_window.title("Welcome to Playlist Manager")

    home_window.geometry("800x600")

    try:
        image_path = "/Users/arphaxadnyabuto/PycharmProjects/p01-final-project-nyabutoa_finalproject/image/welcome_image.png"
        image = Image.open(image_path)

        # Resize the image to a smaller size (e.g., 400x300)
        resized_image = image.resize((400, 300))  # Resize the image to 400x300 pixels

        # Convert the image to a Tkinter-compatible format
        welcome_image = ImageTk.PhotoImage(resized_image)

        # Create a label to display the image
        image_label = tk.Label(home_window, image=welcome_image)
        image_label.pack(pady=10)

        # Keep a reference to the image to prevent it from being garbage collected
        image_label.image = welcome_image

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
