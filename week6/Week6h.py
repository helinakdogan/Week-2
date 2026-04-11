import tkinter as tk
from tkinter import ttk
import Week6i # Second window


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Week 6")
        self.build_ui()

    def build_ui(self):
        self.lbl1 = ttk.Label(self, text="Main Window", font=("Tahoma", 16))
        self.lbl2 = ttk.Label(self)
        self.btn1 = ttk.Button(self, text="Open Second Window", command=self.open_second_window)
        self.btn2 = ttk.Button(self, text="Close", command=self.destroy)

        self.lbl1.pack(pady=(20, 0))
        self.btn1.pack(pady=(20, 0))
        self.btn2.pack(pady=(20, 0))
        self.lbl2.pack(pady=(20, 0))

    def open_second_window(self):
        self.lbl2.config(text="")
        self.win2 = Week6i.SecondWindow(parent=self)
        self.win2.grab_set()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()