from tkinter import *
import register_page
import os
import sqlite3 as base
import datetime
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()

login_page =Tk()
login_page.title("KM bank")
login_page.configure(bg="#93D5FF")
login_page.iconbitmap("dbmsicon.ico")
#login_page.geometry("900x700")
Label(login_page,text = "KMC BANK",font ="Algerian 35",bg ="#93D5FF").grid(sticky=E)

##########################################################################
# Only functions()
def login():
    u="admin"
    p="1234"
    user_i= username_box.get()
    passw_i=password_box.get()
    cursor.execute("SELECT PASSWORD from customer WHERE CUST_ID = :CUSTID;",{ 'CUSTID':user_i})
    password_real = cursor.fetchall()
    cust_id_=user_i
    def manager_view():
        admin_page =Tk()
        admin_page.title("KM bank")
        admin_page.configure(bg="#93D5FF")
        admin_page.iconbitmap("dbmsicon.ico")

        #functions
        def employee_details_f():
            all_emp_details_page=Toplevel()
            all_emp_details_page.title("KM bank")
            all_emp_details_page.configure(bg="#93D5FF")
            all_emp_details_page.iconbitmap("dbmsicon.ico")  

            cursor.execute("select * from OFFICER ")
            x =cursor.fetchall()
            i=0
            j=0 
            var=''
            result=[]
            for i in range(len(x)):
                for j in range(6):
                    var=var+"\t" +str(x[i][j]) 
                result.append(var)
                var=' '
            Label(all_emp_details_page,text ="EMP_ID  BRANCH_ID  NAME  EMAIL  GENDER  CONTACT ",font ="none 15",bg ="#93D5FF", borderwidth=2, relief="ridge",pady=10,padx=10).grid(row=0,column=0,pady=10,padx=10,sticky = E)
            for i in range(len(result)):
                Label(all_emp_details_page,text = result[i] +"\t",font ="none 15",bg ="#93D5FF", borderwidth=2, relief="ridge").grid(row=i+1,column=0,pady=10,padx=10,sticky = E)
            def close_button_f():
                all_emp_details_page.destroy()
            close_button=Button(all_emp_details_page,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
            close_button.grid(row=30,column=0,pady=10,padx=20)
            all_emp_details_page.grab_set()


        def account_details_f():
            all_ac_details_page=Toplevel()
            all_ac_details_page.title("KM bank")
            all_ac_details_page.configure(bg="#93D5FF")
            all_ac_details_page.iconbitmap("dbmsicon.ico")  

            cursor.execute("select * from account ")
            x =cursor.fetchall()
            i=0
            j=0 
            var=''
            result=[]
            for i in range(len(x)):
                for j in range(8):
                    var=var+"\t" +str(x[i][j]) 
                result.append(var)
                var=' '
            Label(all_ac_details_page,text ="ACCCOUNT NO |  INT_ID |  CUSTOMER_ID  |  AC_TYPE |  BALANCE |  INT_AMOUNT |  INT_RATE |  OPEN_DATE| ",font ="none 15",bg ="#93D5FF", borderwidth=2, relief="ridge",pady=10,padx=10).grid(row=0,column=0,pady=10,padx=10,sticky = E)
            for i in range(len(result)):
                Label(all_ac_details_page,text = result[i] +"\t",font ="none 15",bg ="#93D5FF", borderwidth=2, relief="ridge").grid(row=i+1,column=0,pady=10,padx=10,sticky = W)
            def close_button_f():
                all_ac_details_page.destroy()
            close_button=Button(all_ac_details_page,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
            close_button.grid(row=30,column=0,pady=10,padx=20)
            all_ac_details_page.grab_set()

            
        def account_activity_details_f():
            account_activity_details_tk = Toplevel()
            account_activity_details_tk.title("KM bank")
            account_activity_details_tk.configure(bg="#93D5FF")
            account_activity_details_tk.iconbitmap("dbmsicon.ico")


            Label(account_activity_details_tk,text = "Enter account no.",font ="none 25",bg ="#93D5FF").grid(row=0,column=0,pady=10,padx=20)
            acc_no_input_activity =Entry(account_activity_details_tk,font ="none 20",bg ="#93D5FF")
            acc_no_input_activity.grid(row=1,column=0,pady=10,padx=20)
            def get_ac_no():
                if acc_no_input_activity.get() == '':
                    Label(account_activity_details_tk,text="Enter Account No. or close",font ="none 25",bg ="#93D5FF").grid(row=3,column=0,pady=10,padx=20)
                else:
                    ac_no=int(acc_no_input_activity.get())
                    get_acc_button.destroy()
                    acc_no_input_activity.destroy()
                    cursor.execute("SELECT * FROM transactions where ac_no =:ac_no",{'ac_no':ac_no})
                    print(ac_no)
                    x = cursor.fetchall()
                    i=0
                    j=0
                    result =[]
                    var=' '
                    for i in range(len(x)):
                        for j in range(4):
                            var=var+"\t" +str(x[i][j]) 
                        result.append(var)
                        var=' '
                    i=0
                    Label(account_activity_details_tk,text ="\tACCOUNT NO\tTRANS ID   \tACTIVITY \tACTIVITY DATETIME\t",font ="none 15",bg ="#93D5FF", borderwidth=2, relief="ridge",pady=10,padx=10).grid(row=0,column=0,pady=10,padx=10,sticky = E)
                    for i in range(len(result)):
                        Label(account_activity_details_tk,text = result[i] +"\t",font ="none 15",bg ="#93D5FF", borderwidth=2, relief="ridge").grid(row=i+1,column=0,pady=10,padx=10,sticky = E)
                    def close_button_f():
                        account_activity_details_tk.destroy()
                    close_button=Button(account_activity_details_tk,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
                    close_button.grid(row=30,column=0,pady=10,padx=20)
            

            get_acc_button=Button(account_activity_details_tk,text="submit",padx=20,pady=5,height = 2, width = 20,command=get_ac_no)
            get_acc_button.grid(row=2,column=0,pady=10,padx=20)
            account_activity_details_tk.grab_set()

        def add_employee_f():
            add_emp_page =Toplevel()
            add_emp_page.title("KM bank")
            add_emp_page.configure(bg="#93D5FF")
            add_emp_page.iconbitmap("dbmsicon.ico")

            #functions only
            def go_back_button():
                add_emp_page.destroy()
            def register_button():
                branch_id =     branch_id_e.get()
                name =          name_e.get()
                street =     street_box.get()
                state =      state_box.get()
                city =       city_box.get()
                pin =        pin_box.get()
                email =         email_e.get()
                gender =        gender_e.get()
                contact =       contact_e.get()
                nationality=    nationality_e.get()
                dob=            dob_e.get()
                username  =     username_e.get()
                password =    password_e.get()
                if branch_id =='':
                    Label(add_emp_page,text ="Please enter Branch_id",font="Android 15",padx=10,pady=10)    .grid(row=17,column=1)
                elif name =='':
                    Label(add_emp_page,text ="Please enter Name",font="Android 15",padx=10,pady=10)         .grid(row=17,column=1)
                elif email =='':
                    Label(add_emp_page,text ="Please enter Email",font="Android 15",padx=10,pady=10)        .grid(row=17,column=1)
                elif street =='':
                    Label(add_emp_page,text ="Please enter street",font="Android 15",padx=10,pady=10)      .grid(row=17,column=1)        
                elif state =='':
                    Label(add_emp_page,text ="Please enter state",font="Android 15",padx=10,pady=10)       .grid(row=17,column=1)        
                elif city =='':
                    Label(add_emp_page,text ="Please enter city",font="Android 15",padx=10,pady=10)        .grid(row=17,column=1)        
                elif pin =='':
                    Label(add_emp_page,text ="Please enter pin",font="Android 15",padx=10,pady=10)         .grid(row=17,column=1)        
                elif gender =='':
                    Label(add_emp_page,text ="Please enter Gender",font="Android 15",padx=10,pady=10)       .grid(row=17,column=1)
                elif contact =='':
                    Label(add_emp_page,text ="Please enter Contact No.",font="Android 15",padx=10,pady=10)  .grid(row=17,column=1)
                elif nationality =='':
                    Label(add_emp_page,text ="Please enter Nationality",font="Android 15",padx=10,pady=10)  .grid(row=17,column=1)
                elif dob =='':
                    Label(add_emp_page,text ="Please enter dob",font="Android 15",padx=10,pady=10)      .grid(row=17,column=1)
                elif username =='':
                    Label(add_emp_page,text ="Please enter username",font="Android 15",padx=10,pady=10) .grid(row=17,column=1)
                elif password =='':
                    Label(add_emp_page,text ="Please enter password",font="Android 15",padx=10,pady=10) .grid(row=17,column=1)
                else:
                    cursor.execute("INSERT INTO OFFICER VALUES (:EMP_ID ,:BRANCH_ID , :NAME , :EMAIL ,:GENDER  ,:CONTACT ,:NATIONALITY ,:DOB ,:USERNAME ,:PASSWORD )",
                        {
                            'EMP_ID':emp_id,
                            'BRANCH_ID': branch_id,
                            'NAME':name ,
                            'EMAIL':email ,
                            'GENDER':gender ,
                            'CONTACT': contact,
                            'NATIONALITY':nationality ,
                            'DOB': dob,
                            'USERNAME':username,
                            'PASSWORD':password 
                            })
                    cursor.execute("INSERT INTO OFFICER_ADDRESS VALUES (:EMP_ID , :STREET  ,:CITY,:STATE,:PIN)",
                            {
                                'EMP_ID':emp_id,
                                'STREET':street,
                                'STATE':state ,
                                'CITY':city ,
                                'PIN':pin
                            })
                    add_emp_page.destroy()
                    cursor.execute("UPDATE employeeID_generator SET employee_id_g = :employee_id_g WHERE row=1;",{
                    'employee_id_g':x[0][0]+1
                    }
                    ) 

            cursor.execute("SELECT employee_id_g FROM employeeID_generator where row =1")
            x = cursor.fetchall()
            emp_id =x[0][0]   
            #Labels
            Label(add_emp_page,text = "EMP_ID",font ="none 15",bg ="#93D5FF")       .grid(row=1,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text = emp_id,font ="none 15",bg ="#93D5FF")         .grid(row=1,column=1,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text="BRANCH_ID ",font ="none 15",bg ="#93D5FF")     .grid(row=2,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text = "NAME ",font ="none 15",bg ="#93D5FF")        .grid(row=3,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text = "Address: Street",font ="none 15",bg ="#93D5FF") .grid(row=4,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text="Address: State",font ="none 15",bg ="#93D5FF")    .grid(row=5,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text = "Address: City",font ="none 15",bg ="#93D5FF")   .grid(row=6,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text = "Address: pin",font ="none 15",bg ="#93D5FF")    .grid(row=7,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text = "EMAIL ",font ="none 15",bg ="#93D5FF")      .grid(row=8,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text="GENDER ",font ="none 15",bg ="#93D5FF")       .grid(row=9,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text = "CONTACT ",font ="none 15",bg ="#93D5FF")    .grid(row=10,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text="NATIONALITY ",font ="none 15",bg ="#93D5FF")  .grid(row=11,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text = "DOB",font ="none 15",bg ="#93D5FF")         .grid(row=12,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text="USERNAME ",font ="none 15",bg ="#93D5FF")     .grid(row=13,column=0,pady=10,padx=20,sticky = W)
            Label(add_emp_page,text="PASSWORD ",font ="none 15",bg ="#93D5FF")     .grid(row=14,column=0,pady=10,padx=20,sticky = W)
            #entry
            branch_id_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            name_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            street_box=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            state_box=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            city_box=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            pin_box=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            email_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            gender_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            contact_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            nationality_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            dob_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            username_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            password_e=Entry(add_emp_page,font ="none 15",bg ="#93D5FF")
            #entry.grid()
            branch_id_e     .grid(row=2,column=1,pady=10,padx=20,sticky = W)
            name_e          .grid(row=3,column=1,pady=10,padx=20,sticky = W)
            street_box.     grid(row=4,column=1,pady=10,padx=20,sticky = W)
            state_box.      grid(row=5,column=1,pady=10,padx=20,sticky = W)
            city_box.       grid(row=6,column=1,pady=10,padx=20,sticky = W)
            pin_box.        grid(row=7,column=1,pady=10,padx=20,sticky = W)
            email_e         .grid(row=8,column=1,pady=10,padx=20,sticky = W)
            gender_e        .grid(row=9,column=1,pady=10,padx=20,sticky = W)
            contact_e       .grid(row=10,column=1,pady=10,padx=20,sticky = W)
            nationality_e   .grid(row=11,column=1,pady=10,padx=20,sticky = W)
            dob_e           .grid(row=12,column=1,pady=10,padx=20,sticky = W)
            username_e      .grid(row=13,column=1,pady=10,padx=20,sticky = W)
            password_e      .grid(row=14,column=1,pady=10,padx=20,sticky = W)
            #Only Buttons()
            register=Button(add_emp_page,text="Register Employee",padx=30,pady=5,command=register_button)
            go_back=Button(add_emp_page,text="Go Back",padx=30,pady=5,command=go_back_button)
            #button.grid()
            register.grid(row=15,column=1,pady=10,padx=20,sticky = W)
            go_back.grid(row=16,column=1,pady=10,padx=20,sticky = W)        


        def set_interest_rate_f():
            set_interest_rate = Toplevel()
            set_interest_rate.title("KM bank")
            set_interest_rate.configure(bg="#93D5FF")
            set_interest_rate.iconbitmap("dbmsicon.ico")

            cursor.execute("SELECT SAVING_INT  FROM INTEREST where INTEREST_ID  =1")
            x= cursor.fetchall()
            current_int_amt=x[0][0]
            Label(set_interest_rate,text ="Current Interest Rate for savings account" ,font ="none 25",bg ="#93D5FF").grid(row=0,column=0,pady=10,padx=20)
            Label(set_interest_rate,text =current_int_amt ,font ="none 25",bg ="#93D5FF").grid(row=1,column=0,pady=10,padx=20)
            Label(set_interest_rate,text ="Enter new Interest Rate" ,font ="none 25",bg ="#93D5FF").grid(row=2,column=0,pady=10,padx=20)
            new_interest_rate_e =Entry(set_interest_rate,font ="none 20",bg ="#93D5FF")
            new_interest_rate_e.grid(row=3,column=0,pady=10,padx=20)

            def set_new_int_rate():
                new_interest_rate = new_interest_rate_e.get()
                if new_interest_rate =='':
                    Label(set_interest_rate,text ="Enter any value or close",font ="none 15",bg ="#93D5FF").grid(row=31,column=0,pady=10,padx=20)
                    return
                cursor.execute("UPDATE INTEREST SET SAVING_INT  = :SAVING_INT  WHERE INTEREST_ID =1;",{
                'SAVING_INT':new_interest_rate
                }
                ) 
                cursor.execute("UPDATE ACCOUNT SET INTEREST_RATE= :INTEREST_RATE WHERE INTEREST_ID =1;",{
                'INTEREST_RATE':new_interest_rate
                }
                )
                data_base.commit()
                submit_int_rate.destroy()
                Label(set_interest_rate,text ="Interest rate set to "+ str(new_interest_rate) ,font ="none 25",bg ="#93D5FF").grid(row=4,column=0,pady=10,padx=20)

            submit_int_rate=Button(set_interest_rate,text="submit",padx=20,pady=5,height = 2, width = 20,command=set_new_int_rate)
            submit_int_rate.grid(row=4,column=0,pady=10,padx=20)
            def close_button_f():
                set_interest_rate.destroy()
            close_button=Button(set_interest_rate,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
            close_button.grid(row=30,column=0,pady=10,padx=20)
            set_interest_rate.grab_set()

        def add_interest_to_accounts_f():
            add_int_acc_page = Tk()
            add_int_acc_page.title("KM bank")
            add_int_acc_page.configure(bg="#93D5FF")
            add_int_acc_page.iconbitmap("dbmsicon.ico")

            def CONFIRM_f():
                cursor.execute("select AC_NO from ACCOUNT")
                x = cursor.fetchall()
                i=0
                for i in range(len(x)):
                    ac_no=x[i][0]
                    cursor.execute("select BALANCE  from ACCOUNT where AC_NO =:AC_NO",{'AC_NO':ac_no})
                    balance_fetch= cursor.fetchall()
                    balance = float(balance_fetch[0][0])
                    cursor.execute("select INTEREST_RATE from ACCOUNT where AC_NO =:AC_NO",{'AC_NO':ac_no})
                    interest_rate_fetch= cursor.fetchall()
                    int_rate = float(interest_rate_fetch[0][0]) 
                    updated_balance = round((balance + balance*int_rate*0.001),3) 
                    updated_int_amt=round((balance*int_rate*0.001),3)
                    cursor.execute("UPDATE account SET balance= :balance where AC_NO=:AC_NO;",{
                    'balance':updated_balance,
                    'AC_NO':ac_no
                    }
                    )
                    cursor.execute("UPDATE account SET INTEREST_AMOUNT = :INTEREST_AMOUNT WHERE AC_NO=:AC_NO ;",{
                    'INTEREST_AMOUNT':updated_int_amt,
                    'AC_NO':ac_no
                    }
                    )
                    cursor.execute("SELECT trans_id_g FROM transactionID_generator where row =1")
                    t = cursor.fetchall()
                    trans_id =t[0][0]
                    print("TransID = "+ str(trans_id))
                    cursor.execute("UPDATE transactionID_generator SET trans_id_g = :trans_id_g WHERE row=1;",
                    {
                        'trans_id_g':t[0][0]+1
                        })
                    date_of_trans = datetime.datetime.now()

                    cursor.execute("INSERT INTO TRANSACTIONS VALUES (:AC_NO,:TRANS_ID ,:TRANS_TYPE ,:DATE_OF_TRANS )",
                    {
                        
                        'AC_NO':ac_no,
                        'TRANS_ID':trans_id,
                        'TRANS_TYPE': "\tSavingsINT +"+ str(updated_int_amt)+"\t",
                        'DATE_OF_TRANS':date_of_trans 
                        })
                confirm_button.destroy()
                Label(add_int_acc_page,text ="Interest amount added to all accounts" ,font ="none 25",bg ="#93D5FF").grid(row=1,column=0,pady=10,padx=20)
            Label(add_int_acc_page,text ="Confirm to add interest amount to all accounts" ,font ="none 25",bg ="#93D5FF").grid(row=0,column=0,pady=10,padx=20)
            confirm_button=Button(add_int_acc_page,text="CONFIRM",padx=20,pady=5,height = 2, width = 20,command=CONFIRM_f)
            confirm_button.grid(row=1,column=0,pady=10,padx=20)


        def log_out_f():
            admin_page.destroy()
        #Labels
        Label(admin_page,text = "Welcome Manager",font ="Algerian 25",bg ="#93D5FF").grid(row=0,column=0,pady=10,padx=20)
        #Button
        employee_details=Button(admin_page,text="Employee Details",padx=30,pady=5,height = 2, width = 20,command=employee_details_f)
        account_details=Button(admin_page,text="All Account Details",padx=30,pady=5,height = 2, width = 20,command=account_details_f)
        account_activity_details=Button(admin_page,text="Account activity Details",padx=30,pady=5,height = 2, width = 20,command=account_activity_details_f)
        add_employee=Button(admin_page,text="Add Employee",padx=30,pady=5,height = 2, width = 20,command=add_employee_f)
        set_interest_rate=Button(admin_page,text="Set Interest Rate",padx=30,pady=5,height = 2, width = 20,command=set_interest_rate_f)
        add_interest_to_accounts=Button(admin_page,text="Add interest amount to accounts",padx=30,pady=5,height = 2, width = 20,command=add_interest_to_accounts_f)
        log_out_button=Button(admin_page,text="LogOut",padx=30,pady=5,height = 2, width = 20,command=log_out_f)


        #Buttone.grid()
        employee_details        .grid(row=1,column=0,pady=10,padx=20)
        add_employee            .grid(row=1,column=1,pady=10,padx=20)
        account_details         .grid(row=2,column=0,pady=10,padx=20)
        account_activity_details.grid(row=2,column=1,pady=10,padx=20)
        set_interest_rate       .grid(row=3,column=0,pady=10,padx=20)
        add_interest_to_accounts.grid(row=3,column=1,pady=10,padx=20)
        log_out_button          .grid(row=4,column=0,pady=10,padx=20)
        admin_page.grab_set()
    def customer_signin_window(cust_id_):
        signin_page =Tk()
        signin_page.title("KM bank")
        signin_page.configure(bg="#93D5FF")
        signin_page.iconbitmap("dbmsicon.ico")
        def check_balance_f():
            balance_page =Toplevel()
            balance_page.title("KM bank")
            balance_page.configure(bg="#93D5FF")
            balance_page.iconbitmap("dbmsicon.ico")
            cursor.execute("SELECT BALANCE from account WHERE AC_NO = :ACNO;",{ 'ACNO':ac_no})
            b = cursor.fetchall()
            balance =b[0][0]
            balance_l=Label(balance_page,text = "  Your Current Balance: "+ str(balance)+"  ",font ="none 25",bg ="#93D5FF")
            balance_l.grid(row=0,column=0,pady=10,padx=20)
            def close_button_f():
                balance_page.destroy()
            close_button=Button(balance_page,text="Close",padx=30,pady=10,height = 2, width = 20,command=close_button_f)
            close_button.grid(row=1,column=0,pady=10,padx=20)
            balance_page.grab_set()

        def deposit_f():
            deposit_page =Toplevel()
            deposit_page.title("KM bank")
            deposit_page.configure(bg="#93D5FF")
            deposit_page.iconbitmap("dbmsicon.ico")
            deposit_test_l=             Label(deposit_page,text = "  Enter amount to deposit: ",font ="none 25",bg ="#93D5FF")
            deposit_amount_entry=       Entry(deposit_page,font ="none 25")
            deposit_test_l          .grid(row=0,column=0,pady=10,padx=20)
            deposit_amount_entry    .grid(row=1,column=0,pady=10,padx=20)
            def submit_button_f():
                cursor.execute("SELECT BALANCE from account WHERE AC_NO = :ACNO;",{ 'ACNO':ac_no})
                b = cursor.fetchall()
                balance =b[0][0]
                if deposit_amount_entry.get() == '':
                    Label(deposit_page,text = "  Enter amount to deposit or Close ",font ="none 10",bg ="#93D5FF").grid(row=1,column=1,pady=10,padx=20)
                elif deposit_amount_entry.get().isdigit():
                    cursor.execute("SELECT trans_id_g FROM transactionID_generator where row =1")
                    t = cursor.fetchall()
                    trans_id =t[0][0]
                    print("TransID = "+ str(trans_id))
                    cursor.execute("UPDATE transactionID_generator SET trans_id_g = :trans_id_g WHERE row=1;",
                    {
                        'trans_id_g':t[0][0]+1
                        })
                    date_of_trans = datetime.datetime.now()

                    cursor.execute("INSERT INTO TRANSACTIONS VALUES (:AC_NO,:TRANS_ID ,:TRANS_TYPE ,:DATE_OF_TRANS )",
                    {
                        
                        'AC_NO':ac_no,
                        'TRANS_ID':trans_id,
                        'TRANS_TYPE': "\tDEPOSITED +"+ str(deposit_amount_entry.get()),
                        'DATE_OF_TRANS':date_of_trans 
                        })


                    updated_balance=balance+int(deposit_amount_entry.get())
                    cursor.execute("UPDATE account SET balance = :balance WHERE AC_NO = :ACNO;",{ 'balance':updated_balance,'ACNO':ac_no})
                    submit_button.destroy()
                    Label(deposit_page,text = "Rs "+str(deposit_amount_entry.get())+" deposited",font ="none 25",bg ="#93D5FF").grid(row=2,column=0,pady=10,padx=20)
                else:
                    Label(deposit_page,text = "  Enter only numbers ",font ="none 10",bg ="#93D5FF").grid(row=1,column=1,pady=10,padx=20)

                
            submit_button=Button(deposit_page,text="Deposit",padx=30,pady=10,height = 2, width = 20,command=submit_button_f)
            submit_button.grid(row=2,column=0,pady=10,padx=20)
            def close_button_f():
                deposit_page.destroy()
            close_button=Button(deposit_page,text="Close",padx=30,pady=10,height = 2, width = 20,command=close_button_f)
            close_button.grid(row=3,column=0,pady=10,padx=20)
            deposit_page.grab_set()
            
        def withdraw_f():
            withdraw_page =Toplevel()
            withdraw_page.title("KM bank")
            withdraw_page.configure(bg="#93D5FF")
            withdraw_page.iconbitmap("dbmsicon.ico")
            withdraw_test_l=             Label(withdraw_page,text = "  Enter amount to transfer: ",font ="none 25",bg ="#93D5FF")
            withdraw_amount_entry=       Entry(withdraw_page,font ="none 25")
            withdraw_test_l          .grid(row=0,column=0,pady=10,padx=20)
            withdraw_amount_entry    .grid(row=1,column=0,pady=10,padx=20)
            def submit_button_f_w():
                cursor.execute("SELECT BALANCE from account WHERE AC_NO = :ACNO;",{ 'ACNO':ac_no})
                b = cursor.fetchall()
                balance =b[0][0]
                if withdraw_amount_entry.get() == '':
                    Label(withdraw_page,text = "  Enter amount to transfer or Close ",font ="none 10",bg ="#93D5FF").grid(row=1,column=1,pady=10,padx=20)
                elif withdraw_amount_entry.get().isdigit():
                    cursor.execute("SELECT trans_id_g FROM transactionID_generator where row =1")
                    t = cursor.fetchall()
                    trans_id =t[0][0]
                    print("TransID = "+ str(trans_id))
                    cursor.execute("UPDATE transactionID_generator SET trans_id_g = :trans_id_g WHERE row=1;",
                    {
                        'trans_id_g':t[0][0]+1
                        })
                    date_of_trans = datetime.datetime.now()

                    cursor.execute("INSERT INTO TRANSACTIONS VALUES (:AC_NO,:TRANS_ID ,:TRANS_TYPE ,:DATE_OF_TRANS )",
                    {
                        
                        'AC_NO':ac_no,
                        'TRANS_ID':trans_id,
                        'TRANS_TYPE': "\tWITHDREW -"+ str(withdraw_amount_entry.get())+"\t",
                        'DATE_OF_TRANS':date_of_trans 
                        })


                    updated_balance=balance - int(withdraw_amount_entry.get())
                    cursor.execute("UPDATE account SET balance = :balance WHERE AC_NO = :ACNO;",{ 'balance':updated_balance,'ACNO':ac_no})
                    submit_button.destroy()
                    Label(withdraw_page,text = "Rs "+str(withdraw_amount_entry.get())+" withdrawn",font ="none 25",bg ="#93D5FF").grid(row=2,column=0,pady=10,padx=20)
                else:
                    Label(withdraw_page,text = "  Enter only numbers ",font ="none 10",bg ="#93D5FF").grid(row=1,column=1,pady=10,padx=20)

                
            submit_button=Button(withdraw_page,text="Transfer",padx=30,pady=10,height = 2, width = 20,command=submit_button_f_w)
            submit_button.grid(row=2,column=0,pady=10,padx=20)
            def close_button_f():
                withdraw_page.destroy()
            close_button=Button(withdraw_page,text="Close",padx=30,pady=10,height = 2, width = 20,command=close_button_f)
            close_button.grid(row=3,column=0,pady=10,padx=20)
            withdraw_page.grab_set()

        def mini_statement_f():
            mini_statement =Toplevel()
            mini_statement.title("KM bank")
            mini_statement.configure(bg="#93D5FF")
            mini_statement.iconbitmap("dbmsicon.ico")
            cursor.execute("SELECT * FROM transactions where ac_no =:ac_no",{'ac_no':ac_no})
            print(ac_no)
            x = cursor.fetchall()
            i=0
            j=0
            result =[]
            var=' '
            for i in range(len(x)):
                for j in range(4):
                    var=var+"\t" +str(x[i][j]) 
                result.append(var)
                var=''
            i=0
            Label(mini_statement,text ="\tACCOUNT NO\t\tTRANSACTION ID   \tACTIVITY \t\tACTIVITY DATETIME\t",font ="none 15",bg ="#93D5FF", borderwidth=2, relief="ridge",pady=10,padx=10).grid(row=0,column=0,pady=10,padx=0,sticky = E)
            for i in range(len(result)):
                Label(mini_statement,text = result[i] +"\t",font ="none 15",bg ="#93D5FF", borderwidth=2, relief="ridge").grid(row=i+1,column=0,pady=10,padx=10,sticky = E)
            def close_button_f():
                mini_statement.destroy()
            close_button=Button(mini_statement,text="Close",padx=20,pady=5,height = 2, width = 20,command=close_button_f)
            close_button.grid(row=30,column=0,pady=10,padx=20)
            mini_statement.grab_set()

        def log_out_f():
            signin_page.destroy()
        cursor.execute("SELECT AC_NO from account WHERE CUST_ID = :CUSTID;",{ 'CUSTID':cust_id_})
        x = cursor.fetchall()
        ac_no=x[0][0]
        #print(ac_no)
        cursor.execute("SELECT NAME from customer WHERE CUST_ID = :CUSTID;",{ 'CUSTID':cust_id_})
        n = cursor.fetchall()
        name = n[0][0]
        #print(balance)
        #Label
        welcome_message=Label(signin_page,text = "Welcome "+name,font ="Algerian 25",bg ="#93D5FF")
        #Button
        check_balance=Button(signin_page,text="Check Balance",padx=30,pady=5,height = 2, width = 20,command=check_balance_f)
        deposit=Button(signin_page,text="Deposit",padx=30,pady=5,height = 2, width = 20,command=deposit_f)
        withdraw=Button(signin_page,text="Transfer",padx=30,pady=5,height = 2, width = 20,command=withdraw_f)
        mini_statement=Button(signin_page,text="Mini Statement",padx=30,pady=5,height = 2, width = 20,command=mini_statement_f)
        log_out_button=Button(signin_page,text="LogOut",padx=30,pady=5,height = 2, width = 20,command=log_out_f)
        
        #Label.grid()
        welcome_message .grid(row=0,column=0,pady=10,padx=20)
        #Buttone.grid()
        check_balance   .grid(row=1,column=0,pady=10,padx=20)
        deposit         .grid(row=2,column=0,pady=10,padx=20)
        withdraw        .grid(row=1,column=1,pady=10,padx=20)
        mini_statement  .grid(row=2,column=1,pady=10,padx=20)
        log_out_button  .grid(row=3,column=0,pady=10,padx=20) 
        signin_page.grab_set()   
    if user_i =='':
        lab = Label(login_page,text ="Please enter Cust_ID",font="Android 15",padx=10,pady=10)
        lab.grid(row=5,column=1)
    elif passw_i =='':
        lab = Label(login_page,text ="Please enter Password",font="Android 15",padx=10,pady=10)
        lab.grid(row=5,column=1,columnspan=2)       
    elif user_i == u and passw_i == p:
        manager_view()
    elif password_real[0][0] == passw_i:
        cursor.execute("SELECT NAME from customer WHERE CUST_ID = :CUSTID;",{ 'CUSTID':user_i})
        n = cursor.fetchall()
        print(password_real[0][0])
        customer_signin_window(cust_id_)
        login_page.grab_set()
    else:
        lab = Label(login_page,text ="Try Again",font="Android 20",padx=10,pady=10)
        lab.grid(row=5,column=1,columnspan=2)


register_page_exists=0
def signup():
    global register_page_exists
    global register_page
    if register_page_exists == 0:    
        os.system('register_page.py')

    if register_page.register_page.winfo_exists():
        register_page_exists=1
    else:
        os.system('register_page.py')
        register_page_exists=1

##########################################################################
#Only Label()
#picture = PhotoImage(file = "")
#lab = Label(login_page, image=picture)
#lab.grid(row=0,column=0,columnspan=2)
username=Label(login_page,text = "CustomerID",font ="none 15",bg ="#93D5FF")
password=Label(login_page,text="Password",font ="none 15",bg ="#93D5FF")
##########################################################################

#Only Entry() 
username_box=Entry(login_page,font="none 15", w=20)
password_box=Entry(login_page,font="none 15", w=20,show="*")
##########################################################################

#Only Buttons()
login=Button(login_page,text="Login",padx=20,pady=3,command=login)
sign_up=Button(login_page,text="SignUp",padx=20,pady=3,command=signup)
##########################################################################
#GRID()
##########################################################################
#Only Label.grid()
username.grid(row=1,column=0,pady=10,padx=20)
password.grid(row=2,column=0,pady=5,padx=2)
##########################################################################
#Only Entry.grid()
username_box.grid(row=1,column=1,pady=10,padx=20)
password_box.grid(row=2,column=1,pady=10,padx=20)
##########################################################################
# Only Button.grid()
login.grid(row=3,column=1,pady=8,padx=20,sticky = W)
sign_up.grid(row=4,column=1,pady=8,padx=20,sticky = W)



mainloop()
data_base.commit()
data_base.close()