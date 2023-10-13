from tkinter import *
import os 
import time

win = Tk()


photo =[]
for i in os.listdir('pic'):
    photo.append(PhotoImage(file=f"pic/{i}"))
    

# img = PhotoImage(file="pic/01.png")
def cycle():
    for i in photo:
        while 1:
            for i in photo:
                yield i

for j in cycle():

    lbl = Label(win,image=j)
    lbl.pack()
    time.sleep(1)
    win.update()
    lbl.pack_forget()
    if i == len(photo)-1:
        i=0


win.mainloop()