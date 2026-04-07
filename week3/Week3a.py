import tkinter as tk

win = tk.Tk()
win.geometry("300x300")
win.title("Week 3")

label1 = tk.Label(win, text="Label 1", bg="lightblue")
label2 = tk.Label(win, text="Label 2", bg="lightgreen")
label3 = tk.Label(win, text="Label 3", bg="lightpink")

# Absolute placement (values are in pixels)
label1.place(x=30, y=30, width=100, height=40)
label2.place(x=150, y=180, width=120, height=40)
label3.place(x=20, y=220, width=80, height=60)

# Relative placement (values are proportional to the parent widget's size, between 0.0 and 1.0)
# anchor: Defines which part of the widget will be positioned at (x, y) or (relx, rely).
label4 = tk.Label(win, text="Relative Label", bg="yellow")
label4.place(
    relx=0.5,        # 50% across the window
    rely=0.5,        # 50% down the window
    relwidth=0.3,    # 30% of the window's width
    relheight=0.1,   # 10% of the window's height
    anchor="center"  # position label's center at the relx/rely point
)

win.mainloop()
