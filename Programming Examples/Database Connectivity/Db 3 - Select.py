
import sqlite3

con = sqlite3.connect('SQLite_Python.db')

cursorObj = con.cursor()

cursorObj.execute("select * from Student_Details")

rows = cursorObj.fetchall()

print("Student Details are :- ")
for row in rows :
    print(row)

con.commit()

con.close()
