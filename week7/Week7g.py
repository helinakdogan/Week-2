# Install customtkinter: https://customtkinter.tomschimansky.com/
# Textbox, segmented button, and tab view widgets

import customtkinter as ctk


class GUIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Week 7")
        self.sbtn1_value = ctk.StringVar(value="Option 3") # Default button selection
        self.build_ui()

    def build_ui(self):
        self.container = ctk.CTkFrame(self)
        self.textbox1 = ctk.CTkTextbox(self.container, wrap="none", width=240, height=80)
        self.sbtn1 = ctk.CTkSegmentedButton(self.container, values=["Option 1", "Option 2", "Option 3"],
                                            variable=self.sbtn1_value, command=self.on_select)
        self.tabview1 = ctk.CTkTabview(self.container, anchor="sw")  # "anchor" sets the placement of the tab buttons
        self.tab1 = self.tabview1.add("Tab 1")
        self.tab2 = self.tabview1.add("Tab 2")
        self.lbl1 = ctk.CTkLabel(self.tab1, text="This is tab 1.")
        self.lbl2 = ctk.CTkLabel(self.tab2, text="This is tab 2.")
        self.btn1 = ctk.CTkButton(self.tab2, text="Exit", command=self.destroy)

        self.container.pack(pady=20, padx=20, fill="both", expand=True)
        self.textbox1.pack(pady=(10, 0))
        self.sbtn1.pack(pady=(10, 0))
        self.tabview1.pack(padx=10, pady=10)
        self.lbl1.pack(pady=(30, 0))
        self.lbl2.pack(pady=(30, 0))
        self.btn1.pack(pady=(30, 0))

        # Default tab selection
        self.tabview1.set("Tab 2")

    def on_select(self, value):
        self.textbox1.insert("end", f"{value} selected.\n") # self.sbtn1_value.get()
        self.textbox1.see("end") # "1.0" - Line 1, column 0 (first line, first character)


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()