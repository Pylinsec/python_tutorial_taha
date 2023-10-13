from ast import Delete
from tkinter import *

win = Tk()
win.geometry('300x300')
# str_var = StringVar()  # -- yek nmoone ya shai az class string var dar tkinter 
# str_var.set('iran')
# print(str_var.get())

# int_var = IntVar  # yek class dade az no integer
# int_var = 123434
# print(int_var)

# double_va = DoubleVar  # adad ashari daresh qerar miger
# bool_var = BooleanVar # peziresh just True and false  or 1 and 0

def print1():
    # lbl.config(text=f"username shom as {entry1.get()}")
    # lbl.config(text=f"password shom as {entry2.get()}")
   # entry1.insert(0,"username")  # inser(index,"string")  jehat neveshtan dar enry 
   #entry1.delete(0,END)  # inser(start index,endindex) jehat clear kardan entry 
#    str_var.set(entry2.get())
    root = Tk()
    root.geometry('300x300')
    win.quit()
    win.update()
    root.mainloop()

str_var = StringVar()


btn2 = Button(win,bg='lightblue',bd=2,text="clickblue",relief='raised',command=print1)
btn2.pack(ipadx=10,ipady=10,expand=TRUE)

lbl2 = Label(win,text= 'username')
lbl2.pack()
entry1 = Entry(win,font=10,bg='yellow',textvariable=str_var)

entry1.pack()


lbl2 = Label(win,text= 'password')
lbl2.pack()
entry2 = Entry(win,font=10,bg='yellow',show="*")  # show jehat security 
entry2.pack()


lbl = Label(win)
lbl.pack()
win.mainloop()