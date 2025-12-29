import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("450x400")
        self.root.config(bg="#F3F4F6")

        # 🎨 Color palette
        self.primary_color = "#4CAF50"
        self.secondary_color = "#E74C3C"
        self.text_color = "#2C3E50"

        # Random number between 1 and 100
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # 🧱 Main frame
        self.card = tk.Frame(root, bg="white", bd=2, relief="ridge")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

        # 🏷️ Title label
        self.title_label = tk.Label(self.card, text="🎯 Guess The Number!", font=("Poppins", 18, "bold"),
                                    bg="white", fg=self.text_color)
        self.title_label.pack(pady=15)

        # ℹ️ Instruction
        self.instruction_label = tk.Label(self.card, text="Enter a number between 1 and 100 👇",
                                          font=("Poppins", 11), bg="white", fg="#555")
        self.instruction_label.pack()

        # 🔢 Input box
        self.input_box = tk.Entry(self.card, font=("Poppins", 13), width=10, justify="center", bd=2, relief="solid")
        self.input_box.pack(pady=10)
        self.input_box.bind("<Return>", self.check_guess_event)  # ENTER key event

        # ✅ Guess button
        self.guess_button = tk.Button(self.card, text="Check Guess", font=("Poppins", 12, "bold"),
                                      bg=self.primary_color, fg="white", activebackground="#45a049",
                                      cursor="hand2", relief="flat", command=self.check_guess)
        self.guess_button.pack(pady=8)
        self.guess_button.bind("<Enter>", lambda e: self.guess_button.config(bg="#45a049"))
        self.guess_button.bind("<Leave>", lambda e: self.guess_button.config(bg=self.primary_color))

        # 💬 Feedback label
        self.feedback_label = tk.Label(self.card, text="", font=("Poppins", 13, "italic"),
                                       bg="white", fg=self.text_color)
        self.feedback_label.pack(pady=10)

        # 🔁 Reset button
        self.reset_button = tk.Button(self.card, text="Reset Game", font=("Poppins", 11, "bold"),
                                      bg=self.secondary_color, fg="white", activebackground="#c0392b",
                                      cursor="hand2", relief="flat", command=self.reset_game)
        self.reset_button.pack(pady=8)
        self.reset_button.bind("<Enter>", lambda e: self.reset_button.config(bg="#c0392b"))
        self.reset_button.bind("<Leave>", lambda e: self.reset_button.config(bg=self.secondary_color))

    # 🎯 Event Handling (Button click)
    def check_guess(self):
        try:
            guess = int(self.input_box.get())  # May raise ValueError
            if guess < 1 or guess > 100:
                raise ValueError("Out of range")

            self.attempts += 1

            # Compare guesses
            if guess < self.secret_number:
                self.feedback_label.config(text="📉 Too Low! Try Again.", fg="#E67E22")
            elif guess > self.secret_number:
                self.feedback_label.config(text="📈 Too High! Try Again.", fg="#2980B9")
            else:
                messagebox.showinfo("🎉 Congratulations!",
                                    f"You guessed it right in {self.attempts} attempts!\n\nNumber was {self.secret_number}.")
                self.reset_game()

        except ValueError:
            # ⚠️ Exception Handling
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 100.")
            self.input_box.delete(0, tk.END)

    # 🎯 Event Handling (Enter key)
    def check_guess_event(self, event):
        self.check_guess()

    # 🔁 Reset Game
    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="")
        self.input_box.delete(0, tk.END)
        self.feedback_label.config(text="Game reset! Start guessing again 🎲", fg=self.text_color)


# 🚀 Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
