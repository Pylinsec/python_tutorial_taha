from tkinter import *


win = Tk()
win.geometry('800x600')
win.config(bg='lightgreen')

my_menu = Menu(win)
win.config(menu=my_menu)

# make file menu
file_menu = Menu(my_menu,tearoff=0,bg='red')
my_menu.add_cascade(label='View',menu=file_menu)
# make appearance
appearance_menu = Menu(file_menu,tearoff=0,fg='blue')
file_menu.add_cascade(label='Appearance',menu=appearance_menu)
#  create panel position
panel_menu = Menu(appearance_menu,tearoff=0)
appearance_menu.add_cascade(label='panel position',menu=panel_menu)
#  make command 
panel_menu.add_command(label='left',command=lambda:print('left'))
panel_menu.add_command(label='right',command=lambda:print('right'))
panel_menu.add_command(label='bottom',command=lambda:print('bottom'))

win.mainloop()