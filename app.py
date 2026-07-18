"""
GUI callbacks:
    *_pressed() -> GUI -> Calculator

Calculator methods:
    press_*() -> Calculator logic
"""

import tkinter as tk
from modules.calculator import Calculator

class CalculatorApp:

    def __init__(self):
        self.configure_window()
        self.calculator = Calculator()
        self.create_display()
        self.create_buttons()
        self.last_size = None
        self.root.bind("<Key>", self.key_pressed)
        self.root.bind("<Configure>", self.update_fonts)
        self.update_display()

    def run(self):
        self.root.mainloop()

    def configure_window(self):
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        self.root.iconbitmap("assets/icon.ico")
        self.root.geometry("315x300")
        self.root.minsize(315, 300)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

    def create_display(self):

        display_frame = tk.Frame(self.root)
        display_frame.grid(row=0, column=0, sticky="ew")
        display_frame.grid_columnconfigure(0, weight=1)

        self.expression_label = tk.Label(
            display_frame,
            text=self.calculator.expression,
            font=("Segoe UI", 14),
            anchor="e",
            justify="right"
        )
        self.expression_label.grid(row=0, column=0, pady=5, sticky="ew", padx=5)

        self.display_text = tk.StringVar()
        self.display_entry = tk.Entry(
            display_frame,
            textvariable=self.display_text,
            justify="right",
            font=("Segoe UI", 20)
        )
        self.display_entry.grid(row=1, column=0, pady=5, sticky="ew", padx=5)
        self.display_text.set(self.calculator.display)

    def update_fonts(self, event=None):
        if event and event.widget is not self.root:
            return

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        if self.last_size == (width, height):
            return
        self.last_size = (width, height)

        # smaller dimension to keep scaling balanced
        scale = min(width, height)

        button_size = max(12, min(28, scale // 18))
        expression_size = max(14, min(28, scale // 25))
        display_size = max(20, min(42, scale // 16))

        self.display_entry.config(font=("Segoe UI", display_size))
        self.expression_label.config(font=("Segoe UI", expression_size))

        for button in self.button_widgets:
            button.config(font=("Segoe UI", button_size))

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.grid(row=1, column=0, sticky="nsew")

        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)

        BUTTON_CONFIG = [
            {"text": "AC", "type": "clear", "mode": "all", "keys": ["Escape"], "row": 0, "column": 0},
            {"text": "CE", "type": "clear", "mode": "entry", "keys": ["grave"], "row": 0, "column": 1},
            {"text": "⌫", "type": "clear", "mode": "backspace", "keys": ["BackSpace"], "row": 0, "column": 2},
            {"text": "÷", "type": "operator", "keys": ["slash"], "row": 0, "column": 3},
            {"text": "7", "type": "digit", "keys": ["7"], "row": 1, "column": 0},
            {"text": "8", "type": "digit", "keys": ["8"], "row": 1, "column": 1},
            {"text": "9", "type": "digit", "keys": ["9"], "row": 1, "column": 2},
            {"text": "×", "type": "operator", "keys": ["asterisk"], "row": 1, "column": 3},
            {"text": "4", "type": "digit", "keys": ["4"], "row": 2, "column": 0},
            {"text": "5", "type": "digit", "keys": ["5"], "row": 2, "column": 1},
            {"text": "6", "type": "digit", "keys": ["6"], "row": 2, "column": 2},
            {"text": "-", "type": "operator", "keys": ["minus"], "row": 2, "column": 3},
            {"text": "1", "type": "digit", "keys": ["1"],"row": 3, "column": 0},
            {"text": "2", "type": "digit", "keys": ["2"], "row": 3, "column": 1},
            {"text": "3", "type": "digit", "keys": ["3"], "row": 3, "column": 2},
            {"text": "+", "type": "operator", "keys": ["plus"],  "row": 3, "column": 3},
            {"text": "%", "type": "percent", "keys": ["percent"], "row": 4, "column": 0,},
            {"text": "0", "type": "digit", "keys": ["0"], "row": 4, "column": 1,},
            {"text": ".", "type": "digit", "keys": ["period"], "row": 4, "column": 2},
            {"text": "=", "type": "equal", "keys": ["Return", "equal"], "row": 4, "column": 3},
        ]

        self.button_widgets = []
        self.key_commands = {}

        for config in BUTTON_CONFIG:
            button_type = config["type"]
            button_text = config["text"]
            if button_type == "digit":
                command = lambda text=button_text: self.digit_pressed(text)
            elif button_type == "operator":
                command = lambda text=button_text: self.operator_pressed(text)
            elif button_type == "clear":
                match config["mode"]:
                    case "all":
                        command = self.clear_pressed
                    case "entry":
                        command = self.clear_entry_pressed
                    case "backspace":
                        command = self.backspace_pressed
            elif button_type == "equal":
                command = self.equal_pressed
            elif button_type == "percent":
                command = self.percent_pressed
            for key in config["keys"]:
                self.key_commands[key] = command
            button = tk.Button(
                buttons_frame,
                text=button_text,
                font=("Segoe UI", 12),
                command=command
            )
            button.grid(
                row=config["row"],
                column=config["column"],
                columnspan=config.get("columnspan", 1),
                sticky="nsew",
                padx=2,
                pady=2
            )
            self.button_widgets.append(button)

    def update_display(self):
        self.display_text.set(self.calculator.display)
        self.expression_label.config(text=self.calculator.expression)

    def handle_error(self, error):
        self.calculator.display = str(error)
        self.calculator.error_state = True
        self.calculator.expression = ""
        self.update_display()

    def digit_pressed(self, digit):
        self.calculator.press_digit(digit)
        self.update_display()

    def operator_pressed(self, operator):
        try:
            self.calculator.press_operator(operator)
            self.update_display()
        except ZeroDivisionError as error:
                self.handle_error(error)

    def percent_pressed(self):
        self.calculator.press_percent()
        self.update_display()

    def clear_pressed(self):
        self.calculator.press_clear()
        self.update_display()

    def clear_entry_pressed(self):
        self.calculator.press_clear_entry()
        self.update_display()

    def backspace_pressed(self):
        self.calculator.press_backspace()
        self.update_display()

    def equal_pressed(self):
        try:
            self.calculator.press_equal()
            self.update_display()
        except ZeroDivisionError as error:
            self.handle_error(error)

    def key_pressed(self, event):
        command = self.key_commands.get(event.keysym)
        if command:
            command()
