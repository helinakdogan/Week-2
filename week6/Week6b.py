# Toplevel (single instance only)

import tkinter as tk
from tkinter import ttk

win2 = None


def open_second_window():
    global win2

    if win2 is not None and win2.winfo_exists():
        win2.lift()
        win2.focus_set()
        return

    win2 = tk.Toplevel(win)
    win2.geometry("300x200")
    win2.title("Second Window")
    # win2.grab_set()  # Restricts all user interactions to this window only (modal window).
    ttk.Label(win2, text="Second Window").pack(pady=(20, 0))
    ttk.Button(win2, text="Close", command=win2.destroy).pack(pady=(20, 0))


win = tk.Tk()
win.geometry("300x300")
win.title("Week 6")

btn1 = ttk.Button(win, text="Open Second Window", command=open_second_window)
btn2 = ttk.Button(win, text="Close", command=win.destroy)

btn1.pack(pady=(20, 0))
btn2.pack(pady=(20, 0))

win.mainloop()
