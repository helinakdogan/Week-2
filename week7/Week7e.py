# Install customtkinter: https://customtkinter.tomschimansky.com/
# Basic CTk GUI with classes

import customtkinter as ctk


class GUIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Week 7")
        self.build_ui()

    def build_ui(self):
        self.lbl = ctk.CTkLabel(self, text="GUI Programming with Python", fg_color=("orange", "green"), corner_radius=20)
        self.btn = ctk.CTkButton(self, text="Change Appearance", command=self.on_theme_change)

        self.lbl.pack(pady=20)
        self.btn.pack()

    def on_theme_change(self):
        new_theme = "Light" if ctk.get_appearance_mode() == "Dark" else "Dark"
        ctk.set_appearance_mode(new_theme)


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()