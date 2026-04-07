import tkinter as tk

win = tk.Tk()
win.geometry("300x300")
win.title("Week 3")

# uniform: Columns/rows with the same non-empty uniform tag form a group.
# Space for that group is allocated so their sizes stay in strict proportion to their weight values.
win.columnconfigure(index=0, weight=1, uniform="eq")
win.columnconfigure(index=1, weight=2, uniform="eq")
win.columnconfigure(index=2, weight=3, uniform="eq")
win.rowconfigure(index=0, weight=1, uniform="eq")
win.rowconfigure(index=1, weight=1, uniform="eq")
win.rowconfigure(index=2, weight=1, uniform="eq")

label1 = tk.Label(win, text="Label 1", bg="lightblue")
label2 = tk.Label(win, text="This is a very very long label.", bg="lightgreen")
label3 = tk.Label(win, text="Label 3", bg="lightpink")

# sticky: Controls widget alignment or stretching within the grid cell.
# rowspan / columnspan: Allows a widget to span multiple rows or columns.
label1.grid(row=0, column=0, sticky="nswe") # rowspan=2
label2.grid(row=1, column=2, sticky="nswe")
label3.grid(row=2, column=1, sticky="nswe") # columnspan=2

win.mainloop()