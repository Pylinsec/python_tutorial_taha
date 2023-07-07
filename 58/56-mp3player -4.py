from tkinter import *
from tkinter import PhotoImage , filedialog
import os 
import pygame

win = Tk()
win.geometry('500x500')
win.config(bg='aliceblue')
win.title('MusicPlayer')
#  make varible 
bool_var = BooleanVar()
bool_var.set(False)


pygame.init()
# make frame for listbox
frame_list_box = Frame(win)
frame_list_box.pack()
# make frame for btn and scale 
frame_middle = Frame(win)
frame_middle.pack()
# make frame for btn 
frame_btns = Frame(frame_middle,border=3,relief='solid',)
frame_btns.pack(pady=30,fill='x')
# make frmae for status 
status_frame = Frame(win,bg='black',bd=1,relief=GROOVE,height=30)
status_frame.pack(side=BOTTOM,fill=X)
# make label for timer
status_left = Label(status_frame,text='play',bg='black',fg='white',font=6)
status_left.pack(side='left',padx=10)
status_right = Label(status_frame,text='12:00/12:00',bg='black',fg='white',font=6)
status_right.pack(side='right',padx=10)

# make listbox
song_list = Listbox(frame_list_box,bg='lightyellow',fg='green',width=70,font=5)
song_list.pack(pady=20)

# create player control btn image
back_img = PhotoImage(file='photo/back_img.png')
play_img = PhotoImage(file='photo/play_img.png')
pause_img = PhotoImage(file='photo/pause_img.png')
stop_img = PhotoImage(file='photo/stop_img.png')
forward_img = PhotoImage(file='photo/forward_img.png')


#  define functions 
def open_one_music():
    global dir_name
    song = filedialog.askopenfilename(initialdir='music',title='select one file',
    filetypes=(('music Files','*.mp3'),('music Files','*.wav'),('music Files','*.wma'),('All','*.*')))
    dir_name = os.path.dirname(song)
    base_name = os.path.basename(song)
    song_list.insert(END,base_name)
    song_list.activate(0)
    song_list.select_set(ACTIVE)


# define function for add music 
def open_many_musics():
        song_list.delete(0,END)
        global dir_name
        songs = filedialog.askopenfilenames(initialdir='music',title='select one file',
    filetypes=(('music Files','*.mp3'),('music Files','*.wav'),('music Files','*.wma'),('All','*.*')))
        for song in songs:
            dir_name = os.path.dirname(song)
            base_name = os.path.basename(song)
            song_list.insert(END,base_name)    
        song_list.activate(0)
        song_list.select_set(ACTIVE)       
        song_list.focus_set()



#  make functin for play music 
def play():
    global dir_name
    song = song_list.get(ACTIVE)
    new_song = f"{dir_name}/{song}"
    pygame.mixer.music.load(new_song)
    pygame.mixer.music.play(loops=0)
    
    # define function for stop playing
def stop():
     pygame.mixer.music.stop()
     # 
     song_list.selection_clear(ACTIVE)

# make function for pause and unpause 
def pause(is_paused):
     if is_paused:
          pygame.mixer.music.unpause()
          bool_var.set(False)
     else:
         pygame.mixer.music.pause()
         bool_var.set(True)      

# session 57
#  make function for removing one music
def remove_one_music():
     pygame.mixer.music.stop()
     song = song_list.curselection()[0]
     song_list.delete(song)
#  session 57
# clear listbox 
def clear_list():
     pygame.mixer.music.stop()
     song_list.delete(0,END)

# make function for play forward song 
def forward():
     try:
          global dir_name
          # get current index of song 
          current_index = song_list.index(ACTIVE)
          # update index 
          next_index= current_index + 1
          # clear list box 
          song_list.select_clear(ACTIVE)
          #  jabejaei line 
          song_list.activate(next_index)
          # jebajaei backgrount beraye next
          song_list.select_set(ACTIVE)
          # get next song 
          next_song = song_list.get(next_index)
          # make path for song
          next_song_path = f"{dir_name}/{next_song}"
          # play
          pygame.mixer.music.load(next_song_path)
          pygame.mixer.music.play(loops=0)

     except:
          pass     

# make function for play back song 
def back():
     try:
          global dir_name
          # get current index of song 
          current_index = song_list.index(ACTIVE)
          # update index 
          back_index= current_index - 1
          # clear list box 
          song_list.select_clear(ACTIVE)
          #  jabejaei line 
          song_list.activate(back_index)
          # jebajaei backgrount beraye back
          song_list.select_set(ACTIVE)
          # get back song 
          back_song = song_list.get(back_index)
          # make path for song
          back_song_path = f"{dir_name}/{back_song}"
          # play
          pygame.mixer.music.load(back_song_path)
          pygame.mixer.music.play(loops=0)
     except:
          pass


# create music control btns 
back_btn = Button(frame_btns,image=back_img,command=back)
back_btn.grid(row=0,column=0,padx=10)
play_btn = Button(frame_btns,image=play_img,command=play)
play_btn.grid(row=0,column=1,padx=10)
pause_btn = Button(frame_btns,image=pause_img,command=lambda:pause(bool_var.get()))
pause_btn.grid(row=0,column=2,padx=10)
stop_btn = Button(frame_btns,image=stop_img,command=stop)
stop_btn.grid(row=0,column=3,padx=10)
forward_btn = Button(frame_btns,image=forward_img,command=forward)
forward_btn.grid(row=0,column=4,padx=10)


# create main menu
my_menu = Menu(win)
win.config(menu=my_menu)
# make file menu
file_menu = Menu(my_menu,tearoff=0,font=1)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='add one music',command=open_one_music)
file_menu.add_command(label='add many musics',command=open_many_musics)
# make menu for remove 
remove_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Remove',menu=remove_menu)
remove_menu.add_command(label='delete on music',command=remove_one_music)
remove_menu.add_command(label='clear list',command=clear_list)



# make help menu_--------------------------
help_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='help',menu=help_menu)



win.mainloop()