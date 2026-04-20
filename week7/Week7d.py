# Install ttkbootstrap: https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/installation/
# Some common widgets

import ttkbootstrap as ttk
from ttkbootstrap import Style


class GUIApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("Week 7")
        self.resizable(width=False, height=False)
        self.cb_var = ttk.IntVar(value=1)
        self.rb_var = ttk.StringVar()
        self.current_appearance = ttk.StringVar(value="Dark")
        self.build_ui()
        self.entry1.bind("<KeyRelease>", self.on_key_release)
        self.on_theme_change()

    def build_ui(self):
        self.container = ttk.Labelframe(self, text="Common Widgets")
        self.lbl1 = ttk.Label(self.container, text="Label", bootstyle="primary")
        self.entry1 = ttk.Entry(self.container, bootstyle="primary", width=30)
        self.combo1 = ttk.Combobox(self.container, values=["Item 1", "Item 2", "Item 3"], bootstyle="primary", width=28)
        self.cb1 = ttk.Checkbutton(self.container, text="Checkbutton 1", onvalue=1, offvalue=0, variable=self.cb_var, bootstyle="primary")
        self.cb2 = ttk.Checkbutton(self.container, text="Checkbutton 2", onvalue=1, offvalue=0, bootstyle="round-toggle")
        self.rb1 = ttk.Radiobutton(self.container, text="Item 1", value="Item 1", variable=self.rb_var, bootstyle="info")
        self.rb2 = ttk.Radiobutton(self.container, text="Item 2", value="Item 2", variable=self.rb_var, bootstyle="info")
        self.btn1 = ttk.Button(self.container, text="Button", bootstyle="success-outline")
        self.pb1 = ttk.Progressbar(self.container, maximum=100, value=0, style="info-striped")
        self.sc1 = ttk.Scale(self.container, from_=0, to=100, style="primary", command=self.on_slider_change)
        self.cb3 = ttk.Checkbutton(self.container, variable=self.current_appearance, textvariable=self.current_appearance, onvalue="Light", offvalue="Dark", bootstyle="square-toggle", command=self.on_theme_change)

        pad = {"padx": 40, "pady": (25, 0)}
        self.container.pack(fill="both", expand=True, padx=20, pady=20)
        self.lbl1.pack(**pad)
        self.entry1.pack(**pad)
        self.combo1.pack(**pad)
        self.cb1.pack(**pad)
        self.cb2.pack(**pad)
        self.cb2.pack(**pad)
        self.rb1.pack(**pad)
        self.rb2.pack(**pad)
        self.btn1.pack(**pad)
        self.pb1.pack(**pad, fill="x")
        self.sc1.pack(**pad, fill="x")
        self.cb3.pack(padx=40, pady=25)

    def on_key_release(self, event):
        self.lbl1.configure(text=self.entry1.get())

    def on_slider_change(self, value):
        self.pb1.configure(value=value)
        self.lbl1.configure(text=f"Slider value: {float(value):.2f}")

    def on_theme_change(self):
        # Light theme: yeti  |  Dark theme: superhero
        new_theme = "yeti" if self.current_appearance.get() == "Light" else "superhero"
        Style().theme_use(new_theme)


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()