from tkinter import *
import random


win = Tk()
win.geometry('400x400')
win.config(bg = 'aqua')

list_adad = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
random.shuffle(list_adad)

# create function
def swap(btn):
    if free_btn.grid_info()['row'] == btn.grid_info()['row'] and abs(free_btn.grid_info()['column'] - btn.grid_info()['column']) == 1:
        temp = free_btn.grid_info()['column']
        free_btn.grid(column=btn.grid_info()['column'])
        btn.grid(column=temp)
    elif free_btn.grid_info()['column'] == btn.grid_info()['column'] and abs(free_btn.grid_info()['row'] - btn.grid_info()['row']) == 1:
        temp = free_btn.grid_info()['row']
        free_btn.grid(row=btn.grid_info()['row'])
        btn.grid(row=temp)




# create button
free_btn = Button(win,width=10,height=5,bg='aqua',text='',border=0)
btn1 = Button(win,width=10,height=5,bg='lightgreen',text=1,command=lambda:swap(btn1))
btn2 = Button(win,width=10,height=5,bg='lightgreen',text=2,command=lambda:swap(btn2))

btn3 = Button(win,width=10,height=5,bg='lightgreen',text=3,command=lambda:swap(btn3))
btn4 = Button(win,width=10,height=5,bg='lightgreen',text=4,command=lambda:swap(btn4))
btn5 = Button(win,width=10,height=5,bg='lightgreen',text=5,command=lambda:swap(btn5))

btn6 = Button(win,width=10,height=5,bg='lightgreen',text=6,command=lambda:swap(btn6))
btn7 = Button(win,width=10,height=5,bg='lightgreen',text=7,command=lambda:swap(btn7))
btn8 = Button(win,width=10,height=5,bg='lightgreen',text=8,command=lambda:swap(btn8))

# grid()
free_btn.grid(row=list_adad[0][0],column=list_adad[0][1],padx=10,pady=10)
btn1.grid(row=list_adad[1][0],column=list_adad[1][1],padx=10,pady=10)
btn2.grid(row=list_adad[2][0],column=list_adad[2][1],padx=10,pady=10)

btn3.grid(row=list_adad[3][0],column=list_adad[3][1],padx=10,pady=10)
btn4.grid(row=list_adad[4][0],column=list_adad[4][1],padx=10,pady=10)
btn5.grid(row=list_adad[5][0],column=list_adad[5][1],padx=10,pady=10)

btn6.grid(row=list_adad[6][0],column=list_adad[6][1],padx=10,pady=10)
btn7.grid(row=list_adad[7][0],column=list_adad[7][1],padx=10,pady=10)
btn8.grid(row=list_adad[8][0],column=list_adad[8][1],pady=10)

# print(btn1.grid_info()['column'],btn1.grid_info()['row'])
# print(btn2.grid_info()['column'],btn2.grid_info()['row'])


win.mainloop()