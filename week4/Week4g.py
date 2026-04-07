# Spinbox

import tkinter as tk

def apply_font():
    size = size_var.get()
    preview_label.configure(font=("Arial", size, "normal")) # bold italic

win = tk.Tk()
win.geometry("300x150")
win.title("Week 4")

size_var = tk.IntVar(value=12)
font_size = tk.Spinbox(win, from_=8, to=38, increment=1, textvariable=size_var, width=5, command=apply_font)
font_size.pack(pady=5)

preview_label = tk.Label(win, text="Preview Text")
preview_label.pack(pady=5)

win.mainloop()
