import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def button_handler():
    win.destroy()

win = tk.Tk()
win.geometry("300x340")
win.title("Week 3")

notebook1 = ttk.Notebook(win)
notebook1.pack(fill="both", expand=True)

tab1 = ttk.Frame(notebook1)
tab2 = ttk.Frame(notebook1)

notebook1.add(tab1, text="Editor")
notebook1.add(tab2, text="About")

# wrap: none, char, word
scrolled_text1 = ScrolledText(tab1, width=30, height=10, wrap="word", undo=True, font=("Consolas", 10))
scrolled_text1.pack(fill="both", expand=True, padx=5, pady=5)
scrolled_text1.focus_set()

label1 = ttk.Label(tab2, text="A simple text editor.")
button1 = ttk.Button(tab2, text="Exit", command=button_handler)

label1.pack(pady=(50, 10))
button1.pack(pady=10)

win.mainloop()