from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.config(bg='green')
        self.list_box=None
        # Tk.__init__(self)
        self.str_var = StringVar()
        self.create_widget()


    def create_widget(self):
        # create listbox
        self.list_box = Listbox(self, bg="yellow", height=10, width=40 ,font=20 )
        self.list_box.pack()
        

        # create label for display selct
        self.lbl = Label(self, textvariable=self.str_var, bg='white',font=15, text='your selection:', width=40 )
        self.lbl.pack(side='bottom', pady=10, expand=True)

        # create down btn
        self.btn_down = Button(self, text='go down', bg='pink', command=self.down)
        self.btn_down.pack(ipady=6, ipadx=12, pady=15 , side='left' ,padx=10)

        # create btn for show listbox selection
        self.btn_click = Button(self, text='show select', bg='pink', command=self.click)
        self.btn_click.pack(ipady=6, ipadx=12, pady=15, side='left',padx=100)

        # create up btn
        self.btn_up = Button(self, text='go up', bg='pink', command=self.up)
        self.btn_up.pack(ipady=6, ipadx=12, pady=15, side='left',padx=10)



        for i in ['taha', 'nemati', 15, 'nohom', 'shahidbaqeri']:
            # self.list_box.insert(index,item) index from 0 to END
            self.list_box.insert(END, i)
        self.list_box.insert(1,'qoli')

        self.list_box.selection_set(0) # line ra  select mikonad
        # self.list_box.delete(0,2) # delete(index,index)

    def down(self):

        self.index = self.list_box.curselection()[0]
        self.list_box.selection_clear(0, END)
        self.list_box.selection_set(self.index + 1)
        self.list_box.activate(self.index + 1)




    def up(self):
        self.index = self.list_box.curselection()[0]# tuple az line barmigardand ke ma entekhabash kardim
        self.list_box.selection_clear(0, END)
        self.list_box.selection_set(self.index - 1)
        self.list_box.activate(self.index + 1) # activate(line number)  khat andakhtanb zire line

    def click(self):
        # print(self.list_box.selection_get())  # selection_get()  khat ra barmigardanad ke ma onra click karde bashim
        self.str_var.set(self.list_box.selection_get())
a = App()

a.mainloop()