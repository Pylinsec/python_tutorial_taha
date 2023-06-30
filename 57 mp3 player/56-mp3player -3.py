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
# make frame
frame_list_box = Frame(win)
frame_list_box.pack()
frame_btns = Frame(win,border=3,relief='solid',)
frame_btns.pack(pady=30)

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


# define function for add music 
def open_many_musics():
        global dir_name
        songs = filedialog.askopenfilenames(initialdir='music',title='select one file',
    filetypes=(('music Files','*.mp3'),('music Files','*.wav'),('music Files','*.wma'),('All','*.*')))
        for song in songs:
            dir_name = os.path.dirname(song)
            base_name = os.path.basename(song)
            song_list.insert(END,base_name)    



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


# create music control btns 
back_btn = Button(frame_btns,image=back_img)
back_btn.grid(row=0,column=0,padx=10)
play_btn = Button(frame_btns,image=play_img,command=play)
play_btn.grid(row=0,column=1,padx=10)
pause_btn = Button(frame_btns,image=pause_img,command=lambda:pause(bool_var.get()))
pause_btn.grid(row=0,column=2,padx=10)
stop_btn = Button(frame_btns,image=stop_img,command=stop)
stop_btn.grid(row=0,column=3,padx=10)
forward_btn = Button(frame_btns,image=forward_img)
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