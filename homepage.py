import tkinter as tk
from PIL import Image, ImageTk

def show_home_page():
    def go_to_main():
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
