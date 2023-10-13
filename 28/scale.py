from tkinter import *
from tkinter import ttk
import time


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600')
        self.config(bg='#000000')
        self.title('scale')
        self.db_var = DoubleVar()
        self.colors = ['red','blue','yellow','aqua','pink','black','green']
        self.create_widget()


    def create_widget(self):

      self.scale = Scale(self,length=1000,variable=self.db_var,from_=1,to=1000,orient='horizontal') # or orient = vertical
      self.scale.pack()
      self.scale.config(troughcolor='red',command=self.zoom ,tickinterval=100 ,width=50)


    def zoom(self ,*arg):
        # self.geometry(f"{self.scale.get()}x{self.scale.get()}")
        # self.geometry(str(self.scale.get())+'x'+str(self.scale.get()))
        if self.scale.get() <= 100:
            self.config(bg=self.colors[0])
        elif self.scale.get() <= 200:
            self.config(bg=self.colors[1])
        elif self.scale.get() <= 300:
            self.config(bg = self.colors[2])
        elif self.scale.get() <= 400:
            self.config(bg = self.colors[3])
        elif self.scale.get() <= 500:
            self.config(bg = self.colors[4])
        elif self.scale.get() <= 600:
            self.config(bg = self.colors[5])
        elif self.scale.get() <= 700:
            self.config(bg = self.colors[6])

        self.update()

 # 3 scale methods ---> scale.get() , scale.set(adad)


a = App()
a
a.mainloop()
