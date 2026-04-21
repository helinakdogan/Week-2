import ttkbootstrap as ttk
from ttkbootstrap import Style

class GUIApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")   # temalı pencere
        self.title("Week 7")
        self.geometry("420x420")
        self.resizable(False, False)

        # widgetlarla bağlı değişkenler
        self.name_var = ttk.StringVar()
        self.appearance_var = ttk.StringVar(value="Light")

        self.build_ui()

        # event
        self.entry_name.bind("<KeyRelease>", self.on_key_release)

    def build_ui(self):
        # ana container
        self.frame = ttk.Frame(self, padding=20)
        self.frame.pack(fill="both", expand=True)

        # başlık
        self.lbl_title = ttk.Label(self.frame, text="Week 7 Form", bootstyle="primary")
        self.lbl_title.pack(pady=(0, 15))

        # entry
        self.entry_name = ttk.Entry(self.frame, textvariable=self.name_var, width=30)
        self.entry_name.pack(pady=8)

        # combobox
        self.combo_course = ttk.Combobox(
            self.frame,
            values=["Python", "Java", "C++"],
            width=27,
            state="readonly",
            bootstyle="info"
        )
        self.combo_course.set("Python")
        self.combo_course.pack(pady=8)

        # checkbutton
        self.check_updates = ttk.Checkbutton(
            self.frame,
            text="Receive updates",
            bootstyle="success-round-toggle"
        )
        self.check_updates.pack(pady=8)

        # progressbar
        self.progress = ttk.Progressbar(
            self.frame,
            maximum=100,
            value=0,
            bootstyle="warning-striped"
        )
        self.progress.pack(fill="x", pady=8)

        # slider / scale
        self.slider = ttk.Scale(
            self.frame,
            from_=0,
            to=100,
            command=self.on_slider_change,
            bootstyle="warning"
        )
        self.slider.pack(fill="x", pady=8)

        # theme switch mantığı için checkbutton
        self.switch_theme = ttk.Checkbutton(
            self.frame,
            textvariable=self.appearance_var,
            variable=self.appearance_var,
            onvalue="Dark",
            offvalue="Light",
            bootstyle="dark-square-toggle",
            command=self.on_theme_change
        )
        self.switch_theme.pack(pady=12)

        # sonuç label
        self.lbl_result = ttk.Label(self.frame, text="Type your name...")
        self.lbl_result.pack(pady=10)

        # buton
        self.btn_show = ttk.Button(
            self.frame,
            text="Show Info",
            bootstyle="primary-outline",
            command=self.on_button_click
        )
        self.btn_show.pack(pady=8)

    def on_key_release(self, event):
        # entry'ye yazdıkça label güncellenir
        self.lbl_result.configure(text=f"Hello, {self.entry_name.get()}")

    def on_slider_change(self, value):
        # slider değeri progressbar'a aktarılır
        self.progress.configure(value=float(value))

    def on_theme_change(self):
        # checkbutton durumuna göre tema değişir
        new_theme = "superhero" if self.appearance_var.get() == "Dark" else "litera"
        Style().theme_use(new_theme)

    def on_button_click(self):
        # entry + combobox bilgisini label'da göster
        self.lbl_result.configure(
            text=f"Name: {self.entry_name.get()} | Course: {self.combo_course.get()}"
        )

if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()