# Event binding I (Mouse click)

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

win = tk.Tk()
win.geometry("400x250")
win.title("Week 5")

btn_a = ttk.Button(win, text="Button A")
btn_b = ttk.Button(win, text="Button B")
lbl = ttk.Label(win, justify="center")

btn_a.pack(pady=(20, 0))
btn_b.pack(pady=20)
lbl.pack()

# Button, Button-1, Button-2, Button-3, Double-Button, Double-Button-1, ButtonRelease, ButtonRelease-1, ...

btn_a.bind("<Button>", on_click)
btn_b.bind("<ButtonRelease-3>", on_click)

btn_a.focus_set()

win.mainloop()
