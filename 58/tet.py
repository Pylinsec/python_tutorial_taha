from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('600x500')


entry = Entry(root,width=20)
entry.pack()
entry.focus_set()
root.focus_set()
listbox = Listbox(root,width=75,selectbackground='lightpink',selectborderwidth=1,selectforeground='blue')
listbox.pack()

data = ['Iran','USA','Germany','spain']
for i in data:
    listbox.insert(END,i)


def chap():
    # print(listbox.selection_get())
    # current = listbox.curselection()[0]
        # get index current item
    current = listbox.index(ACTIVE)
    current += 1
    if current < listbox.size():
        # get song 
        next = listbox.get(current)
        # clear listbox 
        # listbox.selection_clear(0,END)
        listbox.selection_clear(ACTIVE)
        # bordan line zir item 
        listbox.activate(current)#  current addad hast
        #  jabejaei background --> current addad hast
        listbox.selection_set(current)
    else:
        print('out')

Button(root,text='next',command=chap).pack()   
root.mainloop()