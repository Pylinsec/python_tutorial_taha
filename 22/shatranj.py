from tkinter import *
import time

win = Tk()
win.geometry()
win.config(bd=5,relief='sunken',padx=10,pady=10)
# win.config(bg='yellow')
colors = ['white','black','white','black']
for i in range(8):
    frame = Frame(win )  # widget hast ke mitonim ba an mekan widget haye  dige modiriat konim 
    # frame.pack(fill = 'both',expand=True)
    frame.pack()
    for j in range(8):
        if i % 2 ==0:
            color=['black','white']
            lbl= Label(frame,bg=color[j % 2],width=8,height=4)
            lbl.pack(side='left')
        if i % 2 ==1:
            color=['white','black']
            lbl= Label(frame,bg=color[j % 2],width=8,height=4)
            lbl.pack(side='left')

# revesh dovoom

# for i in range(8):
#     for j in range(8):
#         if i % 2 ==0:
#             color=['black','white']
#             lbl= Label(win,bg=color[j % 2],width=8,height=4)
#             lbl.grid(row=i,column=j)
#         if i % 2 ==1:
#             color=['white','black']
#             lbl= Label(win,bg=color[j % 2],width=8,height=4)
#             lbl.grid(row=i,column=j)

win.mainloop()



