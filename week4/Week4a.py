# Simple menu

import tkinter as tk

win = tk.Tk()
win.geometry("300x200")
win.title("Week 4")

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Exit", command=win.destroy)

# underline: specifies the character index that will be underlined
# for keyboard shortcut (press <Alt> for Windows)
menubar.add_cascade(label="File", menu=file_menu, underline=0)

win.mainloop()
