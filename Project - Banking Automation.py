from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import time
import re
import sqlite3

try:
    conobj = sqlite3.connect(database = "bank.sqlite")
    curobj = conobj.cursor()
    curobj.execute("create table acn (acn_no integer primary key autoincrement, acn_name text, acn_pass text, acn_email text, acn_mob text, acn_bal float, acn_opendate text, acn_gender text)")
    curobj.close()
    print("Table Created")
except:
    print("Somethimg went wrong, might be table already exists")

win = Tk()
win.state('zoomed')
win.configure(bg = 'pink')
win.resizable(width = False, height = False)

title = Label(win,text=("Banking Automation"), font = ('arial',40,'bold'), bg = 'pink')
title.pack()
dt = time.strftime("%d %b %Y")
date = Label(win,text =f"{dt}",font = ('arial',20,'bold'), bg = 'pink',fg = 'blue' )
date.place(relx =.85,rely = .1)

def main_screen():
    frm = Frame(win)
    frm.configure(bg ='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def forgetpass():
        frm.destroy()
        forgetpass_screen()

    def open_new_acn():
        frm.destroy()
        open_new_account()

    def login():
        global gacn
        gacn=e_acn.get()
        pwd=e_password.get()
        if len(gacn)==0 or len(pwd)==0:
            messagebox.showwarning("Validation","Empty fields are not allowed")
            return
        else:
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select * from acn where acn_no=? and acn_pass=?",(gacn,pwd))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror("Login","Invalid ACN/PASS")
            else:
                frm.destroy()
                login_screen()
        
    def clear():
        e_acn.delete(0,"end")
        e_password.delete(0,"end")
        e_acn.focus()


    lbl_name = Label(frm, text="Created by: Rahul Kumar", font=('arial', 12, 'bold'), bg='powder blue')
    lbl_name.place(relx=0.80, rely=0.85)

    lbl_phone = Label(frm, text="Phone No.: 8351054274", font=('arial', 12, 'bold'), bg='powder blue')
    lbl_phone.place(relx=0.80, rely=0.90)

    lbl_email = Label(frm, text="Email: 167.kumar@gmail.com", font=('arial', 12, 'bold'), bg='powder blue')
    lbl_email.place(relx=0.80, rely=0.95)
        
    lbl_acn = Label(frm,text="Acn",bd = 5, font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_acn.place(relx=.25,rely=.1)
    e_acn = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_acn.place(relx=.35,rely =.1)

    lbl_password = Label(frm,bd = 5,text="Password", font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_password.place(relx=.22,rely=.20)
    e_password = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_password.place(relx=.35,rely =.20)

    btn_login = Button(frm,bd = 5,text="Login", font = ('arial',18,'bold'), bg = 'pink',command = login)
    btn_login.place(relx=.38,rely=.3)
    
    btn_clear = Button(frm,bd = 5,command = clear,text="Clear", font = ('arial',18,'bold'), bg = 'pink')
    btn_clear.place(relx=.48,rely=.3)

    btn_fp = Button(frm,bd = 5,text="Forget Password", font = ('arial',18,'bold'), bg = 'pink', command = forgetpass)
    btn_fp.place(relx=.38,rely=.45)

    btn_new_acn = Button(frm,bd = 5,command = open_new_acn ,text="Open New Account", font = ('arial',18,'bold'), bg = 'pink')
    btn_new_acn.place(relx=.372,rely=.6)


def forgetpass_screen():
    frm = Frame(win)
    frm.configure(bg ='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        main_screen()
        
    def clear():
        e_acn.delete(0,"end")
        e_Phone_No.delete(0,"end")
        e_email.delete(0,"end")
        e_acn.focus()

    def forgetpass_db():
        acn = e_acn.get()
        email = e_email.get()
        mob = e_Phone_No.get()
        conobj = sqlite3.connect(database="bank.sqlite")
        curobj = conobj.cursor()
        curobj.execute("select acn_pass from acn where acn_no=? and acn_mob=? and acn_email=?",(acn,mob,email))
        tup = curobj.fetchone()
        if tup == None:
            messagebox.showerror("Forgot Pass","Record not found")
        else:
            messagebox.showinfo("Forgot Pass",f"Your Pass={tup[0]}")
        conobj.close()

    
    

    lbl_acn = Label(frm,text="Acn",bd = 5, font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_acn.place(relx=.35,rely=.1)
    e_acn = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_acn.place(relx=.48,rely =.1)

    lbl_Phone_No = Label(frm,bd = 5,text="Phone Number", font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_Phone_No.place(relx=.3,rely=.22)
    e_Phone_No = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_Phone_No.place(relx=.48,rely =.22)

    lbl_email = Label(frm,bd = 5,text="Email", font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_email.place(relx=.34,rely=.33)
    e_email = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_email.place(relx=.48,rely =.33)

    btn_back = Button(frm,bd = 5,command = back,text="Back", font = ('arial',18,'bold'), bg = 'pink')
    btn_back.place(relx=0,rely=0)

    btn_submit = Button(frm,bd = 5,command = forgetpass_db,text="Submit", font = ('arial',18,'bold'), bg = 'pink')
    btn_submit.place(relx=.50,rely=.44)

    btn_clear = Button(frm,bd = 5,command = clear,text="Clear", font = ('arial',18,'bold'), bg = 'pink')
    btn_clear.place(relx=.60,rely=.44)

def open_new_account():
    frm = Frame(win)
    frm.configure(bg ='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        main_screen()

    def clear():
        e_Name.delete(0,"end")
        e_pass.delete(0,"end")
        e_Phone_No.delete(0,"end")
        e_email.delete(0,"end")
        cb_gender.delete(0,"end")
        e_Name.focus()

    def newuser_db():
        name = e_Name.get()
        pwd = e_pass.get()
        email = e_email.get()
        mob = e_Phone_No.get()
        gender = cb_gender.get()
        bal = 0
        opendate=time.strftime("%d %B %Y,%A")

        match = re.fullmatch("[6-9][0-9]{9}",mob)
        if match == None:
            messagebox.showwarning("Validation","Invalid format of mob")
            return
        
        match = re.fullmatch("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",email)
        if match == None:
            messagebox.showwarning("Validation","Invalid format of email")
            return

        conobj = sqlite3.connect(database = "bank.sqlite")
        curobj = conobj.cursor()
        curobj.execute("insert into acn(acn_name,acn_pass,acn_email,acn_mob,acn_gender,acn_opendate,acn_bal) values(?,?,?,?,?,?,?)",(name,pwd,email,mob,gender,opendate,bal))
        conobj.commit()
        conobj.close()

        conobj = sqlite3.connect(database = "bank.sqlite")
        curobj = conobj.cursor()
        curobj.execute("select max(acn_no) from acn")
        tup = curobj.fetchone()
        conobj.close()
                        
        messagebox.showinfo("New User",f"Account Created with ACN NO. = {tup[0]}")
        e_Name.delete(0,"end")
        e_pass.delete(0,"end")
        e_email.delete(0,"end")
        e_Phone_No.delete(0,"end")
        cb_gender.delete(0,"end")

    lbl_Name = Label(frm,text = "Name",bd = 5, font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_Name.place(relx=.35,rely=.1)
    e_Name = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_Name.place(relx=.48,rely =.1)

    lbl_Phone_No = Label(frm,bd = 5,text = "Phone Number", font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_Phone_No.place(relx=.3,rely=.22)
    e_Phone_No = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_Phone_No.place(relx=.48,rely =.22)

    lbl_email = Label(frm,bd = 5,text = "Email", font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_email.place(relx=.34,rely=.33)
    e_email = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_email.place(relx=.48,rely =.33)

    lbl_gender = Label(frm,text = "Gender",bd = 5, font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_gender.place(relx=.33,rely=.44)
    cb_gender = Combobox(frm,values = ['---Select---','Male','Female'],font = ('arial',20,'bold'))
    cb_gender.place(relx=.48,rely =.44)

    lbl_pass = Label(frm,text = "Password",bd = 5, font = ('arial',20,'bold'), bg = 'powder blue')
    lbl_pass.place(relx=.33,rely=.55)
    e_pass = Entry(frm,bd = 5,font = ('arial',20,'bold'), bg = 'white')
    e_pass.place(relx=.48,rely =.55)
        

    btn_back = Button(frm,bd = 5,command = back,text="Back", font = ('arial',18,'bold'), bg = 'pink')
    btn_back.place(relx=0,rely=0)

    btn_submit = Button(frm,bd = 5,command = newuser_db,text="Submit", font = ('arial',18,'bold'), bg = 'pink')
    btn_submit.place(relx=.5,rely=.7)

    btn_clear = Button(frm,bd = 5,command = clear,text="Clear", font = ('arial',18,'bold'), bg = 'pink')
    btn_clear.place(relx=.61,rely=.7)

def login_screen():
    frm = Frame(win)
    frm.configure(bg ='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def logout():
        frm.destroy()
        main_screen()

    def details():
        ifrm = Frame(highlightbackground = 'black', highlightthickness = 3)
        ifrm.configure(bg = 'white')
        ifrm.place(relx=.22 ,rely=.3 , relwidth=.65 ,relheight =.45 )

        lbl_wel = Label(ifrm,text = "This is Detail Screen ",bd = 5, font = ('arial',12,'bold'), bg = 'white')
        lbl_wel.pack()

        conobj = sqlite3.connect("bank.sqlite")
        curobj = conobj.cursor()
        curobj.execute("select acn_opendate,acn_bal,acn_gender,acn_email,acn_mob,acn_name from acn where acn_no=?",(gacn))
        tup = curobj.fetchone()
        conobj.close()

        lbl_name = Label(ifrm,text = f"Name : {tup[5]}",bd = 5, font = ('arial',15,'bold'),fg = 'orange', bg = 'white')
        lbl_name.place(relx=.07,rely=.21)

        lbl_phn = Label(ifrm,text = f"Phone No. : {tup[4]}",bd = 5, font = ('arial',15,'bold'),fg = 'orange', bg = 'white')
        lbl_phn.place(relx=.07,rely=.31)

        lbl_email = Label(ifrm,text = f"Email : {tup[3]}",bd = 5, font = ('arial',15,'bold'),fg = 'orange', bg = 'white')
        lbl_email.place(relx=.07,rely=.41)
        
        lbl_gender = Label(ifrm,text = f"Gender: {tup[2]}",bd = 5, font = ('arial',15,'bold'),fg = 'orange', bg = 'white')
        lbl_gender.place(relx=.07,rely=.51)

        lbl_bal = Label(ifrm,text = f"Balance : {tup[1]}",bd = 5, font = ('arial',15,'bold'),fg = 'orange', bg = 'white')
        lbl_bal.place(relx=.07,rely=.61)

        lbl_opendate = Label(ifrm,text = f"Open Date : {tup[0]}",bd = 5, font = ('arial',15,'bold'),fg = 'orange', bg = 'white')
        lbl_opendate.place(relx=.07,rely=.71)


    def update():
        ifrm = Frame(highlightbackground = 'black', highlightthickness = 3)
        ifrm.configure(bg = 'white')
        ifrm.place(relx=.22 ,rely=.3 , relwidth=.65 ,relheight =.45 )

        conobj = sqlite3.connect("bank.sqlite")
        curobj = conobj.cursor()
        curobj.execute("select acn_name,acn_mob,acn_email,acn_pass from acn where acn_no=?",(gacn))
        tup = curobj.fetchone()
        conobj.close()

        lbl_wel = Label(ifrm,text = "This is Update Screen ",bd = 5, font = ('arial',12,'bold'), bg = 'white')
        lbl_wel.pack()

        lbl_name = Label(ifrm,text = "Name",bd = 5, font = ('arial',15,'bold'), bg = 'white')
        lbl_name.place(relx=.07,rely=.21)
        e_name = Entry(ifrm,bd = 5,font = ('arial',15,'bold'), bg = 'white')
        e_name.place(relx=.25,rely =.21)
        e_name.insert(0,tup[0])

        lbl_phn = Label(ifrm,text = "Phone No. ",bd = 5, font = ('arial',15,'bold'), bg = 'white')
        lbl_phn.place(relx=.07,rely=.51)
        e_phn = Entry(ifrm,bd = 5,font = ('arial',15,'bold'), bg = 'white')
        e_phn.place(relx=.25,rely =.51)
        e_phn.insert(0,tup[1])

        lbl_email = Label(ifrm,text = "Email",bd = 5, font = ('arial',15,'bold'), bg = 'white')
        lbl_email.place(relx=.58,rely=.21)
        e_email = Entry(ifrm,bd = 5,font = ('arial',15,'bold'), bg = 'white')
        e_email.place(relx=.70,rely =.21)
        e_email.insert(0,tup[2])

        lbl_password = Label(ifrm,text = "Password",bd = 5, font = ('arial',15,'bold'), bg = 'white')
        lbl_password.place(relx=.58,rely=.51)
        e_password = Entry(ifrm,bd = 5,font = ('arial',15,'bold'), bg = 'white')
        e_password.place(relx=.70,rely =.51)
        e_password.insert(0,tup[3])

        def update_db():
            name = e_name.get()
            pwd = e_password.get()
            email = e_email.get()
            mob = e_phn.get()

            conobj = sqlite3.connect("bank.sqlite")
            curobj = conobj.cursor()
            curobj.execute("update acn set acn_name=?,acn_pass=?,acn_email=?,acn_mob=? where acn_no = ?",(name,pwd,email,mob,gacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update","Record Updated")
            login_screen()
            

        btn_update = Button(ifrm,bd = 5,command = update_db,text="Update", font = ('arial',15,'bold'), bg = 'pink')
        btn_update.place(relx=.45,rely=.75)

    def deposit():
        ifrm = Frame(highlightbackground = 'black', highlightthickness = 3)
        ifrm.configure(bg = 'white')
        ifrm.place(relx=.22 ,rely=.3 , relwidth=.65 ,relheight =.45 )

        lbl_wel = Label(ifrm,text = "This is Deposit Screen ",bd = 5, font = ('arial',12,'bold'), bg = 'white')
        lbl_wel.pack()

        lbl_amt_to_deposit = Label(ifrm,text = "Enter Amount To Deposit ",bd = 5, font = ('arial',15,'bold'), bg = 'white')
        lbl_amt_to_deposit.place(relx=.20,rely=.40)
        e_amt_to_deposit = Entry(ifrm,bd = 5,font = ('arial',15,'bold'), bg = 'white')
        e_amt_to_deposit.place(relx=.50,rely =.40)

        def deposit_db():
            amt = float(e_amt_to_deposit.get())
            conobj = sqlite3.connect("bank.sqlite")
            curobj = conobj.cursor()
            curobj.execute("update acn set acn_bal = acn_bal + ?  where acn_no = ?",(amt,gacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update",f"{amt } Amount Deposited")
            

        btn_submit = Button(ifrm,bd = 5,command = deposit_db,text="Submit", font = ('arial',15,'bold'), bg = 'pink')
        btn_submit.place(relx=.45,rely=.75)

    def withdraw():
        ifrm = Frame(highlightbackground = 'black', highlightthickness = 3)
        ifrm.configure(bg = 'white')
        ifrm.place(relx=.22 ,rely=.3 , relwidth=.65 ,relheight =.45 )

        lbl_wel = Label(ifrm,text = "This is Withdraw Screen ",bd = 5, font = ('arial',12,'bold'), bg = 'white')
        lbl_wel.pack()

        lbl_amt_to_deposit = Label(ifrm,text = "Enter Amount To Withdraw ",bd = 5, font = ('arial',15,'bold'), bg = 'white')
        lbl_amt_to_deposit.place(relx=.20,rely=.40)
        e_amt_to_deposit = Entry(ifrm,bd = 5,font = ('arial',15,'bold'), bg = 'white')
        e_amt_to_deposit.place(relx=.60,rely =.40)

        def withdraw_db():
            amt = float(e_amt_to_deposit.get())

            conobj = sqlite3.connect("bank.sqlite")
            curobj = conobj.cursor()
            curobj.execute("select acn_bal from acn where acn_no = ?",(gacn,))
            tup = curobj.fetchone()
            avl_bal = tup[0]

            if avl_bal > amt:
                conobj = sqlite3.connect("bank.sqlite")
                curobj = conobj.cursor()
                curobj.execute("update acn set acn_bal = acn_bal - ?  where acn_no = ?",(amt,gacn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Withdraw",f"{amt } Amount Withdraw")
            else:
                messagebox.showwarning("Withdraw", "Insufficient Balance")
            

        btn_submit = Button(ifrm,bd = 5,command = withdraw_db,text="Submit", font = ('arial',15,'bold'), bg = 'pink')
        btn_submit.place(relx=.45,rely=.75)

    def transfer():
        ifrm = Frame(highlightbackground = 'black', highlightthickness = 3)
        ifrm.configure(bg = 'white')
        ifrm.place(relx=.22 ,rely=.3 , relwidth=.65 ,relheight =.45 )
            
        lbl_wel=Label(ifrm,text = "This is Transfer Screen ",bd = 5, font = ('arial',12,'bold'), bg = 'white')
        lbl_wel.pack()
            
        lbl_amt=Label(ifrm,text="Amount",font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.1,rely=.2)

        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()
            
        lbl_to=Label(ifrm,text="To",font=('arial',20,'bold'),bg='white')
        lbl_to.place(relx=.1,rely=.4)

        e_to=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_to.place(relx=.3,rely=.4)
        e_to.focus()
                          
        def transfer_db(): 
            to_acn=e_to.get()
            amt=float(e_amt.get())
            if to_acn==gacn:
                messagebox.showwarning("Transfer","To and From can't be same")
                return
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from acn where acn_no=?",(gacn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()

            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_no from acn where acn_no=?",(to_acn,))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showwarning("Transfer","Invalid To ACN")
                return
            if avail_bal>=amt:
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                curobj.execute("update acn set acn_bal=acn_bal+? where acn_no=?",(amt,to_acn))
                curobj.execute("update acn set acn_bal=acn_bal-? where acn_no=?",(amt,gacn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Transfer",f"{amt} transered to ACN {to_acn}")

        btn_submit = Button(ifrm,bd = 5,command = transfer_db,text="Submit", font = ('arial',15,'bold'), bg = 'pink')
        btn_submit.place(relx=.45,rely=.65)

        

    lbl_welcome= Label(frm,text = '''"Welcome to your secure banking portal! Manage your finances with ease."''',bd = 5, font = ('arial',15,'bold'), bg = 'powder blue')
    lbl_welcome.place(relx=.001,rely=.001)

    btn_logout = Button(frm,bd = 5,command = logout,text="Log Out", font = ('arial',18,'bold'), bg = 'pink')
    btn_logout.place(relx=.91,rely=.01)

    btn_details = Button(frm,bd = 5,command = details,text="Details", font = ('arial',18,'bold'), bg = 'pink')
    btn_details.place(relx=.005,rely=.20)

    btn_update = Button(frm,bd = 5,command = update, text="Update", font = ('arial',18,'bold'), bg = 'pink')
    btn_update.place(relx=.005,rely=.30)    

    btn_deposit = Button(frm,bd = 5,command = deposit,text="Deposit", font = ('arial',18,'bold'), bg = 'pink')
    btn_deposit.place(relx=.005,rely=.40)
    

    btn_withdraw = Button(frm,bd = 5,command = withdraw,text="Withdraw", font = ('arial',18,'bold'), bg = 'pink')
    btn_withdraw.place(relx=.005,rely=.50)

    btn_transfer = Button(frm,bd = 5,command = transfer,text="Transfer", font = ('arial',18,'bold'), bg = 'pink')
    btn_transfer.place(relx=.005,rely=.60)


    
    
main_screen()
win.mainloop()






















