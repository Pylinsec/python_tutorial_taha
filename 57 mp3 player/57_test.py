from tkinter import *
from tkinter import PhotoImage , filedialog
import os 
import pygame

win = Tk()
win.geometry('500x500')
win.config(bg='aliceblue')
win.title('MusicPlayer')


frame_list_box = Frame(win)
frame_list_box.pack()

win.mainloop()