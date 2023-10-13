from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk

class App():
    def __init__(self,master):
        self.master = master
        self.master.title('combo')
        self.master.geometry('300x400')
        self.master.config(bg='skyblue')
        self.month = ['january','febuary','march','may','april','june','july','aguest','septemper','october','november','desember']
        self.combo_var = StringVar()
        self.spin_var = StringVar()
        self.combo_var.set('select birthmonth')
        self.create_widget()
        


    def create_widget(self):
        # values=[] , in method meqdar be combo midehad 
        # textvaariable = Stringvar() , beraye neshan daden heman values ha 
        # self.combo_var.set(self.month[0])
        self.combo_box = Combobox(self.master ,values=self.month ,textvariable=self.combo_var)
        self.combo_box.pack(pady=20)
        #postcommand mesl command hast 
        self.combo_box.config(state='readonly',postcommand=self.print_combo_get)
        
        #create btn for printing 
        self.btn_print = Button(self.master,text='chapkon',bg='lightgreen' ,bd=5,relief=GROOVE)
        self.btn_print.pack(after=self.combo_box , anchor=NE)
        self.btn_print.config(command=self.print_combo_get)


        #create spinbox
        #increment(adad): stpe azfeh kardan 

        #self.spin_box = Spinbox(self.master ,from_=1,to=31 ,increment=2, state='readonly' , textvariable=self.spin_var ,command=self.print_combo_get)
        self.spin_box = Spinbox(self.master ,from_=1,to=31 ,values=self.month,state='readonly' , textvariable=self.spin_var ,command=self.print_combo_get)
        self.spin_box.pack()

        
    def print_combo_get(self):
        if self.combo_var.get() != 'select birthmonth':
            print(f" your birth date is {self.combo_var.get()} {self.spin_var.get()}")
           




win = Tk()
App(win)   
win.mainloop()     