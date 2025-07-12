import tkinter as tk
import random
from plyer import notification

# Load motivational quotes
with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = f.readlines()

# Timer settings (adjust for testing)
FOCUS_TIME = 10        # 10 seconds for quick testing
BREAK_TIME = 5         # 5 seconds

# GUI setup
root = tk.Tk()
root.title("Study Timer and Break Reminder")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

timer_label = tk.Label(root, text="Ready to Focus!", font=("Arial", 24), bg="#f5f5f5")
timer_label.pack(pady=40)

# ✅ FIXED update_timer function using `after()` (no threading, no errors)
def update_timer(t, label, session_name):
    mins, secs = divmod(t, 60)
    time_str = '{:02d}:{:02d}'.format(mins, secs)
    label.config(text=f"{session_name}: {time_str}")

    if t > 0:
        root.after(1000, update_timer, t - 1, label, session_name)
    else:
        quote = random.choice(quotes).strip()
        notification.notify(
            title=f"{session_name} Complete!",
            message=quote,
            timeout=5
        )
        label.config(text=f"{session_name} Done! ✨")

# Button functions — no threading
def start_focus():
    update_timer(FOCUS_TIME, timer_label, "Focus")

def start_break():
    update_timer(BREAK_TIME, timer_label, "Break")

# Buttons
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=20)

focus_btn = tk.Button(btn_frame, text="Start Focus", command=start_focus, bg="#4CAF50", fg="white", width=15)
focus_btn.grid(row=0, column=0, padx=10)

break_btn = tk.Button(btn_frame, text="Start Break", command=start_break, bg="#2196F3", fg="white", width=15)
break_btn.grid(row=0, column=1, padx=10)

# Start the GUI loop
root.mainloop()
