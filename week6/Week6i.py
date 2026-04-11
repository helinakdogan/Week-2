import tkinter as tk
from tkinter import ttk


class SecondWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("300x200")
        self.title("Second Window")
        self.build_ui()
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.entry1.bind("<Return>", self.on_return)

    def build_ui(self):
        self.lbl1 = ttk.Label(self, text="Second Window", font=("Tahoma", 16))
        self.lbl2 = ttk.Label(self, text="Enter your message and press <Return>.")
        self.entry1 = ttk.Entry(self)
        self.btn1 = ttk.Button(self, text="Close", command=self.close_window)

        self.lbl1.pack(pady=(20, 0))
        self.lbl2.pack(pady=(20, 0))
        self.entry1.pack(pady=(20, 0))
        self.btn1.pack(pady=(20, 0))

        self.entry1.focus_set()

    def on_return(self, event):
        # Update the label text in the parent (if entry1 has text).
        if self.entry1.get():
            self.parent.lbl2.configure(text=f"Message from the second window: {self.entry1.get()}")
            self.close_window()

    def close_window(self):
        self.destroy()
