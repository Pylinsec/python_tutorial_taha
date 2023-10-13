# make textbox

from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600') # ('widthxheight+x position+y position)
        self.config(bg='aqua')
        self.title("textbox")
        self.str_var= StringVar()
        self.img = PhotoImage(file='horse.png')
        self.create_widget()


    # function for create widget
    def create_widget(self):
        #textbox
        # wrap  agar 'word' bezarim akhat khat agar jaye keleme nabood ono mibareh khat bad
        # vali dar halat 'char' ba harf andaze migireh 
        self.textbox = Text(self,bg='#FFFFFF',font=10 ,wrap='word') 
        self.textbox.pack(pady=25 , padx=25)
        self.textbox.image_create('end',image=self.img)
 

    # define entry for get text 
        self.entry = Entry(self ,textvariable=self.str_var , width=60 , font=5)
        self.entry.pack(ipady=10 ,pady=10)

    # define btn
        self.btn_write = Button(self , text ='write',bg='yellow', command=self.write)
        self.btn_write.pack(side='left',padx=30)
        self.btn_read = Button(self , text ='read',bg='yellow', command=self.read)
        self.btn_read.pack(side='right' , padx=30)

    # function for writing
    def write(self):    
        #self.textbox.insert('m.n','message')  m --> line number az 1 shooro mishe
        # n --> charachter number az 0 shoooro mishevad 
        self.textbox.insert('end',f"{self.str_var.get()}\n")  
        # self.textbox.insert('end','\n')
        self.str_var.set('')

    # function for reading textbox 
    def read(self):
        #self.textbox.get(start,end) start = 'm.n'   end = 'm.n'
        print(self.textbox.get('1.0','end'))
        self.var = self.textbox.get('1.0','end')
        self.textbox.delete('1.0','end')
        self.textbox.insert('end',self.var)


a = App()
a.mainloop()    

class App():
    pass

# for review method 2 to define class 
# root = Tk()
# App()
# root.mainloop()
