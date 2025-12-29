# 🌈 QR Code Generator Project
# Developed by Rutuja Peherkar
# Enhanced Stylish Version with Event & Exception Handling ✨

from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import qrcode
import threading
import time


# ======================== QR Generator Logic ==========================

def open_input_page():
    welcome_frame.pack_forget()
    input_frame.pack(pady=40)


def generate_qr():
    name = name_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()

    try:
        if not name or not mobile or not email:
            raise ValueError("All fields are required!")

        if not mobile.isdigit() or len(mobile) != 10:
            raise ValueError("Please enter a valid 10-digit mobile number.")

        data = f"Name: {name}\nMobile: {mobile}\nEmail: {email}"

        input_frame.pack_forget()
        show_loading()
        qr_thread = threading.Thread(target=generate_qr_code, args=(data,))
        qr_thread.start()

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))


def generate_qr_code(data):
    time.sleep(2)  # Simulate processing delay
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    qr_img.save("qr_code.png")

    qr_tk = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_tk)
    qr_label.image = qr_tk

    window.after(2000, hide_loading)


def show_loading():
    loading_frame.pack(pady=40)
    progress.start(15)


def hide_loading():
    progress.stop()
    loading_frame.pack_forget()
    input_frame.pack(pady=40)
    messagebox.showinfo("Success", "QR Code generated successfully!")
    rating_frame.pack(pady=20)


def rate_app(stars):
    messagebox.showinfo("Rating", f"⭐ Thank you for rating us {stars} stars! ⭐")


# ======================== Window Setup ==========================

window = Tk()
window.title("🌈 Stylish QR Code Generator")
window.geometry("700x700")
window.resizable(False, False)

# Gradient Background
canvas = Canvas(window, width=700, height=700)
canvas.pack(fill="both", expand=True)

for i in range(700):
    color = f"#ff{hex(255 - i // 3)[2:]:>02}aa"
    canvas.create_line(0, i, 700, i, fill=color)

# Main container to hold frames
main_frame = Frame(canvas, bg="#ffe5b4")
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# ======================== Frames ==========================

welcome_frame = Frame(main_frame, bg="#fff0f5")
input_frame = Frame(main_frame, bg="#ffb6c1")
loading_frame = Frame(main_frame, bg="#fff8dc")
rating_frame = Frame(main_frame, bg="#f5f5f5")

# ======================== Welcome Frame ==========================

Label(welcome_frame, text="✨ Welcome to Rutuja’s QR Generator ✨",
      font=("Comic Sans MS", 20, "bold"), bg="#fff0f5", fg="#ff1493").pack(pady=40)

Button(welcome_frame, text="Start",
       command=open_input_page,
       bg="#ff69b4", fg="white",
       font=("Helvetica", 16, "bold"),
       relief="raised", padx=20, pady=10).pack(pady=20)

welcome_frame.pack(pady=40)

# ======================== Input Frame ==========================

Label(input_frame, text="Enter Your Details", font=("Arial Rounded MT Bold", 20), bg="#ffb6c1", fg="white").grid(row=0, column=0, columnspan=2, pady=20)

Label(input_frame, text="Name:", font=("Arial", 14, "bold"), bg="#ffb6c1").grid(row=1, column=0, pady=5, sticky="e")
name_entry = Entry(input_frame, font=("Arial", 14), width=25)
name_entry.grid(row=1, column=1, pady=5, padx=10)

Label(input_frame, text="Mobile:", font=("Arial", 14, "bold"), bg="#ffb6c1").grid(row=2, column=0, pady=5, sticky="e")
mobile_entry = Entry(input_frame, font=("Arial", 14), width=25)
mobile_entry.grid(row=2, column=1, pady=5, padx=10)

Label(input_frame, text="Email:", font=("Arial", 14, "bold"), bg="#ffb6c1").grid(row=3, column=0, pady=5, sticky="e")
email_entry = Entry(input_frame, font=("Arial", 14), width=25)
email_entry.grid(row=3, column=1, pady=5, padx=10)

generate_button = Button(input_frame, text="Generate QR Code",
                         command=generate_qr,
                         bg="#32cd32", fg="white",
                         font=("Helvetica", 14, "bold"), relief="raised", padx=20, pady=10)
generate_button.grid(row=4, column=0, columnspan=2, pady=20)

qr_label = Label(input_frame, bg="#ffb6c1")
qr_label.grid(row=5, column=0, columnspan=2, pady=10)

# ======================== Loading Frame ==========================

Label(loading_frame, text="Generating your QR Code...",
      font=("Comic Sans MS", 16, "bold"), bg="#fff8dc", fg="#ff4500").pack(pady=20)

progress = ttk.Progressbar(loading_frame, mode='indeterminate', length=300)
progress.pack(pady=20)

# ======================== Rating Frame ==========================

Label(rating_frame, text="Please rate the app 😊",
      font=("Comic Sans MS", 14, "bold"), bg="#f5f5f5").pack(pady=10)

stars_frame = Frame(rating_frame, bg="#f5f5f5")
stars_frame.pack()

for i in range(1, 6):
    Button(stars_frame, text="⭐" * i, bg="#ffdab9", command=lambda s=i: rate_app(s),
           font=("Arial", 12, "bold"), relief="ridge").grid(row=0, column=i, padx=4)

# Initially hide other frames
input_frame.pack_forget()
loading_frame.pack_forget()
rating_frame.pack_forget()

window.mainloop()
