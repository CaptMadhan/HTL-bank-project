from tkinter import *
import os
import sqlite3 as base
import datetime
data_base = base.connect("demo1.db")
cursor = data_base.cursor()


cursor.execute("DELETE FROM customerID_generator")
cursor.execute("DELETE FROM account_NO_generator")
cursor.execute("DELETE  FROM transactionID_generator")
cursor.execute("DELETE  FROM employeeID_generator")
cursor.execute("DELETE FROM CUSTOMER")
cursor.execute("DELETE FROM Interest")
cursor.execute("DELETE  FROM CUSTOMER_Address")
cursor.execute("DELETE  FROM ACCOUNT")
cursor.execute("DELETE  FROM BRANCH")
cursor.execute("DELETE  FROM OFFICER")
cursor.execute("DELETE  FROM BRANCH_ADDRESS")
cursor.execute("DELETE  FROM OFFICER_ADDRESS")
cursor.execute("DELETE  FROM TRANSACTIONS")
cursor.execute("DELETE  FROM BACKUP_ACCOUNTS_DATA")
cursor.execute("DELETE  FROM BACKUP_TRANSACTIONS_DATA")
cursor.execute("INSERT INTO BRANCH VALUES (:BRANCH_ID , :BRANCH_NAME )",
             {
               'BRANCH_ID':1001 ,
             'BRANCH_NAME':"GAT2 RRnagar"
       })
cursor.execute("INSERT INTO customerID_generator VALUES (:row, :cust_id_g)",
              {
                 'row':1 ,
                'cust_id_g':110011000
           })
cursor.execute("INSERT INTO account_NO_generator VALUES (:row, :acc_no)",
             {
               'row':1 ,
             'acc_no':66556655000
       })
cursor.execute("INSERT INTO transactionID_generator VALUES (:row, :trans_id_g)",
             {
               'row':1 ,
               'trans_id_g':8888811000
       })

cursor.execute("INSERT INTO employeeID_generator VALUES (:row, :employee_id_g)",
              {
                 'row':1 ,
                'employee_id_g':7000
           })

cursor.execute("INSERT INTO INTEREST VALUES (:INTEREST_ID , :SAVING_INT )",
              {
                 'INTEREST_ID':1 ,
                'SAVING_INT':10
           })
print(cursor.fetchall())

data_base.commit()
data_base.close()