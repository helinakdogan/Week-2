import tkinter as tk

win = tk.Tk()
win.geometry("300x300")
win.title("Week 3")

label1 = tk.Label(win, text="Label 1", bg="lightblue")
label2 = tk.Label(win, text="Label 2", bg="lightgreen")
label3 = tk.Label(win, text="Label 3", bg="lightpink")
label4 = tk.Label(win, text="Label 3", bg="lightgray")

# side: Defines the side of the container where the widget is placed (top, left, right, bottom)
label1.pack(ipadx=10, ipady=10, fill="x", side="top")
label2.pack(ipadx=10, ipady=10, fill="y", side="left")
label3.pack(ipadx=10, ipady=10, fill="y", side="right")
label4.pack(ipadx=10, ipady=10, fill="x", side="bottom") # Pack order matters. Pack after label1 to see the difference.


win.mainloop()