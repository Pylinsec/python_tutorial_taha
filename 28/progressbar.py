from tkinter import *
from tkinter import ttk
import time


class App(Tk):
    def __init__(self):
        super().__init__()
        self.progress = None
        self.btn_start = None
        self.btn_stop = None
        self.geometry('600x600')
        self.config(bg='#000000')
        self.db_var = DoubleVar()
        self.create_widget()
        # self.loop()


    def create_widget(self):
        self.progress = ttk.Progressbar(self, length=200,value=1.5, variable=self.db_var)  # vertical be manay amoodi hast
        # horizontal  ofoqi
        self.progress.pack(ipady=10)
        self.progress.config(mode='determinate')  # determinate --> vaqti hamechi moshakhas hast
        # indeterminate  bishtar beryae jaha ei ast ke ma nemidonim cheqadr tool mikeshe

        self.btn_start = Button(self, text="start", command=lambda:self.progress.start(), bg='yellow', height=5, width=10)
        self.btn_start.pack()
        self.btn_stop = Button(self, text="stop", command=lambda: self.progress.stop(), bg='yellow', height=5, width=10)
        self.btn_stop.pack()
        self.btn_next = Button(self, text="next", command=lambda: self.progress.step(2), bg='yellow', height=5,width=10)
        self.btn_next.pack()
        self.btn_back = Button(self, text="back", command=lambda: self.progress.step(-20), bg='yellow', height=5, width=10)
        self.btn_back.pack()


    def loop(self):
        for i in range(100):
            time.sleep(0.2)
            self.db_var.set(i)
            self.update()




a = App()
a
a.mainloop()
