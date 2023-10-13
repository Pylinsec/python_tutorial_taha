from tkinter import *

# define mainloop
win = Tk()
win.geometry('200x200')
#
int_var = IntVar()
int_var.set(0)
#define Entry 
entry = Entry(win,font=20,bg='lightgreen',textvariable=int_var)
entry.pack()
entry2 = Entry(win,font=20,bg='lightblue') #  state in entry 3 halat darad: 'disabled' , 'normal' , 'readonly' 
entry2.pack()
# photo
img_up = PhotoImage(file='up.png')
img_down = PhotoImage(file='down.png')
#define btn 
btn_up = Button(win,text ="+",image=img_up)
btn_up.pack(side=RIGHT)
btn_down = Button(win,text ="-",image=img_down)
btn_down.pack(side=LEFT)

#defube function 
def inc(counter): # 
    entry2.config(state='disabled')
    global int_var
    int_var.set(counter)
    btn_up.config(command=lambda:inc(counter+1))
    btn_down.config(command=lambda:dec(counter-1))
    win.update()


def dec(counter):
    global int_var
    int_var.set(counter)
    btn_down.config(command=lambda:dec(counter-1))
    btn_up.config(command=lambda:inc(counter+1))
    win.update()

#update btns 
btn_up.config(command=lambda:inc(1000))
btn_down.config(command=lambda:dec(0))

win.mainloop()