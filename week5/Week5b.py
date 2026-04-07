# Event binding II (Mouse move, ComboboxSelected)

import tkinter as tk
from tkinter import ttk

def on_click(event):
    # lbl.configure(text=event)

    button_name = {1: "Left", 2: "Middle", 3: "Right"}.get(event.num, "Unknown")

    message = f"Clicked at: {event.x}, {event.y}.\n"
    message += f"Screen coordinates: {event.x_root}, {event.y_root}.\n"
    message += f"Event type: {event.type.name}.\n"
    message += f"Clicked button: {button_name}.\n"
    message += f"Button text: {event.widget['text']}.\n"
    lbl.configure(text=message)

def on_enter(event):
    # event.widget["text"] = "Mouse entered"
    event.widget.configure(text="Mouse entered")

def on_leave(event):
    event.widget["text"] = "Mouse left"

def on_motion(event):
    win.title(f"{event.x}, {event.y}")

def on_combo_select(event):
    value = combo.get()
    lbl.configure(text=f"Selected: {value}")

win = tk.Tk()
win.geometry("400x250")
win.title("Week 5")

btn_a = ttk.Button(win, text="Button A")
btn_b = ttk.Button(win, text="Button B")
lbl = ttk.Label(win, justify="center")
combo = ttk.Combobox(win, values=["Option 1", "Option 2", "Option 3"], state="readonly")
combo.set("Select an option")

btn_a.pack(pady=(20, 0))
btn_b.pack(pady=(20, 0))
combo.pack(pady=20)
lbl.pack()

btn_a.bind("<Button-1>", on_click)
btn_b.bind("<Button-3>", on_click)
btn_a.bind("<Enter>", on_enter)
btn_a.bind("<Leave>", on_leave)
win.bind("<Motion>", on_motion)
combo.bind("<<ComboboxSelected>>", on_combo_select)

btn_a.focus_set()

win.mainloop()
