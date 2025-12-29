import tkinter as tk

class ControlForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Control Form")

        # Create a frame for the form
        self.form_frame = tk.Frame(self)
        self.form_frame.pack(padx=10, pady=10)

        # Labels
        tk.Label(self.form_frame, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Label(self.form_frame, text="Age:").grid(row=1, column=0, sticky="e")
        tk.Label(self.form_frame, text="Email:").grid(row=2, column=0, sticky="e")

        # Entries
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=1)
        self.age_entry = tk.Entry(self.form_frame)
        self.age_entry.grid(row=1, column=1)
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=2, column=1)

        # Buttons
        self.add_button = tk.Button(self.form_frame, text="Add", command=self.add_control)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_control(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()

        # Do something with the entered data (e.g., print it)
        print(f"Name: {name}, Age: {age}, Email: {email}")

if __name__ == "__main__":
    app = ControlForm()
    app.mainloop()
