import tkinter as tk
from tkinter import messagebox


def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_text.get("1.0", "end-1c")

    # Validation (you can add more validation as needed)
    if not name or not email or not phone or not address:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Process the form data (you can save to a file or send it somewhere)
    # For now, just display it
    messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}")


# Create the main window
root = tk.Tk()
root.title("Job Application Form")

# Name field
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Email field
tk.Label(root, text="Email:").grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Phone field
tk.Label(root, text="Phone:").grid(row=2, column=0, sticky="w")
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

# Address field
tk.Label(root, text="Address:").grid(row=3, column=0, sticky="w")
address_text = tk.Text(root, height=4, width=30)
address_text.grid(row=3, column=1, padx=5, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
