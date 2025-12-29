from tkinter import *

def event_method1():
    fobj = open("all_login_form_data.txt", "a")
    uid = txt1.get()
    passw = txt2.get()
    fobj.write(uid + "," +passw + "\n")
    fobj.close()

base=Tk()
base.geometry("700x600")
base.title("Login Form")

ft1 = ("Comic Sans MS", 19)
btn1 = Button(base, text="Submit", font=ft1, fg ="white",bg = "green", command=event_method1)
lb1 = Label(base, text="Enter User ID ", font=ft1)
lb2 = Label(base, text="Enter Password ", font=ft1)
txt1 = Entry(base, font=ft1)
txt2 = Entry(base, font=ft1)

lb1.place(x=50, y=50)
lb2.place(x=50, y=150)
txt1.place(x=350, y=40)
txt2.place(x=350, y=150)
btn1.place(x=300, y=240)

base.mainloop()