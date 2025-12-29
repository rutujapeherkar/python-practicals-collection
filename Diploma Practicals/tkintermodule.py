from tkinter import *
root=Tk()
name=Label(root,text="enter name: ")

e1=Entry(root)
b1=Button(root,text="4submit",bg="gray",foreground="white")

e1.grid(row=0,column=1)
name.grid(row=0,column=0)
b1.grid(row=1,column=1)
root.mainloop()