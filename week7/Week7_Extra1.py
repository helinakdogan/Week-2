# Install ttkbootstrap: https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/installation/
# Scrollable frame (ttkbootstrap)

import ttkbootstrap as ttk
from ttkbootstrap.widgets.scrolled import ScrolledFrame


class GUIApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("Week 7")
        self.labels = []
        self.build_ui()

    def build_ui(self):
        self.frm_main = ttk.Frame(self)
        self.lbl_title = ttk.Label(self.frm_main, text="List of Labels", font=("Arial", 12, "bold"))
        self.frm_scrollable = ScrolledFrame(self.frm_main, autohide=True, width=500, height=500)
        self.btn_add = ttk.Button(self.frm_scrollable, text="Add labels", command=self.on_add, bootstyle="primary")
        self.btn_remove = ttk.Button(self.frm_scrollable, text="Remove labels", command=self.on_remove, bootstyle="secondary")

        self.frm_main.pack(pady=20, padx=20, fill="both", expand=True)
        self.lbl_title.pack(pady=(0, 10))
        self.frm_scrollable.pack(fill="both", expand=True)
        self.btn_add.pack(pady=(10, 0))
        self.btn_remove.pack(pady=(10, 0))

    def on_add(self):
        list_size = len(self.labels)
        for i in range(20):
            lbl = ttk.Label(self.frm_scrollable, text=f"Label {list_size + i + 1}")
            lbl.pack(pady=(10, 0))
            self.labels.append(lbl)

        self.lbl_title.configure(text=f"List of Labels ({len(self.labels)})")

    def on_remove(self):
        for lbl in self.labels:
            lbl.destroy()

        self.labels.clear()
        self.lbl_title.configure(text="List of Labels")


if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()