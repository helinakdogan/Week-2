# Event unbinding

import tkinter as tk
from tkinter import ttk

def on_unbind(event):
    # btn.unbind("<Button-1>")
    try:
        btn.unbind("<Button-1>", h2)
    except tk.TclError: # Exception occurs if the binding is already removed.
        pass

    lbl["text"] = ""

def handler_one(event):
    lbl["text"] = "Handler 1 fired."

def handler_two(event):
    lbl["text"] += "\nHandler 2 fired."

def handler_three(event):
    lbl["text"] += "\nHandler 3 fired."

win = tk.Tk()
win.geometry("320x220")
win.title("Week 5")

# Create an info label
tk.Label(win, text="Click the button, press Esc, then click the button again.").pack(pady=10, side="bottom")

btn = ttk.Button(win, text="Click")
lbl = ttk.Label(win, text="")
btn.pack(pady=25)
lbl.pack(pady=10)

# First binding
h1 = btn.bind("<Button-1>", handler_one)

# Add two more bindings without overwriting
h2 = btn.bind("<Button-1>", handler_two, add="+")
h3 = btn.bind("<Button-1>", handler_three, add="+")

# Bind Escape key to unbind handler(s)
win.bind("<Escape>", on_unbind)

win.mainloop()
