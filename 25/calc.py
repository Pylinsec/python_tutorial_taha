from tkinter import *
from tkinter import messagebox

class App():
    def __init__(self , master):
        self.str_var = StringVar()
        self.master = master
        self.window =[]
        self.master.title('simple calc')
        self.master.geometry('500x400')
        self.master.config(bg='lightpink')
        self.create_widget()

    def create_widget(self):

        #entry 
        self.entry = Entry(self.master,width=40,font=15 , textvariable=self.str_var)   

        #keys 
        
        self.btn_7 = Button(self.master,text='7',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('7'))
        self.btn_8 = Button(self.master,text='8',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('8'))
        self.btn_9 = Button(self.master,text='9',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('9'))
        self.btn_add = Button(self.master,text='+',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('+'))
        


        self.entry.grid(row=0 ,column = 0,columnspan=4 ,pady=10 ,padx=50)
        self.btn_7.grid(row=1,column=0)
        self.btn_8.grid(row=1,column=1)
        self.btn_9.grid(row=1,column=2)
        self.btn_add.grid(row=1,column=3)
       

    def write(self ,char):
        sum = self.str_var.get()
        self.str_var.set(sum + char)

    def calc(self):
        pass    


win = Tk()
App(win)
win.mainloop()