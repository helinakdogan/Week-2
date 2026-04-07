import tkinter as tk

win = tk.Tk()
win.geometry("300x300")
win.title("Week 3")

label1 = tk.Label(win, text="Label 1", bg="lightblue")
label2 = tk.Label(win, text="Label 2", bg="lightgreen")
label3 = tk.Label(win, text="Label 3", bg="lightpink")

# fill: Controls whether the widget should expand to fill the space allocated to it in the specified direction(s).
# expand: Controls whether the widget should be given extra space if the parent widget has any extra space available.
# anchor: Defines how the widget is positioned within its packing area (n, s, w, e, ne, ...).
label1.pack(ipadx=10, ipady=10, fill="y", expand=True)  # fill: none, x, y, both
label2.pack(ipadx=10, ipady=10, anchor="w")
label3.pack(ipadx=10, ipady=10, anchor="e")

win.mainloop()