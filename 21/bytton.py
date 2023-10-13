from tkinter import *

win = Tk()
win.geometry('400x400')
win.configure(bg="lightblue")
lbll = Label(win,bg = "yellow",text="havij",font=5,foreground="red")
lbl2 = Label(win,bg = "blue",text="havij",font=5,foreground="black")
#lbl.pack(side='bottom')  side meqdar 'left' 'right' 'top' 'bottom'  or TOP RIGHT LEFT BOTTOM
lbll.pack(side='top')
# lbl2.pack(before=lbll,side="right")# befor= widget , after= widget

def chang_bg():
    if btn['bg']=='green':
        btn.config(bg="aqua")
        btn.pack(padx=10 ,pady =20,ipady=40,ipadx=20)   
        lbl2.config(text="tegarg") 
        lbl2.pack(padx=100,pady=80)
    else:
        btn.config(bg="green")
        btn.pack(padx=100 ,pady =100,ipady=40,ipadx=20)  
        lbl2.config(text="toofan") 
        lbl2.pack(padx=10,pady=10)# befor= widget , after= widget


btn = Button(win,text="clickme", bg="green",fg="white",relief="groove",command=chang_bg)
btn.pack(padx=60 ,pady =120,ipady=60,ipadx=40)

win.mainloop()