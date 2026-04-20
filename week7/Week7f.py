# Install customtkinter: https://customtkinter.tomschimansky.com/
# Some common widgets

import customtkinter as ctk
from tkinter import messagebox

class GUIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Week 7")
        self.resizable(width=False, height=False)
        self.rb_value = ctk.IntVar(value=1)
        self.current_appearance = ctk.StringVar(value="Dark")
        self.build_ui()
        self.entry1.bind("<KeyRelease>", self.on_key_release)
        self.on_theme_change()

    def build_ui(self):
        self.container = ctk.CTkFrame(self)
        self.lbl1 = ctk.CTkLabel(self.container, text="Label")
        self.entry1 = ctk.CTkEntry(self.container, placeholder_text="Type your message.")
        self.combo1 = ctk.CTkComboBox(self.container, values=["Item 1", "Item 2", "Item 3"])
        self.opt_menu1 = ctk.CTkOptionMenu(self.container, values=["Item 1", "Item 2", "Item 3"])
        self.chk1 = ctk.CTkCheckBox(self.container, text="Checkbox", onvalue="checked", offvalue="unchecked")
        self.radio1 = ctk.CTkRadioButton(self.container, text="Item 1", variable=self.rb_value, value=1)
        self.radio2 = ctk.CTkRadioButton(self.container, text="Item 2", variable=self.rb_value, value=2)
        self.btn1 = ctk.CTkButton(self.container, text="Button", command=self.on_button_click)
        self.progress1 = ctk.CTkProgressBar(self.container)
        self.slider1 = ctk.CTkSlider(self.container, from_=0, to=1, command=self.on_slider_change)
        self.switch1 = ctk.CTkSwitch(self.container, variable=self.current_appearance, textvariable=self.current_appearance, onvalue="Light", offvalue="Dark", command=self.on_theme_change)

        pad = {"padx": 15, "pady": (10, 0)}
        self.container.pack(fill="both", expand=True, padx=20, pady=20)
        self.lbl1.pack(**pad)
        self.entry1.pack(**pad)
        self.combo1.pack(**pad)
        self.opt_menu1.pack(**pad)
        self.chk1.pack(**pad)
        self.radio1.pack(**pad)
        self.radio2.pack(**pad)
        self.btn1.pack(**pad)
        self.progress1.pack(**pad)
        self.slider1.pack(**pad)
        self.switch1.pack(padx=10, pady=10)

        # Set initial states
        self.progress1.set(0.8)
        self.slider1.set(0.8)

    def on_key_release(self, event):
        self.lbl1.configure(text=self.entry1.get())

    def on_button_click(self):
        msg = (f"Combobox value is {self.combo1.get()}.\n"
               f"Option menu value is {self.opt_menu1.get()}.\n"
               f"Checkbox is {self.chk1.get()}.\n"
               f"Radio button value is {self.rb_value.get()}.")
        messagebox.showinfo("Widget Values", msg)

    def on_slider_change(self, value):
        self.progress1.set(value)
        self.lbl1.configure(text=f"Slider value: {value:.2f}")

    def on_theme_change(self):
        new_theme = self.current_appearance.get()
        ctk.set_appearance_mode(new_theme)


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()