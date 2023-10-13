from tkinter import *

# define mainloop
win = Tk()
win.geometry('200x200')

str_var1 = StringVar()
str_var2 = StringVar()
check_man = Checkbutton(win,text='man',variable=str_var1,offvalue='0',onvalue=1)
check_man.pack()
check_woman = Checkbutton(win,text='woman',variable=str_var2,offvalue='0',onvalue='1')
check_woman.pack()

def exit_func():
    win.quit()


exit = Button(win,text='exit',command=exit_func).pack()

# state in checkbutton 'normal' or 'disabled' , 'active'
check_man.select()
def select():
    # check_man.config(state='disabled')
    check_man.toggle()  # toggle harchi bood baraks mikone   #select  tick mizenad ,deselect  tick barmidarad 
    print(str_var2.get())

check_man.config(command=lambda:print(str_var1.get()))
check_woman.config(command=select)

win.mainloop()