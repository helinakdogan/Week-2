# Event binding IV (Multiple handler binding)

import tkinter as tk
from tkinter import ttk

def handler_one(event):
    lbl["text"] = "Handler 1 fired."

def handler_two(event):
    lbl["text"] += "\nHandler 2 fired."

def handler_three(event):
    lbl["text"] += "\nHandler 3 fired."

win = tk.Tk()
win.geometry("320x220")
win.title("Week 5")

btn = ttk.Button(win, text="Click")
lbl = ttk.Label(win, text="")
btn.pack(pady=25)
lbl.pack(pady=10)

# First binding
btn.bind("<Button-1>", handler_one)

# Add two more bindings without overwriting
btn.bind("<Button-1>", handler_two, add="+")
btn.bind("<Button-1>", handler_three, add="+")

win.mainloop()
