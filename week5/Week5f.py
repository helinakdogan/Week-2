# Custom Event
# This allows communication between widgets.
# For instance, a Save button could generate a <<FileSaved>> event that other widgets listen for.

import tkinter as tk
from tkinter import ttk

def on_click():
	win.event_generate("<<CustomEvent>>")

def on_custom_event(event):
	lbl["text"] = "Custom event fired."

win = tk.Tk()
win.geometry("300x150")
win.title("Week 5")

btn = ttk.Button(win, text="Button", command=on_click)
lbl = ttk.Label(win, justify="center")

btn.pack(pady=20)
lbl.pack()

win.bind("<<CustomEvent>>", on_custom_event)

win.mainloop()