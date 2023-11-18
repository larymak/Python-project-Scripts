import json_parser
from tkinter import *


class JSONValidator:
    def __init__(self, master):
        self.master = master
        master.title("JSON Validator")

        # Input, Button and Label - Init and Placement

        # JSON Text Box
        self.text_input = Text(master, height=10, width=40)
        self.text_input.pack(pady=20)
        self.text_input.tag_configure("center", justify="center")
        self.text_input.insert("1.0", "Input your JSON here")
        self.text_input.tag_add("center", "1.0", "end")

        # Validate Button
        self.validate_button = Button(
            master, text="Validate", command=self.validate_input
        )
        self.validate_button.pack()

        # Clear Button
        self.clear_button = Button(master, text="Clear", command=self.clear_input)
        self.clear_button.pack(pady=15)

        # Result Label
        self.info_label = Label(master, text=" ")
        self.info_label.pack(side=TOP, pady=25)

        # Window sizing and placement
        master.update_idletasks()

        x = (master.winfo_screenwidth() - (master.winfo_reqwidth() + 100)) // 2
        y = (master.winfo_screenheight() - (master.winfo_reqheight() + 10)) // 2

        master.geometry(
            f"{master.winfo_reqwidth() + 100}x{master.winfo_reqheight() + 10}+{x}+{y}"
        )
        master.resizable(False, False)

        master.mainloop()

    def validate_input(self):
        input_text = self.text_input.get("1.0", "end-1c")

        validator = json_parser.JSONParser(input_text)
        result = validator.parse()

        if not result:
            self.info_label.configure(text="JSON is Valid")
        else:
            self.info_label.configure(text="JSON is Invalid")

    def clear_input(self):
        self.text_input.delete("1.0", END)
        self.info_label.configure(text="")


if __name__ == "__main__":
    root = Tk()
    validator = JSONValidator(root)
