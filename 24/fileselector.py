from tkinter import *
from tkinter import ttk
from tkinter import filedialog


# make or create tkinter class 
win = Tk()
win.geometry('300x300')
win.config(bg='lightgreen')



def select_file():
    # file1 = filedialog.askdirectory() # class str hast 
    # print(file1)
    # file = filedialog.askopenfilename(title='askopoenfilename') # class str hast 
    # print(file)
    files = filedialog.askopenfilenames(title='askopoenfilename') # khoroji tuple hast 
    print(files)
    



#define widget 
btn_select_file = Button(win, text="select file",bg='yellow')
btn_select_file.pack(padx=6,pady=3)

btn_select_file.config(command=select_file)

win.mainloop()