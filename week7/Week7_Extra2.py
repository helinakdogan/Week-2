# Install customtkinter: https://customtkinter.tomschimansky.com/
# Scrollable frame (customtkinter)

import customtkinter as ctk


class GUIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Week 7")
        self.labels = []
        self.build_ui()

    def build_ui(self):
        self.frm_scrollable = ctk.CTkScrollableFrame(self, label_text="List of Labels")
        self.btn_add = ctk.CTkButton(self.frm_scrollable, text="Add labels", command=self.on_add)
        self.btn_remove = ctk.CTkButton(self.frm_scrollable, text="Remove labels", command=self.on_remove)

        self.frm_scrollable.pack(pady=20, padx=20, fill="both", expand=True)
        self.btn_add.pack(pady=(10, 0))
        self.btn_remove.pack(pady=(10, 0))

    def on_add(self):
        list_size = len(self.labels)
        for i in range(20):
            lbl = ctk.CTkLabel(self.frm_scrollable, text=f"Label {list_size + i + 1}")
            lbl.pack(pady=(10, 0))
            self.labels.append(lbl)

        self.frm_scrollable.configure(label_text=f"List of Labels ({len(self.labels)})")

    def on_remove(self):
        for lbl in self.labels:
            lbl.destroy()

        self.labels.clear()
        self.frm_scrollable.configure(label_text="List of Labels")


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()
