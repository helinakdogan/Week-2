# Basic tkinter GUI without classes

import tkinter as tk
from tkinter import ttk

def on_ok_clicked():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    print(f"First Name: {first_name}\nLast Name: {last_name}\n")

def on_cancel_clicked():
    win.destroy()

win = tk.Tk()
win.title("Week 7")
win.resizable(False, False)

frame = ttk.Frame(win, padding=30)
frame.pack(fill="both", expand=True)

lbl_heading = ttk.Label(frame, text="Please enter your name and surname:")
lbl_heading.grid(row=0, column=0, padx=(0, 5), pady=(0, 15), columnspan=2, sticky="w")

lbl_first_name = ttk.Label(frame, text="First Name:")
lbl_first_name.grid(row=1, column=0, sticky="e", padx=(0, 5), pady=10)

entry_first_name = ttk.Entry(frame, width=30)
entry_first_name.grid(row=1, column=1, pady=10)

lbl_last_name = ttk.Label(frame, text="Last Name:")
lbl_last_name.grid(row=2, column=0, sticky="e", padx=(0, 5), pady=10)

entry_last_name = ttk.Entry(frame, width=30)
entry_last_name.grid(row=2, column=1, pady=10)

btn_frame = ttk.Frame(frame)
btn_frame.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="e")

btn_ok = ttk.Button(btn_frame, text="OK", width=8, command=on_ok_clicked)
btn_ok.pack(side="left", padx=5)

btn_cancel = ttk.Button(btn_frame, text="Cancel", width=8, command=on_cancel_clicked)
btn_cancel.pack(side="left", padx=5)

entry_first_name.focus_set()
win.mainloop()