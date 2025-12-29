import tkinter as tk
from tkinter import messagebox

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password are correct
    if username =="rutuja" and password =="rutu123":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
pavan = tk.Tk()
pavan.title("Login Form")

# Create and place labels
label_username = tk.Label(pavan, text="Username:")
label_username.grid(row=0, column=0, sticky=tk.E)
label_password = tk.Label(pavan, text="Password:")
label_password.grid(row=1, column=0, sticky=tk.E)

# Create and place entry fields
entry_username = tk.Entry(pavan)
entry_username.grid(row=0, column=1)
entry_password = tk.Entry(pavan, show="*")  # Show * for password
entry_password.grid(row=1, column=1)

# Create and place login button
login_button = tk.Button(pavan, text="Login",bg="green", command=check_credentials)
login_button.grid(row=2, columnspan=2)

# Run the application
pavan.mainloop()