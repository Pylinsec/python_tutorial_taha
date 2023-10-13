from tkinter import *

root = Tk()
root.geometry('400x400')
# state in button --? disabled  normal active 
def dis_inable():
    
    if btn2['state'] == DISABLED:
        btn2['state']=NORMAL
    else:
        btn2['state']='disabled'


btn2 = Button(root,bg='lightblue',bd=2,text="clickblue",relief='raised')
btn2.pack(ipadx=10,ipady=10,expand=TRUE)
btn1 = Button(root,bg='lightgreen',bd=2,text="clickgreen",relief='raised',command=dis_inable)
btn1.pack(ipadx=10,ipady=10,expand=TRUE)


root.mainloop()