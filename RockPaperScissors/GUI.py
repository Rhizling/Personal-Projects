import tkinter as tk
from tkinter import Tk

import PIL
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage


def display_win(round_number: int):
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Round {0}".format(round_number))
    window.configure(background='white')
    win_image = PIL.Image.open('/Users/saimadhavsakhamuri/Documents/Code Folder/RockPaperScissors Images/Win.png')
    win_image: PhotoImage = PIL.ImageTk.PhotoImage(win_image)
    panel = tk.Label(window, image=win_image)
    panel.place(x=80, y=125)
    window.mainloop()


def display_loss(round_number: int):
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Round {0}".format(round_number))
    window.configure(background='black')
    win_image = PIL.Image.open('/Users/saimadhavsakhamuri/Documents/Code Folder/RockPaperScissors Images/Defeat.jpeg')
    win_image = win_image.resize((275, 250), Image.ANTIALIAS)
    win_image = PIL.ImageTk.PhotoImage(win_image)
    panel = tk.Label(window, image=win_image)
    panel.place(x=110, y=125)
    window.mainloop()


def display_draw(round_number: int):
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Round {0}".format(round_number))
    window.configure(background='gray')
    win_image = PIL.Image.open('/Users/saimadhavsakhamuri/Documents/Code Folder/RockPaperScissors Images/Draw.jpeg')
    win_image = win_image.resize((275, 250), Image.ANTIALIAS)
    win_image = PIL.ImageTk.PhotoImage(win_image)
    panel = tk.Label(window, image=win_image)
    panel.place(x=110, y=125)
    window.mainloop()


