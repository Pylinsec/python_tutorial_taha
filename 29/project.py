from tkinter import *
import time

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.config(bg='green')
        self.create_widget()

    def create_widget(self):
        self.btn = Button(self,bg='yellow',width=10,height=2)
        self.btn.place(x=0,y=0)  # relx ijad fasele dar jehat x ha   v rely ijad fasele dar jahat y ha
        # relheight  keshidan shekl darjat y ha  , relwidth keshidan shekl dar jehat x ha
        # nokte mohom   rel ha addadi hastan ashari bin  0 ta 1
        print(self.btn.place_info()['x'])

        for j in range(1,400,30):
            for i in range(1, 400, 10):
                time.sleep(0.1)

                self.btn.place(x=i, y=j , relwidth=i/2000)
                # else:
                #     self.btn.place(x=i, y=j, relwidth=i/(1000+i*100))

                print(self.btn.place_info()['x'],self.btn.place_info()['y'])
                self.update()






App().mainloop()