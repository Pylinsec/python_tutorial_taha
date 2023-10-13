from re import L
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser


# create tkinter 
win = Tk()
win.geometry('300x300')
win.config(bg='lightgreen')

#define function 
def select_color():
   color = colorchooser.askcolor()
   btn_select_color.config(bg=color[1])

#define widget 
btn_select_color = Button(win, text="select color",bg='yellow')
btn_select_color.pack(padx=6,pady=3)

btn_select_color.config(command=select_color)
win.mainloop()