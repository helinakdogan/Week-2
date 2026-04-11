from BaseForm import BaseForm


class SaveForm(BaseForm):
    action_text = "Save"

    def on_submit(self):
        print("Save:", self.get_data())
