from tkinter import *

win = Tk()
win.geometry('200x200')
win.configure(bg="lightblue")
lbll = Label(win,bg = "yellow",text="havij",font=5,foreground="red")
lbl2 = Label(win,bg = "blue",text="havij",font=5,foreground="black")
#lbl.pack(side='bottom')  side meqdar 'left' 'right' 'top' 'bottom'  or TOP RIGHT LEFT BOTTOM
lbll.pack(side='top')
lbl2.pack(before=lbll,side="right")# befor= widget , after= widget
win.mainloop()