# bind and even   format  -->  widget.bind("<>",function(hander))
from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.config(bg='#000000')
        self.btn = Button(self, text='clickme',width=20,height=5,bg='white')
        self.btn.pack(pady=20)
        self.make_bind()



    def make_bind(self):

        #  command
        # self.bind("<>",handler(function))
        #keybosrd :  KeyPress , Key , KeyRelease
        # self.bind("<KeyPress>", self.print_event) keypress yani har kelid ke press shevad
        # self.bind("<Key>", self.print_event) key yani har kelid khas  press shevad
        # self.bind("<KeyRelease>", self.print_event) keypress yani har kelid ke release shevad

        # #  mouce
        # Button :  khodesh se kelid mouce hast har vaqt feshordeh shevasnd
        # ButtonRelease : vaqti click reha shevad
        #Motion  : harvaqt mouse rooye widget ma amad active mishe
        #Enter:  vaqti active besho ke vared qesmat widget shodi
        #Leave :  vaqti active mishevad ke az oon nahieh widget bezenim biroon
        #MouseWheel: --> vaqti active mishevad ke mouse wheel scroll shevad
        # self.bind("<KeyRelease>", self.print_event)


        # FocusIn  vaqti ke dakhel nahieh widget click shevad active mishe
        # FocusOut vaqti ke biroon naheih widget click shevad active mishe
        # Configure : --> vaqti active mishe ke config oon widget avaz sheved mesl width height border font ...

        self.bind("<FocusOut>", self.print_event) # in bind se adad barmigardanad 1 --> left click  2 wheel  3--> right click
        self.btn.config(bg='red' , font=25)
    # Button-1 beraye left click  Button-2 wheel Button-3 right click
    # in Button ba widget Button farq darad inja mouce hast
    # Enter be manaye key enter rooye keyboard nist    oon Return hast


    def print_event(self, event):
        self.unbind('<FocusOut>')
        # print(event.keysym, end=' ')
        # print(event.char)
        print(event)


a = App()
a.mainloop()