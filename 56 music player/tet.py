from tkinter import *

root = Tk()
root.geometry('600x500')
listbox = Listbox(root,width=75)

listbox.pack()

data = ['iran','usa','germany','spain']
for i in data:
    listbox.insert(END,i)

def chap():
    index = listbox.get(ACTIVE)
    print(index)

Button(root,text='click',command=chap).pack()   
root.mainloop()