from tkinter import *
from tkinter import PhotoImage

win = Tk()
win.geometry('500x500')
win.config(bg='aliceblue')
# make frame
frame_list_box = Frame(win)
frame_list_box.pack()
frame_btns = Frame(win,border=3,relief='solid',)
frame_btns.pack(pady=30)

# make listbox
song_list = Listbox(frame_list_box,bg='black',fg='green',width=70)
song_list.pack(pady=20)

# create player control btn image
back_img = PhotoImage(file='photo/back_img.png')
play_img = PhotoImage(file='photo/play_img.png')
pause_img = PhotoImage(file='photo/pause_img.png')
stop_img = PhotoImage(file='photo/stop_img.png')
forward_img = PhotoImage(file='photo/forward_img.png')

# create music control btns 
back_btn = Button(frame_btns,image=back_img)
back_btn.grid(row=0,column=0,padx=10)
play_btn = Button(frame_btns,image=play_img)
play_btn.grid(row=0,column=1,padx=10)
pause_btn = Button(frame_btns,image=pause_img)
pause_btn.grid(row=0,column=2,padx=10)
stop_btn = Button(frame_btns,image=stop_img)
stop_btn.grid(row=0,column=3,padx=10)
forward_btn = Button(frame_btns,image=forward_img)
forward_btn.grid(row=0,column=4,padx=10)

win.mainloop()