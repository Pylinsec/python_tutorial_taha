from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('message')
win.geometry('400x300')
# win['bg']='green'
win.config(bg='lightgreen')
var_info =  messagebox.showinfo(title='information',message='my name is Taha Nemati')
var_error = messagebox.showerror(title='error?',message='you have to insert your name!')
var_warning = messagebox.showwarning(title='warning?',message='you are in dangeropus')
print(var_info ,var_error ,var_warning)



win.mainloop()