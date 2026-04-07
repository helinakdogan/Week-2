# Progressbar with after()
# widget.after(delay_ms, func, *args)
# Schedules func(*args) to be called after delay_ms milliseconds.

import tkinter as tk
from tkinter import ttk

running = False # Flag to manage the scheduled updates

def step(v):
    global running
    if running and v <= 100:
        progressbar1["value"] = v
        # Schedule the next step after 1000ms (1 second)
        # This keeps the Main Loop free to handle events
        win.after(1000, step, v + 20)
    else:
        running = False

def run_progressbar():
    global running
    if not running:
        running = True
        step(0) # Start the first step of the sequence

def stop_progressbar():
    global running
    running = False # Break the 'after' scheduling chain

win = tk.Tk()
win.geometry("300x200")
win.title("Week 5")

progressbar1 = ttk.Progressbar(win, orient="horizontal", length=250, mode="determinate")
progressbar1.pack(pady=20)

ttk.Button(win, text="Run", command=run_progressbar).pack(pady=(0, 10))
ttk.Button(win, text="Stop", command=stop_progressbar).pack()

win.mainloop()