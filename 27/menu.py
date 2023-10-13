#  make menu in tkinter 
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600')
        self.config(bg='aqua')
#         self.create_widget()
# 
#     # function for make menu 
#     def create_widget(self):
#         self.menubar = Menu(self , bg='red')  # make menu 
#         self.config(menu=self.menubar)  # 
# 
#         #make file menu
#         self.file = Menu(self.menubar , tearoff=0) # make item for menu file , edit , help
#         # tearoff agar 0 bashad header dakhel menu ra hazf mikonad 
#         self.menubar.add_cascade(label='File',menu=self.file )
#         # make command in file menu 
#         self.file.add_checkbutton(label='open',command=lambda: print(filedialog.askopenfile())
#         )
#         self.file.add_command(label='exit',command=lambda:self.quit())
# 
# 
#         # help menu 
#         self.help = Menu(self.menubar)
#         self.menubar.add_cascade(label='Help',menu=self.help)
#         self.help.add_command(label='About',command=self.about)
#         self.help.add_command(label='changecolor',command=lambda :self.config(bg=colorchooser.askcolor()[1]))
# 
#     # function for about 
#     def about(self):
#         self.text=  """
#         about writer in 18 semptamber 2022
#         version:1.01
#         name: taha
#         lastname: nemati
#         age:14
#         jog:student
#         class: python programing
#         """
#         messagebox.showinfo(title='About me',message=self.text)   

a = App()      
a.mainloop()  