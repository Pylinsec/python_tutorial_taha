from tkinter import *


win = Tk()
win.geometry('800x600')
#  create main frame 
main_frame = Frame(win,width=800,height=600,bg='yellow',bd=10,relief=GROOVE)
main_frame.pack()
# create frame-top
frame_top = Frame(main_frame,width=800,height=200,bg='lightblue',bd=10,relief=GROOVE)
frame_top.pack(side=TOP)
# create frame_bottom
frame_bottom = Frame(main_frame,width=800,height=400,bg='lightgreen',bd=10,relief=GROOVE)
frame_bottom.pack(side=BOTTOM)
# frame_bottom_left
frame_bottom_left = Frame(frame_bottom,width=300,height=400,bg='pink',bd=10,relief=GROOVE)
frame_bottom_left.pack(side=LEFT)
# frame_bottom_left sub frame
frame_bottom_left_top = Frame(frame_bottom_left,width=300,height=100,bg='pink',bd=10,relief=GROOVE)
frame_bottom_left_top.pack(side='top')
frame_bottom_left_bottom = Frame(frame_bottom_left,width=300,height=300,bg='pink',bd=10,relief=GROOVE)
frame_bottom_left_bottom.pack(side='bottom')
# frame_bottom_right
frame_bottom_right = Frame(frame_bottom,width=500,height=400,bg='green',bd=10,relief=GROOVE)
frame_bottom_right.pack(side='right')
# create frame_bottom_right sub frames 
# create frame_bottom_right sub frames top
frame_bottom_right_top = Frame(frame_bottom_right,width=500,height=150,bg='green',bd=10,relief=GROOVE)
frame_bottom_right_top.pack(side='top')
# create frame_bottom_right sub frames bottom
frame_bottom_right_bottom = Frame(frame_bottom_right,width=500,height=250,bg='green',bd=10,relief=GROOVE)
frame_bottom_right_bottom.pack(side='bottom')
# create frame_bottom_right_bottom sub frames 
# create frame_bottom_right_bottom sub frame left
frame_bottom_right_bottom_left = Frame(frame_bottom_right_bottom,width=150,height=250,bg='pink',bd=10,relief=GROOVE)
frame_bottom_right_bottom_left.pack(side='left')
# frame_bottom_right_bottom_left_sub frame top and bottom
#frame_bottom_right_bottom_left top
frame_bottom_right_bottom_left_top = Frame(frame_bottom_right_bottom_left,width=150,height=50,bg='red',bd=10,relief=GROOVE)
frame_bottom_right_bottom_left_top.pack(side='top')
# frame_bottom_right_bottom_left_bottom
frame_bottom_right_bottom_left_bottom = Frame(frame_bottom_right_bottom_left,width=150,height=200,bg='red',bd=10,relief=GROOVE)
frame_bottom_right_bottom_left_bottom.pack(side='bottom')
# create frame_bottom_right_bottom sub frame right
frame_bottom_right_bottom_right = Frame(frame_bottom_right_bottom,width=350,height=250,bg='purple',bd=10,relief=GROOVE)
frame_bottom_right_bottom_right.pack(side='right')
entry = Entry(frame_bottom_right_bottom_right)
entry.pack(fill=BOTH,expand=True)



win.mainloop()