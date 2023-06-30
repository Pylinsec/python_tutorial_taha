from tkinter import *

root = Tk()
root.geometry('600x500')
listbox = Listbox(root,width=75)

listbox.pack()

data = ['iran','usa','germany','spain']
for i in data:
    listbox.insert(END,i)
songs = listbox.select_set(0,END) # select az koja ta koja 
print(listbox.index(ACTIVE))
def chap():
    country = listbox.get(ACTIVE)
    index = listbox.curselection()[0] # current selection() --> tuple barmigardanad az index active 
    index1 = listbox.index(ACTIVE)
    listbox.delete(0,END) # index tanha feghjat hemoon hazf mishe 
    #  agar omadi range dadi hemnra hazf mikone 
    print(country)
    print(index1)

Button(root,text='click',command=chap).pack()   
root.mainloop()