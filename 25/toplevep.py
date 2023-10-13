from tkinter import *
from tkinter import messagebox

class App():
    def __init__(self , master):
        self.master = master
        self.window =[]
        self.master.geometry('300x400')
        self.master.config(bg='lightpink')
        self.btn = Button(self.master,text='make window',command=self.create_top_level)
        self.btn.pack()
        self.btn_close = Button(self.master,text='close window',command=self.close_window)
        self.btn_close.pack()
        

    def create_top_level(self):
        self.top = Toplevel(self.master)   
        self.window.append(self.top)
         

    def close_window(self):
        if self.window:
            self.top = self.window[-1]
            self.top.destroy()
            # del self.window[-1]
            self.window.pop()
            messagebox.showinfo(title='close',message='closing is successfull')
            self.master.update()
        else:
            messagebox.showerror(title='error',message='list is empty')    




win = Tk()
App(win)
win.mainloop()