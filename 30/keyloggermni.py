from tkinter import *
from datetime import datetime


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.config(bg='lightgreen')

        # make username entry
        self.lbl_username = Label(self,text='username:',font=5 ,bg='lightgreen')
        self.lbl_username.grid(row=0,column=0, pady=25)
        self.username = Entry(self,width=40)
        self.username.grid(row=0,column=1,ipady=10,pady=25)

        # make password entry
        self.lbl_password = Label(self, text='password:', font=5, bg='lightgreen')
        self.lbl_password.grid(row=1, column=0, pady=25)
        self.password = Entry(self, width=40,show='*')
        self.password.grid(row=1, column=1, ipady=10, pady=25)
        # make bind
        self.username.bind('<KeyPress>',self.submit)
        self.password.bind("<KeyPress>",self.submit)
        # make submit button
        self.btn = Button(self, text='submit',width=40,height=3,bg='white',font=10, relief='groove',border=2)
        self.btn.grid(row=2,column=0,columnspan=3,padx=20,pady=20)
        # self.btn.config(command=self.submit)

    # make function for submit information from bind
    def submit(self, event):
        current_time = datetime.now().strftime("date: %Y/%m/%d -->time: %H:%M:%S")
        # print(current_time ,event.keysym)
        with open('temp.txt','a') as file:
            # print(event.char)
            file.write(current_time+"\n")
            file.write(event.char+'\n')


a = App()
a.mainloop()