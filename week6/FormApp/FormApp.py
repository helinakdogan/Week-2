import tkinter as tk
from tkinter import ttk
from SaveForm import SaveForm
from EditForm import EditForm


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x160")
        self.title("Week 6 - Form App")
        self.build_ui()

    def build_ui(self):
        container = ttk.Frame(self, padding=12)
        container.pack(fill="both", expand=True)

        ttk.Label(container, text="Choose a form to open:").pack(anchor="w", pady=(0, 8))
        ttk.Button(container, text="Open Save Form", command=self.open_save).pack(fill="x", pady=(0, 6))
        ttk.Button(container, text="Open Edit Form", command=self.open_edit).pack(fill="x")
        ttk.Separator(container).pack(fill="x", pady=12)
        ttk.Button(container, text="Quit", command=self.destroy).pack(fill="x")

    def open_save(self):
        save_form = SaveForm(parent=self, title="Save Form")
        save_form.grab_set()

    def open_edit(self):
        edit_form = EditForm(parent=self, title="Edit Form")
        edit_form.grab_set()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()