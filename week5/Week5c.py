# Event binding III (Keyboard)

import tkinter as tk
from tkinter import ttk

def on_key_press(event):
    lbl2["text"] = event.keysym  # event.keycode

def on_focus_in(event):
    lbl2["text"] = "Focus gained"

def on_focus_out(event):
    lbl2["text"] = "Focus lost"

def on_return_pressed(event):
    val = entry.get().upper()
    entry.delete(0, "end")
    entry.insert(0, val)

def on_key_combination(event):
    lbl2["text"] = "Key combination pressed"

win = tk.Tk()
win.geometry("400x250")
win.title("Week 5")

lbl1 = ttk.Label(win, text="Enter your text and press <Return>")
entry = ttk.Entry(win, width=30)
btn = ttk.Button(win, text="Button")
lbl2 = ttk.Label(win, text="", font=("Consolas", 12))

lbl1.pack(pady=20)
entry.pack(pady=(0, 20))
btn.pack(pady=(0, 20))
lbl2.pack()

entry.bind("<Key>", on_key_press)  # KeyPress, KeyRelease, F1, F2, ...
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)
entry.bind("<Return>", on_return_pressed)
win.bind("<Control-a>", on_key_combination) # Control-Shift-A, ...

win.mainloop()
