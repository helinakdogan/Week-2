import tkinter as tk

win = tk.Tk()
win.geometry("300x300")
win.title("Week 3")

label1 = tk.Label(win, text="Label 1", bg="lightblue")
label2 = tk.Label(win, text="Label 2", bg="lightgreen")
label3 = tk.Label(win, text="Label 3", bg="lightpink")

# Static grid (not responsive).
label1.grid(row=0, column=0)
label2.grid(row=1, column=2)
label3.grid(row=2, column=1)

win.mainloop()