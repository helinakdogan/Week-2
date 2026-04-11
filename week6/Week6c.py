# Toplevel (show-hide main)

import tkinter as tk
from tkinter import ttk

win2 = None


def open_second_window():
    global win2

    win.withdraw() # Hide the main window
    win2 = tk.Toplevel(win)
    win2.geometry("300x200")
    win2.title("Second Window")
    ttk.Label(win2, text="Second Window").pack(pady=(20, 0))
    ttk.Button(win2, text="Close", command=close_second_window).pack(pady=(20, 0))
    win2.protocol("WM_DELETE_WINDOW", close_second_window)


def close_second_window():
    win.deiconify() # Show the main window again
    win2.destroy() # Close the second window


win = tk.Tk()
win.geometry("300x300")
win.title("Week 6")

btn1 = ttk.Button(win, text="Open Second Window", command=open_second_window)
btn2 = ttk.Button(win, text="Close", command=win.destroy)

btn1.pack(pady=(20, 0))
btn2.pack(pady=(20, 0))

win.mainloop()
