#import 
from tkinter import *
from tkinter import messagebox


# create class 
class App():
    def __init__(self,master,name):
        self.name = name
        self.master = master
        self.master.geometry('300x400')
        self.master.config(bg='aqua')
        self.master.title(self.name)
        self.create_widget()


# function for crreate widget 
    def create_widget(self):
        self.btn = Button(self.master,text='information',bg='yellow')
        self.btn.pack(expand=True)
        self.btn.config(command=self.message_func)

    def message_func(self):
        # var = messagebox.askokcancel(title='qustion',message='are you satisfy?')
        # print(var) # dar in halat True or False barmigardanad 

        # var1 = messagebox.askquestion(title='ask',message='are you ok?')
        # print(var1) # dar in halat yes , no bargardande mishevad 

        # var2 = messagebox.askyesno(title='agg',message='are you 15 years old?')
        # print(var2) # dar in halat true or false barmigardand
        # var3 = messagebox.askyesnocancel(title='permision',message='do you want to continue?')
        # print(var3)  # true or false or none bargardande mishevad 

        var4 = messagebox.askretrycancel()
        print(var4) # true or false bargardande mishevad 




win = Tk()
app = App(win,'apple' )
win.mainloop()

