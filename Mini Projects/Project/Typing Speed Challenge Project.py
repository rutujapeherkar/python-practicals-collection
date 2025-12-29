# 🌟 Advanced Typing Speed Challenge
# Designed & Developed by Rutuja 💻

import tkinter as tk
from tkinter import messagebox
import random
import time

# -----------------------------
# Word Bank (Unique Words)
# -----------------------------
WORDS = [
    "ambition", "galaxy", "keyboard", "velocity", "courage", "dynamic",
    "whisper", "innovation", "journey", "harmony", "mystery", "vibrant",
    "freedom", "pioneer", "creation", "serenity", "adventure", "limitless",
    "momentum", "explore", "gravity", "wonder", "radiant", "universe",
    "optimism", "bloom", "elevate", "cosmic", "vision", "spark"
]


# -----------------------------
# Main Typing Game Class
# -----------------------------
class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🌈 Typing Speed Challenge - by Rutuja 💫")
        self.root.geometry("900x600")
        self.root.config(bg="#FDEFF4")

        # Variables
        self.score = 0
        self.time_left = 45
        self.current_word = ""
        self.is_running = False

        # Title Label
        self.title = tk.Label(
            root, text="⌨️ Typing Speed Challenge ⌨️",
            font=("Comic Sans MS", 30, "bold"),
            fg="#6A1B9A", bg="#FDEFF4"
        )
        self.title.pack(pady=20)

        # Word Display Label
        self.word_label = tk.Label(
            root, text="Press Start to Begin",
            font=("Arial Rounded MT Bold", 28),
            fg="#D81B60", bg="#FDEFF4"
        )
        self.word_label.pack(pady=25)

        # Entry Box
        self.input_box = tk.Entry(
            root, font=("Consolas", 20), justify="center",
            bd=3, relief="solid", width=25
        )
        self.input_box.pack(pady=10)
        self.input_box.bind("<Return>", self.check_word)

        # Info Frame (Score & Timer)
        info_frame = tk.Frame(root, bg="#FDEFF4")
        info_frame.pack(pady=15)

        self.timer_label = tk.Label(
            info_frame, text="⏰ Time: 45s",
            font=("Helvetica", 18, "bold"), fg="#E53935", bg="#FDEFF4"
        )
        self.timer_label.grid(row=0, column=0, padx=50)

        self.score_label = tk.Label(
            info_frame, text="⭐ Score: 0",
            font=("Helvetica", 18, "bold"), fg="#43A047", bg="#FDEFF4"
        )
        self.score_label.grid(row=0, column=1, padx=50)

        # Buttons Frame
        button_frame = tk.Frame(root, bg="#FDEFF4")
        button_frame.pack(pady=20)

        self.start_btn = tk.Button(
            button_frame, text="🚀 Start", font=("Helvetica", 14, "bold"),
            bg="#4CAF50", fg="white", padx=20, pady=5, command=self.start_game
        )
        self.start_btn.grid(row=0, column=0, padx=20)

        self.reset_btn = tk.Button(
            button_frame, text="🔁 Reset", font=("Helvetica", 14, "bold"),
            bg="#FF9800", fg="white", padx=20, pady=5, command=self.reset_game
        )
        self.reset_btn.grid(row=0, column=1, padx=20)

        # Feedback Label
        self.feedback = tk.Label(
            root, text="", font=("Comic Sans MS", 20, "bold"),
            bg="#FDEFF4", fg="#1976D2"
        )
        self.feedback.pack(pady=20)

        # Footer
        self.footer = tk.Label(
            root, text="💡 Tip: Type the words fast & accurately. Press Enter to submit!",
            font=("Arial", 12, "italic"), bg="#FDEFF4", fg="#5D4037"
        )
        self.footer.pack(side="bottom", pady=10)

    # -----------------------------
    # Start Game
    # -----------------------------
    def start_game(self):
        if not self.is_running:
            self.is_running = True
            self.score = 0
            self.time_left = 45
            self.score_label.config(text="⭐ Score: 0")
            self.timer_label.config(text="⏰ Time: 45s", fg="#E53935")
            self.feedback.config(text="")
            self.next_word()
            self.update_timer()
            self.input_box.delete(0, tk.END)
            self.input_box.focus()

    # -----------------------------
    # Pick Next Word
    # -----------------------------
    def next_word(self):
        try:
            self.current_word = random.choice(WORDS)
            self.word_label.config(text=self.current_word, fg="#D81B60")
        except Exception as e:
            messagebox.showerror("Error", f"Word loading failed:\n{e}")

    # -----------------------------
    # Check Word on Enter
    # -----------------------------
    def check_word(self, event):
        if not self.is_running:
            return

        typed = self.input_box.get().strip().lower()
        self.input_box.delete(0, tk.END)

        try:
            if typed == "":
                raise ValueError("You didn’t type anything!")

            if typed == self.current_word.lower():
                self.score += 1
                self.score_label.config(text=f"⭐ Score: {self.score}")
                self.feedback.config(text=random.choice(["✅ Awesome!", "🔥 Perfect!", "⚡ Great job!", "🌟 Spot on!"]),
                                     fg="#43A047")
            else:
                self.feedback.config(text=random.choice(["❌ Oops!", "😅 Try again!", "💢 Missed it!"]),
                                     fg="#E53935")

            self.next_word()

        except ValueError as ve:
            messagebox.showwarning("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Unexpected Error", f"Something went wrong:\n{e}")

    # -----------------------------
    # Timer Countdown
    # -----------------------------
    def update_timer(self):
        if self.time_left > 0 and self.is_running:
            self.time_left -= 1
            color = "#E53935" if self.time_left <= 10 else "#1565C0"
            self.timer_label.config(text=f"⏰ Time: {self.time_left}s", fg=color)
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    # -----------------------------
    # End Game
    # -----------------------------
    def end_game(self):
        self.is_running = False
        feedback = "🎉 Amazing Speed!" if self.score >= 20 else "👍 Good Effort!" if self.score >= 10 else "😅 Keep Practicing!"
        messagebox.showinfo("Time’s Up!", f"{feedback}\nFinal Score: {self.score}")
        self.word_label.config(text="Game Over!", fg="#9C27B0")

    # -----------------------------
    # Reset Game
    # -----------------------------
    def reset_game(self):
        self.is_running = False
        self.score = 0
        self.time_left = 45
        self.word_label.config(text="Press Start to Begin", fg="#D81B60")
        self.feedback.config(text="")
        self.timer_label.config(text="⏰ Time: 45s", fg="#E53935")
        self.score_label.config(text="⭐ Score: 0")
        self.input_box.delete(0, tk.END)


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingGame(root)
    root.mainloop()
