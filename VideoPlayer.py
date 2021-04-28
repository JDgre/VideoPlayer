import tkinter as tk
import font_manager as fonts
import tkinter.scrolledtext as tkst
import video_library as lib
from tkinter import ttk
from tkinter import *
from video_library import set_rating, increment_play_count
import sqlite3
from PIL import Image, ImageTk


def set_text(text_area, content):
    text_area.delete(1.0, tk.END)
    text_area.insert("1.0", content)


def clear_playlist(playlist):
    playlist.clear()


def set_text_alt(text_area, content):
    text_area.insert(1.0, content)


class Innovate:
    def __init__(self, root):
        self.playlist1 = []
        self.playlist2 = []
        self.playlist3 = []
        self.playlist4 = []
        self.playlist5 = []
        self.options = ["Playlist 1", "Playlist 2", "Playlist 3", "Playlist 4", "Playlist 5"]

        if root is None:
            window = tk.Tk()
            fonts.configure()
        else:
            window = tk.Toplevel(root)

# Window configuration

        icon = PhotoImage(file='1.png')
        window.geometry("1015x560")
        window.title("Video Player")
        window.configure(bg="#79a8f2")
        window.resizable(width=False, height=False)
        window.iconphoto(False, icon)

# Video images

        width = 175
        height = 150
        self.img = Image.open(r'Tom1.png')
        self.img = self.img.resize((width, height), Image.ANTIALIAS)
        self.tom = ImageTk.PhotoImage(self.img)

        self.img2 = Image.open(r'BAT1.png')
        self.img2 = self.img2.resize((width, height), Image.ANTIALIAS)
        self.bat = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open(r'casa1.png')
        self.img3 = self.img3.resize((width, height), Image.ANTIALIAS)
        self.casa = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open(r'som1.png')
        self.img4 = self.img4.resize((width, height), Image.ANTIALIAS)
        self.som = ImageTk.PhotoImage(self.img4)

        self.img5 = Image.open(r'gww1.png')
        self.img5 = self.img5.resize((width, height), Image.ANTIALIAS)
        self.gww = ImageTk.PhotoImage(self.img5)

# background image

        background_image = tk.PhotoImage(file='vidbackground.png')
        background_label = tk.Label(window, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Entry fields

        self.add_to_playlist = tk.Entry(window, width=4)
        self.add_to_playlist.grid(row=6, rowspan=1, column=2, columnspan=3, padx=5, pady=5, sticky="E")

        self.check_video_entry = tk.Entry(window, width=5)
        self.check_video_entry.grid(row=6, rowspan=1, column=10, columnspan=1, padx=10, pady=5, sticky="E")

        self.add_rating_entry = tk.Entry(window, width=5)
        self.add_rating_entry.grid(row=7, rowspan=1, column=10, columnspan=1, padx=10, pady=5, sticky="E")

# Option Menu

        style = ttk.Style()
        style.configure('my.TMenubutton', font=('Helvetica', 12, 'bold'))
        self.clicked = StringVar()
        self.current_playlist = ttk.OptionMenu(window, self.clicked, self.options[0], *self.options,
                                               command=self.option_menu_clicked, style='my.TMenubutton')
        self.current_playlist.grid(row=7, rowspan=1, column=3, columnspan=4, padx=25, pady=5)

# Scrolled text areas

        self.playlist_list = tkst.ScrolledText(window, width=45, height=6, wrap="none")
        self.playlist_list.grid(row=4, rowspan=2, column=1, columnspan=4, padx=10, pady=10, sticky="W")

        self.video_list = tkst.ScrolledText(window, width=45, height=6)
        self.video_list.grid(row=3, rowspan=1, column=1, columnspan=4, padx=10, pady=10, sticky="W")

        self.check_video_list = tkst.ScrolledText(window, width=35, height=6, wrap="none")
        self.check_video_list.grid(row=4, rowspan=1, column=8, columnspan=4, padx=10, pady=10)

# Buttons

        add_btn = tk.Button(window, text="Add to Playlist:", borderwidth=3, height=1,
                            font=("Helvetica", 12), command=self.append_playlists)
        add_btn.grid(row=7, rowspan=1, column=2, columnspan=3, padx=15, pady=5)

        save_btn = tk.Button(window, text="Save Playlist", borderwidth=3, height=1,
                             font=("Helvetica", 12), command=self.save_playlist)
        save_btn.grid(row=8, rowspan=1, column=3, columnspan=4, padx=25, pady=5)

        load_btn = tk.Button(window, text="Load Playlist", borderwidth=3, height=1,
                             font=("Helvetica", 12), command=self.load_playlist)
        load_btn.grid(row=8, rowspan=1, column=2, columnspan=3, ipadx=7, padx=15, pady=5)

        play_btn = tk.Button(window, text="Play Playlist", borderwidth=3, font=("Helvetica", 12),
                             command=self.play_playlist)
        play_btn.grid(row=6, rowspan=1, column=1, columnspan=3, ipadx=6, padx=5, pady=5, sticky="NW")

        reset_btn = tk.Button(window, text="Reset Playlist", borderwidth=3, font=("Helvetica", 12),
                              command=self.reset_playlist)
        reset_btn.grid(row=7, rowspan=1, column=1, columnspan=3, padx=5, pady=5, sticky="NW")

        check_btn = tk.Button(window, text="Check Video", borderwidth=3,
                              font=("Helvetica", 12), command=self.check_video_clicked)
        check_btn.grid(row=6, rowspan=1, column=11, columnspan=4, padx=25, pady=5, sticky="NW")

        add_rating_btn = tk.Button(window, text="Add Rating", borderwidth=3,
                                   font=("Helvetica", 12), command=self.add_rating)
        add_rating_btn.grid(row=7, rowspan=1, column=11, columnspan=3, padx=25, pady=5, sticky="NW")

        list_btn = tk.Button(window, text="List Videos", borderwidth=3,
                             font=("Helvetica", 12), command=self.list_videos_clicked)
        list_btn.grid(row=3, rowspan=1, column=5, columnspan=2, padx=25, pady=5, sticky="NW")

# Labels

        self.space_lbl = tk.Label(window, bg="#0b1c3d", text="", font=("Helvetica", 10))
        self.space_lbl.grid(row=0, rowspan=1, column=0, columnspan=1, padx=10, pady=10, sticky="W")

        self.image_lbl = tk.Label(window, fg="#74b6e6", bg="#588ec2",
                                  text="", font=("Helvetica", 10))
        self.image_lbl.grid(row=1, rowspan=3, column=10, columnspan=4, padx=3, pady=10, sticky="W")

        self.title_lbl = tk.Label(window, bg="#0b1c3d", text="", font=("Helvetica", 20))
        self.title_lbl.grid(row=2, rowspan=1, column=0, columnspan=3, padx=10, pady=10, sticky="W")

        self.status_lbl = tk.Label(window, fg="#FFFFFF", bg="#1c3f87", text="", font=("Helvetica", 14))
        self.status_lbl.grid(row=9, rowspan=1, column=1, columnspan=4, padx=10, pady=10)

        self.default_list_filler()

        if root is None:
            window.mainloop()

    def check_video_clicked(self):
        key = self.check_video_entry.get()
        try:
            images = {"01": self.tom, "02": self.bat, "03": self.casa, "04": self.som, "05": self.gww}
            name = lib.get_name(key)
            select = images[key]
            if name is not None:
                self.image_lbl.configure(image=select)
                director = lib.get_director(key)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)
                video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                set_text(self.check_video_list, video_details)
            else:
                set_text(self.check_video_list, f"Video {key} not found")
            self.status_lbl.configure(text="Check Video button was clicked!")
        except KeyError:
            set_text(self.check_video_list, f"Video {key} not found")

# In check_video_clicked a small dictionary allows the users input to be associated with an image
# this allows for the "self.image_lbl" to display the image associated with the key in the dictionary

    def append_playlists(self):
        key = self.add_to_playlist.get()
        name = lib.get_name(key)
        option = self.clicked.get()
        list_indexed = {"Playlist 1": 0, "Playlist 2": 1, "Playlist 3": 2, "Playlist 4": 3, "Playlist 5": 4}[option]
        p_list_indexed = {"Playlist 1": self.playlist1, "Playlist 2": self.playlist2, "Playlist 3": self.playlist3,
                          "Playlist 4": self.playlist4, "Playlist 5": self.playlist5}[option]
        if name is not None:
            if option == f"Playlist {list_indexed + 1}":
                p_list_indexed.append(key)
                self.display_in_playlist(list_indexed)
                self.status_lbl.configure(text=f"Added to Playlist {list_indexed + 1}!")
        else:
            set_text(self.playlist_list, f"Video {key} not found")

# append_playlists uses two dictionaries to convert values sent by the optionMenu into either the associated list
# or the index number of the value, which is useful for incrementing through

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.video_list, ("Video List:\n" + video_list))
        self.status_lbl.configure(text="List Videos button was clicked!")

#  Takes contents of video library and displays it in "self.video list"

    def default_list_filler(self):
        video_list = lib.list_all()
        set_text(self.video_list, ("Video List:\n" + video_list))
        set_text(self.playlist_list, "Playlists")
        set_text(self.check_video_list, "Check videos and adjust ratings here")

# default_list_filler populates the lists and is run once the window and widgets have been loaded

    def display_in_playlist(self, listnum):
        output = f"Playlist {listnum + 1}: \n"
        playlists = [self.playlist1, self.playlist2, self.playlist3, self.playlist4, self.playlist5]
        for key in playlists[listnum]:
            name = lib.get_name(key)
            play_count = lib.get_play_count(key)
            output += f"{name} - [Play Count:{play_count}]\n"
        set_text(self.playlist_list, "")
        set_text(self.playlist_list, output)

#  display_in_playlist was previously divided into 5 separate functions. By using a
#  loop it now selects a playlist using an index sent to it from another function.

    def option_menu_clicked(self, value):
        current = self.clicked.get()
        list_indexed = {"Playlist 1": 0, "Playlist 2": 1, "Playlist 3": 2, "Playlist 4": 3, "Playlist 5": 4}[current]
        if value == f"Playlist {list_indexed +1}":
            self.display_in_playlist(list_indexed)
            self.status_lbl.configure(text="")

#  option_menu_clicked finds the index of the current selection. This is used to display the correct playlist
#  by sending this value to the "self.display_in_playlist" function.

    def add_rating(self):
        key = self.check_video_entry.get()
        name = lib.get_name(key)
        rate = self.add_rating_entry.get()
        try:
            if 1 <= int(rate) <= 5:
                if name is not None:
                    director = lib.get_director(key)
                    play_count = lib.get_play_count(key)
                    set_rating(key, int(rate))
                    video_details = f"{name}\n{director}\nrating: {rate}\nplays: {play_count}"
                    set_text(self.check_video_list, video_details)
                    video_list = lib.list_all()
                    set_text(self.video_list, ("Video List:\n" + video_list))
                else:
                    set_text(self.check_video_list, f"Video {key} not found")
            else:
                set_text(self.check_video_list, f"Please enter a rating between 1 and 5")
        except ValueError:
            set_text(self.check_video_list, f"Please enter a number")

# add_rating checks firstly if the value entered is between 1 and 5, if not, an error message appears.
# If it passes that statement, the next requires the rating entered to be between 1 and 5. If the user
# enters something other than an integer or leaves the field empty, the try/except block handles this and
# asks the user to enter a number

    def play_playlist(self):
        option = self.clicked.get()
        p_list_indexed = {"Playlist 1": self.playlist1, "Playlist 2": self.playlist2, "Playlist 3": self.playlist3,
                          "Playlist 4": self.playlist4, "Playlist 5": self.playlist5}[option]
        list_indexed = {"Playlist 1": 0, "Playlist 2": 1, "Playlist 3": 2, "Playlist 4": 3, "Playlist 5": 4}[option]
        for key in p_list_indexed:
            increment_play_count(key)
            self.display_in_playlist(int(list_indexed))
            self.status_lbl.configure(text="Playing playlist...")

# The play_playlist function takes the value of the option menu and iterates through the keys in the associated list.
# It then runs them through the increment_play_count function adding one to each key it finds

    def reset_playlist(self):
        conn = sqlite3.connect('Innovate_db1.db')
        c = conn.cursor()
        option = self.clicked.get()
        p_list_indexed = {"Playlist 1": self.playlist1, "Playlist 2": self.playlist2, "Playlist 3": self.playlist3,
                          "Playlist 4": self.playlist4, "Playlist 5": self.playlist5}[option]
        list_indexed = {"Playlist 1": 0, "Playlist 2": 1, "Playlist 3": 2, "Playlist 4": 3, "Playlist 5": 4}[option]
        if option == f"Playlist {list_indexed + 1}":
            clear_playlist(p_list_indexed)
            self.display_in_playlist(int(list_indexed))
            c.execute(f"DELETE FROM playlist{list_indexed + 1}")
            conn.commit()
            self.status_lbl.configure(text="Playlist cleared!")

# The reset_playlist function takes the value of the current option selected in the option menu and uses
# an f string to have the if statement process the associated index number. The variable "list_indexed" is used
# to decide which playlist should be cleared and the functions "clear_playlist" and c.execute(..) will clear the list
# and the SQL table

    def save_playlist(self):
        conn = sqlite3.connect('Innovate_db1.db')
        c = conn.cursor()

        option = self.clicked.get()
        p_list_indexed = {"Playlist 1": self.playlist1, "Playlist 2": self.playlist2, "Playlist 3": self.playlist3,
                          "Playlist 4": self.playlist4, "Playlist 5": self.playlist5}[option]
        list_indexed = {"Playlist 1": 0, "Playlist 2": 1, "Playlist 3": 2, "Playlist 4": 3, "Playlist 5": 4}[option]

        c.execute(f"DELETE FROM playlist{list_indexed + 1}")
        conn.commit()
        for key in p_list_indexed:
            entry = (str(key))
            if option == f"Playlist {list_indexed + 1}":
                c.execute(f"INSERT INTO playlist{list_indexed + 1} (key)VALUES('{entry}')")
                conn.commit()
            self.status_lbl.configure(text="Playlist saved!")

# The save_playlist function uses the option menu value to decide which playlist should have each of the keys found in
# the associated list in "p_list_indexed" inserted into the associated SQL table.

    def load_playlist(self):
        conn = sqlite3.connect('Innovate_db1.db')
        c = conn.cursor()

        option = self.clicked.get()
        p_list_indexed = {"Playlist 1": self.playlist1, "Playlist 2": self.playlist2, "Playlist 3": self.playlist3,
                          "Playlist 4": self.playlist4, "Playlist 5": self.playlist5}[option]
        list_indexed = {"Playlist 1": 0, "Playlist 2": 1, "Playlist 3": 2, "Playlist 4": 3, "Playlist 5": 4}[option]

        c.execute(f"SELECT key FROM playlist{list_indexed + 1}")
        items = c.fetchall()
        p_list_indexed.clear()
        for item in items:
            for key in item:
                p_list_indexed.append(key)
                self.display_in_playlist(list_indexed)
        self.status_lbl.configure(text="Playlist loaded!")


# The load_playlist function uses the option menu value to choose a playlist, it then iterates through the
# "key" column in the associated SQL table and retrieves the key in a particular format. The above code
# clears the contents of a list before loading another into it
#
# If i attempt to load a playlist that has video 03 stored in it and i only use "for item in items:"
# the return will be ('03',), the line "for key in item:" then returns precisely 03.
# which can be used in other functions.


if __name__ == "__main__":
    Innovate(None)
