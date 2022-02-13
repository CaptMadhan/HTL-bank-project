from tkinter import *
import os
import sqlite3 as base
import datetime
data_base = base.connect("demo1.db")
cursor = data_base.cursor()

cursor.execute("UPDATE ACCOUNT SET INTEREST_RATE= :INTEREST_RATE WHERE ac_no = 66556655001;",{
'INTEREST_RATE':0
}
)


data_base.commit()
data_base.close()