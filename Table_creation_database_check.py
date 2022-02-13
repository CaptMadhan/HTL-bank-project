import sqlite3 as base

# create or connect a data base
data_base = base.connect("demo1.db")

# create a cursor
cursor = data_base.cursor()


cursor.execute(''' create table if not exists customerID_generator(row int primary key ,cust_id_g int)
''')
cursor.execute(''' create table if not exists account_NO_generator(row int primary key ,acc_no_g int)
''')
cursor.execute(''' create table if not exists transactionID_generator(row int primary key ,trans_id_g int)
''')
cursor.execute(''' create table if not exists employeeID_generator(row int primary key ,employee_id_g int)
''')
#cursor.execute("INSERT INTO customerID_generator VALUES (:row, :cust_id_g)",
#              {
#                 'row':1 ,
#                'cust_id_g':110011000
#           })
#cursor.execute("INSERT INTO account_NO_generator VALUES (:row, :acc_no)",
#             {
#               'row':1 ,
#             'acc_no':66556655000
#       })
#cursor.execute("INSERT INTO transactionID_generator VALUES (:row, :trans_id_g)",
#             {
#               'row':1 ,
#               'trans_id_g':8888811000
#       })

#cursor.execute("INSERT INTO employeeID_generator VALUES (:row, :employee_id_g)",
#              {
#                 'row':1 ,
#                'employee_id_g':7000
#           })

#cursor.execute("SELECT cust_id_g FROM customerID_generator where row =1")
#x = cursor.fetchall()
#cust_id_ =x[0][0]+1
#print(cust_id_)
#cursor.execute("UPDATE customerID_generator SET cust_id_g = :cust_id_d WHERE row=1;",{
#    'cust_id_d':x[0][0]+1
#    }
#    )
#cursor.execute("INSERT INTO INTEREST VALUES (:INTEREST_ID , :SAVING_INT )",
#              {
#                 'INTEREST_ID':1 ,
#                'SAVING_INT':10
#           })
cursor.execute('''create table IF NOT EXISTS CUSTOMER(
CUST_ID INT PRIMARY KEY,
PASSWORD VARCHAR(20),
NAME VARCHAR(50),
DOB DATE,
AGE INT,
GENDER VARCHAR(6),
EMAIL VARCHAR(50),
CONTACT INT,
PAN INT,
NATIONALITY VARCHAR(15)
);''')
cursor.execute('''create table IF NOT EXISTS CUSTOMER_Address(
CUST_ID INT PRIMARY KEY,
STREET VARCHAR(50),
CITY VARCHAR(20),
STATE VARCHAR(20),
PIN INT,
Foreign Key(CUST_ID) REFERENCES CUSTOMER(CUST_ID) ON DELETE CASCADE
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS INTEREST(
INTEREST_ID INT PRIMARY KEY,
SAVING_INT FLOAT
);''')


cursor.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT(
AC_NO INT PRIMARY KEY,
INTEREST_ID INT,
CUST_ID INT,
AC_TYPE VARCHAR(10),
BALANCE INT, 
INTEREST_AMOUNT INT,
INTEREST_RATE INT,
OPEN_DATE DATE,
Foreign Key(CUST_ID) REFERENCES CUSTOMER(CUST_ID) ON DELETE CASCADE,
Foreign Key(INTEREST_ID) REFERENCES INTEREST(INTEREST_ID) ON DELETE CASCADE
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS BRANCH(
BRANCH_ID INT PRIMARY KEY,
BRANCH_NAME VARCHAR(50)
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS BRANCH_ADDRESS(
BRANCH_ID INT PRIMARY KEY,
STATE VARCHAR(20),
COUNTRY VARCHAR(20),
PIN INT,
Foreign Key(BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) ON DELETE CASCADE
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS OFFICER(
EMP_ID INT PRIMARY KEY,
BRANCH_ID INT,
NAME VARCHAR(50),
EMAIL VARCHAR(50),
GENDER VARCHAR(6),
CONTACT INT,
NATIONALITY VARCHAR(20),
DOB DATE,
USERNAME VARCHAR(20),
PASSWORD VARCHAR(20),
Foreign Key(BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) ON DELETE CASCADE
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS OFFICER_ADDRESS(
EMP_ID INT PRIMARY KEY,
STREET VARCHAR(50),
CITY VARCHAR(50),
STATE VARCHAR(50),
PIN INT,
Foreign Key(EMP_ID) REFERENCES OFFICER(EMP_ID) ON DELETE CASCADE
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS MANAGER(
EMP_ID INT PRIMARY KEY,
BRANCH_ID INT ,
NAME VARCHAR(50),
EMAIL VARCHAR(50),
GENDER VARCHAR(6),
CONTACT INT,
NATIONALITY VARCHAR(20),
DOB DATE,
USERNAME VARCHAR(20),
PASSWORD VARCHAR(20),
Foreign Key(BRANCH_ID) REFERENCES BRANCH(BRANCH_ID) ON DELETE CASCADE
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS MANAGER_ADDRESS(
EMP_ID INT PRIMARY KEY,
STREET VARCHAR(50),
CITY VARCHAR(50),
STATE VARCHAR(50),
PIN INT,
Foreign Key(EMP_ID) REFERENCES OFFICER(EMP_ID) ON DELETE CASCADE
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS(
AC_NO INT ,
TRANS_ID INT PRIMARY KEY,
TRANS_TYPE VARCHAR(20),
DATE_OF_TRANS DATE,
Foreign Key(AC_NO) REFERENCES ACCOUNT(AC_NO) ON DELETE CASCADE);
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS BACKUP_ACCOUNTS_DATA(
AC_NO INT PRIMARY KEY,
INTEREST_ID INT,
CUST_ID INT,
AC_TYPE VARCHAR(10),
BALANCE INT, 
INTEREST_AMOUNT INT,
INTEREST_RATE INT,
OPEN_DATE DATE
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS BACKUP_TRANSACTIONS_DATA(
AC_NO INT ,
TRANS_ID INT PRIMARY KEY,
TRANS_TYPE VARCHAR(20),
DATE_OF_TRANS DATE);
''')
#triggers
#cursor.execute('''CREATE TRIGGER  backup_transaction_data_trigger  BEFORE insert ON TRANSACTIONS 
#                    FOR EACH ROW
#                    BEGIN   
#                    
#                   INSERT INTO BACKUP_TRANSACTIONS_DATA VALUES (NEW.AC_NO,NEW.TRANS_ID ,NEW.TRANS_TYPE,NEW.DATE_OF_TRANS );                            
#                    END
#                    ;
#                ''')
#cursor.execute('''CREATE TRIGGER  backup_account_data  BEFORE insert ON account 
#                    FOR EACH ROW
#                    BEGIN   
#                    
#                    INSERT INTO BACKUP_ACCOUNTS_DATA VALUES (NEW.AC_NO,NEW.INTEREST_ID,NEW.CUST_ID,NEW.AC_TYPE,NEW.BALANCE,NEW.INTEREST_AMOUNT,NEW.INTEREST_RATE,NEW.OPEN_DATE);                            
#                    END
#                    ;
#                ''')


#cursor.execute("INSERT INTO BRANCH VALUES (:BRANCH_ID , :BRANCH_NAME )",
#             {
#               'BRANCH_ID':1001 ,
#             'BRANCH_NAME':"GAT2 RRnagar"
#       })
'''
cursor.execute("INSERT INTO BRANCH_ADDRESS VALUES (:BRANCH_ID ,:STATE,:COUNTRY,:PIN)",
             {
                'BRANCH_ID':1001 ,
                'STATE':"Karnataka",
                'COUNTRY':"India" ,
                'PIN':560060,
       })
'''

#######################################################################################
#admin login data
'''cursor.execute("INSERT INTO CUSTOMER VALUES (:CUST_ID,:password,:NAME, :DOB, :AGE,:GENDER,:EMAIL,:Contact,:pan,:nationality)",
    {
                   
                   'CUST_ID':11111111,
                   'password':12345678,
                   'NAME': "ADMIN",
                   'DOB':'2000-06-01' ,
                   'AGE':20 ,
                   'GENDER':'Male' ,
                   'EMAIL': 'hahahahaha',
                   'Contact': 1010101010,
                   'pan': 1010212212,
                   'nationality':"Indian" 
    })
cursor.execute("INSERT INTO CUSTOMER_address VALUES (:CUST_ID, :STREET,:CITY,:STATE,:PIN)",
                {
                    'CUST_ID':11111111,
                    'STREET':"llllll",
                    'STATE':"Karnataka",
                    'CITY':"bangalore" ,
                    'PIN':560071
                })
cursor.execute("SELECT * FROM CUSTOMER")
print(cursor.fetchall())
cursor.execute("SELECT * FROM CUSTOMER_ADDRESS")
print(cursor.fetchall())
'''
#######################################################################################
#cursor.execute("DELETE from users WHERE oid='0'")


# commit all the changes
data_base.commit()

# close the database
data_base.close()