from BaseForm import BaseForm
from tkinter import ttk


class EditForm(BaseForm):
    action_text = "Update"

    def build_ui(self):
        super().build_ui()

        # Get the reference for the button container frame
        btns = self.btn_action.master

        btn_delete = ttk.Button(btns, text="Delete", command=self.on_delete)
        btn_delete.pack(side="left") # before=self.btn_cancel
        #self.btn_cancel.pack_forget()
        #self.btn_cancel.pack(side="left")

        # Cancel button is destroyed and re-created to maintain correct keyboard focus order.
        # Alternatively, you can bind <Tab> key to tell which widget gains next focus using widget.focus_set()
        self.btn_cancel.destroy()
        self.btn_cancel = ttk.Button(btns, text="Cancel", command=self.on_cancel)
        self.btn_cancel.pack(side="left")

    def on_submit(self):
        print("Update:", self.get_data())

    def on_delete(self):
        print("Delete:", self.get_data())
