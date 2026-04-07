# Variable tracing (trace_add)

import tkinter as tk
from tkinter import ttk

DEFAULT_TEXT = "Waiting for input..."

def on_text_change(*_):
    val = var.get().strip()
    text = f"Current value: {val}" if val else DEFAULT_TEXT
    lbl.config(text=text)

win = tk.Tk()
win.geometry("300x200")
win.title("Week 5")

var = tk.StringVar()
entry = ttk.Entry(win, textvariable=var)
lbl = ttk.Label(win, text=DEFAULT_TEXT)

entry.pack(pady=20)
lbl.pack()

# trace_add modes: "write", "read", "unset"
# The callback receives three arguments: var_name, index, mode (often ignored with *_)
var.trace_add("write", on_text_change)

win.mainloop()
