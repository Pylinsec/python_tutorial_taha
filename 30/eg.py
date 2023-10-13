from tkinter import *


my_w = Tk()
my_w.geometry("615x400")
font=('Times',26,'normal')  
def my_callback(event):
    l1.config(text='You Pressed  : '+ event.char)
def my_t1(*args):
    if(len(t1.get())>5):
        t1.config(bg='red')
    else:
        t1.config(bg='lightgreen')

l1=Label(my_w,text='to Display',bg='yellow',font=font)
l1.grid(row=0,column=0,padx=10,pady=10)
t1=Entry(my_w,bg='lightgreen',font=font)
t1.grid(row=1,column=0,padx=10)

t2=Entry(my_w,bg='lightgreen',font=font)
t2.grid(row=2,column=0,padx=10,pady=10)

my_w.bind("<Key>", my_callback) # Any key is pressed 
my_w.bind("<Return>", lambda e:l1.config(text='Hi')) # Enter Key
t1.bind("<KeyPress>",my_t1)
#t1.bind("<KeyRelease>",my_t1)
t1.bind("<FocusIn>",lambda e:l1.config(text='Welcome'))
t1.bind("<FocusOut>",lambda e:l1.config(text='Thanks'))

my_w.mainloop()













# win = Tk()
# win.geometry('500x600')
# 
# def change_state(event):
#     pass
# def change_color(event):
#     print(event)
# 
#     win.config(bg='lightgreen')
#     
# 
# btn = Label(win,width=20,text='clickme')
# btn.pack()
# print(btn.get)
# btn.bind('<FocusIn>',change_color)  
# 
# win.mainloop()