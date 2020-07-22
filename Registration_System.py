from tkinter import *
from tkinter import messagebox,ttk
import re
import sqlite3



with sqlite3.connect('database.db') as m_db:
    c=m_db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS ADMIN (username TEXT NOT NULL,password TEXT NOT NULL,gender TEXT NOT NULL,age real NOT NULL,email TEXT NOT NULL)')
m_db.commit()

c.execute('SELECT * FROM ADMIN')
for i in c.fetchall():
    print('i=',i)

c.close()    


class Registeration:
    

    def __init__(self,master1,master2):
        self.master1=master1
        self.master2=master2

        self.master1.title('Registeration')
        self.master2.title('Registeration')
        
        self.check_user=[False]*5
        

        ##############################################
        # master1:

        self.master1.geometry('600x500')
        self.master1.resizable(False,False)
        self.master1['bg']='gold'

        self.stringvar1=StringVar()
        self.stringvar2=StringVar()

        

        

        self.login_label=Label(self.master1,bg='gold',fg='blue',font=('bnazanin',100,'bold'),text='LOG IN')
        self.login_label.pack()

        self.frame1=Frame(self.master1,bg='blue',width=1000,height=1000,relief=GROOVE)
        self.frame1.pack()
        

        
        
              

        #email label:
        Label(self.frame1,text='User Email',font=(15),bg='blue',fg='yellow').grid(padx=20,pady=5,columnspan=2)

        #entry of email:
        Entry(self.frame1,width=20,font=(10),textvariable=self.stringvar1).grid(padx=15,pady=5,columnspan=2)

        #password label:
        Label(self.frame1,text='User Password',font=(15),bg='blue',fg='yellow').grid(padx=15,pady=5,columnspan=2)

        #entry of password
        Entry(self.frame1,width=20,font=(10),show='*',textvariable=self.stringvar2).grid(padx=15,pady=5,columnspan=2)

        

        #login button
        self.login_button=Button(self.frame1,width=20,height=1,command= self.log_in_func,font=(5),text="Log In",bg='gold',fg='blue')
        self.login_button.grid(padx=15,pady=5,columnspan=2)

        # turquoise


        #not a member label:
        Label(self.frame1,text='not a member?',font=(1),bg='blue',fg='white').grid(row=5,column=0,padx=15,pady=5)

        self.sign_up_now_button=Button(self.frame1,text='sign up now',width=15,command=self.open_sing_up,height=1,bg='blue',fg='white')
        self.sign_up_now_button.grid(row=5,column=1,padx=15,pady=5)

        ############################################

        # master 2:

        self.m2_username=StringVar()
        self.m2_email=StringVar()
        self.m2_password=StringVar()

        self.master2.withdraw()
        self.master2.lift(self.master1)
        Label(self.master2,text="SIGN UP",font=('bnazanin',80,'bold'),bg='aqua',fg='gold').pack()

        self.frame2=Frame(self.master2,bg='gold')
        self.master2['bg']='aqua'


        self.frame2.pack()

        self.frame3=Frame(self.master2,bg='gold')
        self.frame3.pack()
        ###############################################

        self.gender=StringVar()
        self.gender.set(None)

        

        self.check1=Radiobutton(self.frame3,text='male',bg='gold',variable=self.gender,value='male',font=(12))
        self.check1.grid(row=0,column=1,padx=1,pady=10)

        

        self.check2=Radiobutton(self.frame3,text='female',bg='gold',font=(12),variable=self.gender,value='female')
        self.check2.grid(row=0,column=2,padx=1,pady=10)

        self.check3=Radiobutton(self.frame3,text='others',bg='gold',font=(12),variable=self.gender,value='others')
        self.check3.grid(row=0,column=3,padx=1,pady=10,sticky=E)

        self.check1.deselect()
        self.check2.deselect()
        self.check3.deselect()

        ##################################################################
        Label(self.frame2,text='User Name',bg='gold',fg='green',font=(20)).grid(row=0,column=0,padx=10,pady=10)
        
        Label(self.frame2,text='User Email',bg='gold',fg='green',font=(20)).grid(row=1,column=0,padx=10,pady=10)

        Label(self.frame2,text='User Password',bg='gold',fg='green',font=(19)).grid(row=2,column=0,padx=10,pady=10)

        Label(self.frame3,text='User Gender',bg='gold',fg='green',font=(22)).grid(row=0,column=0,padx=10,pady=10)

        Label(self.frame2,text='User Age',bg='gold',fg='green',font=(20)).grid(row=4,column=0,padx=10,pady=10)


        # user name
        Entry(self.frame2,textvariable=self.m2_username,width=26,font=(9)).grid(row=0,column=1,padx=10,pady=10)

        
        # email
        Entry(self.frame2,textvariable=self.m2_email,width=26,font=(9)).grid(row=1,column=1,padx=10,pady=10)


        # password
        Entry(self.frame2,textvariable=self.m2_password,show='*',width=26,font=(9)).grid(row=2,column=1,padx=10,pady=10)

        

        
        # age
        self.age=StringVar()
        self.age.set('')
        ttk.Combobox(self.frame2,textvariable=self.age,width=24,font=(18),values=list(range(9,121))).grid(row=4,column=1,padx=10,pady=10)



        
        
        Button(self.frame3,text='Sign up',width=40,justify='center'
        ,font=(24),bg='aqua',fg='gold',command=self.sing_up_func).grid(row=1,columnspan=4,padx=10,pady=10)

        # .place(x=0,y=0)


        self.master1.mainloop()

        print('gender=',self.gender.get(),type(self.gender.get()))
        print('age=',self.age.get(),type(self.age.get()),list(map(int,self.age.get())))
        print(self.m2_password.get())
        print(self.check_user)
       

    def open_sing_up(self):
        self.master2.wm_deiconify()
        


    
    def log_in_func(self):
        with sqlite3.connect('database.db') as m_db:
            c=m_db.cursor()

        c.execute('SELECT * FROM ADMIN WHERE email=? and password=?',[(self.stringvar1.get()),(self.stringvar2.get())])    
        A=c.fetchall()

        print(A)

        if A:
            messagebox.showinfo('success','welcome to your page!')

        else:
            messagebox.showerror('error','there is no user with this email and password please go to sign up')
        
        






    def sing_up_func(self):
        
        

        with sqlite3.connect('database.db') as m_db:
            c=m_db.cursor()

        c.execute('SELECT * FROM ADMIN WHERE email=? and password=?',[(self.m2_email.get()),(self.m2_password.get())])    
        
        if c.fetchall():
            messagebox.showerror('error','this user is already exists!')


        

        else:
            
            if self.m2_email.get()=='' or self.m2_username.get()=='' or self.age.get()=='':
                messagebox.showerror('error','feilds must not be empty')    
                self.master2.lift(self.master1)
            else:
                self.check_user[0]=self.m2_username.get()
                print(self.check_user)
                


            if len(self.m2_password.get())<6 or not re.match(r'[0-9A-Za-z.,/?]',self.m2_password.get()):
                messagebox.showerror('error','password has to be max 7 characters uper and lower case letter and number and symbols')
                self.m2_password.set("")
                self.master2.lift(self.master1)
            else:
                self.check_user[1]=self.m2_password.get()
                print(self.check_user)    

           
            if  str(self.age.get()).isalpha()  or  (self.age.get())=='':
                messagebox.showerror('error','age have to be int number greater than 9 ')
                self.master2.lift(self.master1)
            else:
                self.check_user[3]=self.age.get()

            
            if self.gender.get() not in ['male','female','others'] :
                messagebox.showerror('error','please select your sex')     
                self.master2.lift(self.master1)
            else:
                self.check_user[2]=self.gender.get()
                print(self.check_user)

            
            if not re.match(r'[\w]+@[\w]*.com',self.m2_email.get()):
                messagebox.showwarning('warning','please enter your email correctly')
                self.master2.lift(self.master1)

            else:
                self.check_user[-1]=self.m2_email.get()
                print(self.check_user)    
            

            if all(self.check_user):
                c.execute('INSERT INTO ADMIN (username,password,gender,age,email) VALUES (?,?,?,?,?)',self.check_user)
                m_db.commit()
                c.close()

                messagebox.showinfo('weldone','successfully do it')
                self.master2.lift(self.master1)
                self.age.set('')
                self.m2_username.set('')
                self.m2_password.set('')
                self.gender.set(None)
                self.m2_email.set('')
                self.check_user=[False]*5
                self.master2.withdraw()


            
                
            

def main():
    def close():

        if messagebox.askquestion('quit','do you want to exit?'):
            root1.destroy()


    root1=Tk()
    root2=Toplevel(root1)

    root1.protocol('WM_DELETE_WINDOW',close)
    
    root2.protocol("WM_DELETE_WINDOW", root2.withdraw)
    

    

    Registeration(root1,root2)
    

    

    


main()

