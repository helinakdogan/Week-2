# Progressbar with threading

import tkinter as tk
from tkinter import ttk
import threading
from time import sleep

running = False # Flag to control the background task

def progressbar_task():
    global running
    for i in range(0, 101, 20):
        if not running: break # Exit loop if stop signal is received
        progressbar1["value"] = i
        sleep(1) # Simulate a time-consuming background task
    running = False

def run_progressbar():
    global running
    if not running: # Prevent starting multiple threads
        running = True
        # Run task in a separate thread to keep GUI responsive
        # daemon=True stops the thread when the main window is closed
        threading.Thread(target=progressbar_task, daemon=True).start()

def stop_progressbar():
    global running
    running = False # Signal the thread to stop
    progressbar1.stop()

win = tk.Tk()
win.geometry("300x200")
win.title("Week 5")

progressbar1 = ttk.Progressbar(win, orient="horizontal", length=250, mode="determinate")
progressbar1.pack(pady=20)

ttk.Button(win, text="Run", command=run_progressbar).pack(pady=(0, 10))
ttk.Button(win, text="Stop", command=stop_progressbar).pack()

win.mainloop()