# Install ttkbootstrap: https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/installation/
# Basic ttkbootstrap GUI with classes

import ttkbootstrap as ttk


class GUIApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("Week 7")
        self.build_ui()

    def build_ui(self):
        self.frame1 = ttk.Frame(self)
        self.frame2 = ttk.Frame(self)

        self.btn1 = ttk.Button(self.frame1, text="Button 1", bootstyle="primary-outline")
        self.btn2 = ttk.Button(self.frame1, text="Button 2", bootstyle="secondary")
        self.btn3 = ttk.Button(self.frame1, text="Button 3", bootstyle="info")

        self.btn4 = ttk.Button(self.frame2, text="Button 4", bootstyle="danger")
        self.btn5 = ttk.Button(self.frame2, text="Button 5", bootstyle="success")
        self.btn6 = ttk.Button(self.frame2, text="Button 6", bootstyle="warning-outline")

        self.frame1.pack(pady=20)
        self.frame2.pack(pady=20)

        self.btn1.pack(padx=20, pady=20, side="left")
        self.btn2.pack(padx=20, pady=20, side="left")
        self.btn3.pack(padx=20, pady=20, side="left")

        self.btn4.pack(padx=20, pady=20, side="left")
        self.btn5.pack(padx=20, pady=20, side="left")
        self.btn6.pack(padx=20, pady=20, side="left")


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()