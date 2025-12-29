import sqlite3

con = sqlite3.connect('SQLite_Python.db')

cursorObj = con.cursor()

cursorObj.execute("insert into Student_Details values (226022, 'Rutuja Peherkar', 'CO', 90.67)")

cursorObj.execute("insert into Student_Details values (226027, 'Siddhi Shelke', 'AIML', 90.00)")

cursorObj.execute("insert into Student_Details values (227044, 'Pavan More', 'IT', 94.27)")

cursorObj.execute("insert into Student_Details values (227047, 'Shreyas Peherkar', 'CSE', 93.67)")

cursorObj.execute("insert into Student_Details values (226029, 'Aransh Jadhav', 'AI', 95.34)")

con.commit()

con.close()