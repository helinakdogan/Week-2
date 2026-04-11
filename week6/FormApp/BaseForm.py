import tkinter as tk
from tkinter import ttk


class BaseForm(tk.Toplevel):
    # Text on the main action button (override in subclasses)
    action_text = "Submit"

    def __init__(self, parent, title):
        super().__init__(parent)
        self.resizable(width=False, height=False)
        self.title(title)

        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()

        self.build_ui()
        self.entry1.focus_set()

        self.protocol("WM_DELETE_WINDOW", self.on_cancel)

    def build_ui(self):
        pad = {"padx": 12, "pady": 6}

        frm = ttk.Frame(self)
        frm.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)

        ttk.Label(frm, text="Field 1:").grid(row=0, column=0, sticky="w", **pad)
        self.entry1 = ttk.Entry(frm, textvariable=self.var1, width=30)
        self.entry1.grid(row=0, column=1, sticky="ew", **pad)

        ttk.Label(frm, text="Field 2:").grid(row=1, column=0, sticky="w", **pad)
        self.entry2 = ttk.Entry(frm, textvariable=self.var2, width=30)
        self.entry2.grid(row=1, column=1, sticky="ew", **pad)

        ttk.Label(frm, text="Field 3:").grid(row=2, column=0, sticky="w", **pad)
        self.entry3 = ttk.Entry(frm, textvariable=self.var3, width=30)
        self.entry3.grid(row=2, column=1, sticky="ew", **pad)

        btns = ttk.Frame(frm)
        btns.grid(row=3, column=0, columnspan=2, sticky="e", **pad)

        self.btn_action = ttk.Button(btns, text=self.action_text, command=self.on_submit)
        self.btn_action.pack(side="left")

        self.btn_cancel = ttk.Button(btns, text="Cancel", command=self.on_cancel)
        self.btn_cancel.pack(side="left")

    def get_data(self):
        return {
            "field1": self.var1.get().strip(),
            "field2": self.var2.get().strip(),
            "field3": self.var3.get().strip(),
        }

    def on_submit(self):
        raise NotImplementedError("Missing method implementation.")

    def on_cancel(self):
        self.destroy()
