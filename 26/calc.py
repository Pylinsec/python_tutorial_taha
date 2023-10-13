
from tkinter import *
from tkinter import messagebox

class App():
    def __init__(self , master):
        self.str_var = StringVar()
        self.master = master
        self.window =[]
        self.master.title('simple calc')
        self.master.geometry('500x500')
        self.master.config(bg='gray')
        self.create_widget()
        self.flag = False
        self.char_flag = False
        self.counter = 0

    def create_widget(self):

        #entry 
        self.entry = Entry(self.master,width=40,font=30,textvariable=self.str_var)   

        #keys 7 ,8 , 9 + 
        self.btn_7 = Button(self.master,text='7',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('7'))
        self.btn_8 = Button(self.master,text='8',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('8'))
        self.btn_9 = Button(self.master,text='9',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('9'))
        self.btn_add = Button(self.master,text='+',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('+'))
      
        # 4 ,5 ,6 -
        self.btn_4 = Button(self.master,text='4',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('4'))
        self.btn_5 = Button(self.master,text='5',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('5'))
        self.btn_6 = Button(self.master,text='6',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('6'))
        self.btn_sub = Button(self.master,text='-',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('-'))
        # 1,2,3,*
        self.btn_1 = Button(self.master,text='1',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('1'))
        self.btn_2 = Button(self.master,text='2',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('2'))
        self.btn_3 = Button(self.master,text='3',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('3'))
        self.btn_mul = Button(self.master,text='x',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('*'))
        # c , . , -
        self.btn_clear = Button(self.master,text='clear',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=self.clear)
        self.btn_clear.config(command=self.clear)
        self.btn_zero = Button(self.master,text='0',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('0'))
        self.btn_dot = Button(self.master,text='.',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('.'))
        self.btn_div = Button(self.master,text='/',font= 6,bg='yellow',activebackground='lightgreen',height=3,width=8 ,command=lambda:self.write('/'))
        # =
        self.btn_equal = Button(self.master,text='=',width=47,height=3,font= 6,bg='yellow',activebackground='lightgreen',command=self.result)
        self.entry.grid(row=0 ,column = 0,columnspan=4 ,pady=10 ,padx=50 , ipady=10)
        # 7,8,9 =
        self.btn_7.grid(pady=10 , row=1,column=0)
        self.btn_8.grid(pady=10 , row=1,column=1)
        self.btn_9.grid(pady=10 , row=1,column=2)
        self.btn_add.grid(pady=10 , row=1,column=3)
        #4,5,6 -
        self.btn_4.grid(pady=10 , row=2,column=0)
        self.btn_5.grid(pady=10 , row=2,column=1)
        self.btn_6.grid(pady=10 , row=2,column=2)
        self.btn_sub.grid(pady=10 , row=2,column=3)
       # 1,2,3 ,x
        self.btn_1.grid(pady=10 , row=3,column=0)
        self.btn_2.grid(pady=10 , row=3,column=1)
        self.btn_3.grid(pady=10 , row=3,column=2)
        self.btn_mul.grid(pady=10 , row=3,column=3)
        # clear , dot , div 
        self.btn_zero.grid(pady=10,row=4,column=1)
        self.btn_clear.grid(pady=10,row=4,column=0)
        self.btn_dot.grid(pady=10,row=4,column=2)
        self.btn_div.grid(pady=10,row=4,column=3)
        # =
        self.btn_equal.grid(pady=10,row=5,column=0,columnspan=4)
       

    def write(self ,char):
        
        self.char_flag = char not in '1234567890'
        if self.char_flag:
            self.flag = False
            
        if char in '-+*/':
            self.counter += 1
        else:
            self.counter = 0
            
        if  self.counter < 2:
            if self.flag == True:
                self.clear()
                self.flag = False
                sum = self.str_var.get()
                self.str_var.set(sum + char)
                
            else:    
                sum = self.str_var.get()
                self.str_var.set(sum + char)

 

    def result(self):
        try:
           sum = self.str_var.get()  
           self.str_var.set(eval(sum))
           self.flag = True
        except ZeroDivisionError :
            messagebox.showinfo(title='zero ', message='division by zero')

        

    def clear(self):
        self.str_var.set('')



win = Tk()
App(win)
win.mainloop()