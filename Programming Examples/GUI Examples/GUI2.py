import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text = "Hello, Tkinter")
greeting.pack()
window.mainloop()
label = tk.Label(text = "Hello, Tkinter")
label = tk.Label(text = "Hello, Tkinter", foreground = "white", background = "black")
#set the backgorund color to black)
#set the text color to white


master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
