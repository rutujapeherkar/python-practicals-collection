# Python Project -QR Code Generator
# Developed by Rutuja
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
import threading


def open_input_page():
    welcome_frame.pack_forget()  # Hide the welcome frame
    input_frame.pack()  # Show the input frame


def generate_qr():
    name = name_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()

    if not name or not mobile or not email:
        messagebox.showerror("Error", "Please fill in all fields..")
        return

    data = f"Name: {name}\nMobile: {mobile}\nEmail: {email}"

    # Hide the input frame
    input_frame.pack_forget()

    # TO Show loading frame
    loading_frame.pack()

    # Generate QR code in a separate thread
    qr_thread = threading.Thread(target=generate_qr_code, args=(data,))
    qr_thread.start()


def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    qr_img.save("qr_code.png")

    # For LoadinG the generated QR code image
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk

    # hide loading after 3 sec
    window.after(3000, hide_loading_frame)


def hide_loading_frame():
    loading_frame.pack_forget()
    # Showing the input frame again
    input_frame.pack()
    messagebox.showinfo("QR Code Generated", "QR Code generated successfully!")
    show_rating_option()


def show_rating_option():
    rating_frame.pack()


# Rating function
def rate_app(stars):
    messagebox.showinfo("Rating", f"Rutuja thanking you for giving {stars} stars!")


window = Tk()
window.title("QR CODE GENERATOR")
window.configure(bg="gold")
window.geometry("500x500")
# Welcome Page Frame
welcome_frame = Frame(window)
welcome_frame.pack(padx=20, pady=20)

# Start button
start_button = Button(welcome_frame, text="Start", command=open_input_page, background="blue", foreground="white",
                      font=("Helvetica", 14, "bold"))
start_button.pack(pady=10)

# Input Page Frame
input_frame = Frame(window)
input_frame.configure(padx=200)

name_label = Label(input_frame, text="Name:", font=("Helvetica", 14, "bold"), pady=15, bg="OrangeRed",
                   foreground="White")
name_label.grid(row=0, column=0, padx=10, sticky="e")
name_entry = Entry(input_frame, font=("Helvetica", 14), bd=2, relief=SOLID)
name_entry.grid(row=0, column=1, padx=5)

mobile_label = Label(input_frame, text="Mobile:", font=("Helvetica", 14, "bold"), pady=5, bg="OrangeRed",
                     foreground="White")
mobile_label.grid(row=1, column=0, padx=10, sticky="e")
mobile_entry = Entry(input_frame, font=("Helvetica", 14), bd=2, relief=SOLID)
mobile_entry.grid(row=1, column=1, padx=5)

email_label = Label(input_frame, text="Email:", font=("Helvetica", 14, "bold"), pady=5, bg="OrangeRed",
                    foreground="White")
email_label.grid(row=2, column=0, padx=10, sticky="e")
email_entry = Entry(input_frame, font=("", 14), bd=2, relief=SOLID)
email_entry.grid(row=2, column=1, padx=5)

generate_button = Button(input_frame, text="Generate QR Code", command=generate_qr, background="green",
                         foreground="white", font=("Helvetica", 14, "bold"))
generate_button.grid(row=3, column=0, columnspan=2, pady=30)

# QR Code Label
qr_label = Label(input_frame)
qr_label.grid(row=4, column=0, columnspan=2, pady=10)

# Loading Frame
loading_frame = Frame(window)
loading_label = Label(loading_frame, text="Please wait, your QR code is getting ready...",
                      font=("Times new roman", 25, "bold"), bg="OrangeRed", foreground="YeLLOW")
loading_label.pack(pady=50)

# Rating Frame
rating_frame = Frame(window)
rating_label = Label(rating_frame, text="Please rate the application:", font=("Helvetica", 14, "bold"))
rating_label.pack(pady=10)

# Rating buttons
stars_frame = Frame(rating_frame)
stars_frame.pack()

star1_button = Button(stars_frame, text="⭐", command=lambda: rate_app(1), bg="orange")
star1_button.grid(row=0, column=0, padx=5)
star2_button = Button(stars_frame, text="⭐⭐", command=lambda: rate_app(2), bg="orange")
star2_button.grid(row=0, column=1, padx=5)
star3_button = Button(stars_frame, text="⭐⭐⭐", command=lambda: rate_app(3), bg="orange")
star3_button.grid(row=0, column=2, padx=5)

# Styling
welcome_frame.configure(bg="white")
input_frame.configure(bg="OrangeRed")
loading_frame.configure(bg="light yellow")
rating_frame.configure(bg="red")
name_entry.focus()

# Initially hide the input frame, loading frame, and rating frame
input_frame.pack_forget()
loading_frame.pack_forget()
rating_frame.pack_forget()

window.mainloop()
