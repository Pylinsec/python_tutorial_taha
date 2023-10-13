from tkinter import *
from tkinter import ttk
# command - state - value-variable - textvariable - select - deselct 
win = Tk()
win.geometry('300x300')
win.config(bg='lightgreen')

# variable
# str_var = StringVar()
global radio_python
int_var = IntVar()
list_lan = ['python','c++','html','javascript']




#define radio button
radio_python = Radiobutton(win,text ='python',indicatoron=0,value=0,variable=int_var ) # indicatoron shekl be mostetil avaz mikonad 
radio_python.pack()
radio_cpp = Radiobutton(win,text ='cpp',value=1,variable=int_var )
radio_cpp.pack()
radio_html = Radiobutton(win,text ='html',value=2,variable=int_var )
radio_html.pack()
radio_javascript = Radiobutton(win,text ='javascript' ,value= 3,variable=int_var )
radio_javascript.pack()
radio_python.select()

#define buttom
btn_submit = Button(win , text='submit' , width=10,height= 3)
btn_submit.pack(side=BOTTOM)
btn_select = Button(win , text='select/deselect' , width=10,height= 3)
btn_select.pack(side=LEFT)

# define function 
def select_lan():
    var1 = int_var.get()
    print(list_lan[var1])
    print(radio_python['value'])
    print(radio_python['state'])


list_var_radio = [radio_python ,radio_cpp, radio_html,radio_javascript]
def sel_desel():
    var1 = int_var.get()
    list_var_radio[var1].config(state='disabled')
    if (radio_javascript['state'] == 'disabled' and 
    radio_cpp['state'] == 'disabled' and
    radio_html['state'] == 'disabled' and
    radio_python['state'] == 'disabled'):
        for i in list_var_radio:
            i.config(state='normal')

    
    
    
    
    
    


#connfig
radio_python.config(command=lambda:print(int_var.get()))
btn_submit.config(command=select_lan)
btn_select.config(command=sel_desel)
win.mainloop()