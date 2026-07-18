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
        self.calc = Calculator()
        self.create_display()
        self.create_buttons()
        self.root.bind("<Key>", self.key_pressed)
        self.update_display()

    def run(self):
        self.root.mainloop()

    def configure_window(self):
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        self.root.iconbitmap("assets/icon.ico")
        self.root.geometry("420x350")
        self.root.resizable(False, False)

    def create_display(self):
        display_frame = tk.Frame(self.root)
        display_frame.pack(padx=20)

        self.expression_label = tk.Label(display_frame, text=self.calc.expression, anchor="e", justify="right",)
        self.expression_label.grid(row=0, column=1, pady=5, sticky="ew")

        self.display_text = tk.StringVar()
        display_entry = tk.Entry(
            display_frame,
            textvariable=self.display_text,
            width=25,
            justify="right",
            font=("Segoe UI", 16)
        )
        display_entry.grid(row=1, column=1, pady=5)
        self.display_text.set(self.calc.display)

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)

        buttons = [
            {"text": "AC", "type": "clear", "mode": "all", "keys": ["Escape"], "row": 0, "column": 0},
            {"text": "CE", "type": "clear", "mode": "entry", "keys": ["grave"], "row": 0, "column": 1},
            {"text": "⌫", "type": "backspace", "keys": ["BackSpace"], "row": 0, "column": 2},
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
            {"text": "0", "type": "digit", "keys": ["0"], "row": 4, "column": 0, "width": 18, "columnspan": 2},
            {"text": ".", "type": "digit", "keys": ["period"], "row": 4, "column": 2},
            {"text": "=", "type": "equal", "keys": ["Return", "equal"], "row": 4, "column": 3},
        ]

        self.key_commands = {}

        for button in buttons:
            button_type = button["type"]
            button_text = button["text"]
            if button_type == "digit":
                command = lambda text=button_text: self.digit_pressed(text)
            elif button_type == "operator":
                command = lambda text=button_text: self.operator_pressed(text)
            elif button_type == "clear":
                if button["mode"] == "all":
                    command = self.clear_pressed
                else:
                    command = self.clear_entry_pressed
            elif button_type == "backspace":
                command = self.backspace_pressed
            elif button_type == "equal":
                command = self.equal_pressed
            for key in button["keys"]:
                self.key_commands[key] = command
            tk.Button(buttons_frame, text=button_text, width=button.get("width", 8), height=2, command=command).grid(row=button["row"], column=button["column"], columnspan=button.get("columnspan", 1))

    def update_display(self):
        self.display_text.set(self.calc.display)
        self.expression_label.config(text=self.calc.expression)

    def handle_error(self, error):
        self.calc.display = str(error)
        self.calc.error_state = True
        self.calc.expression = ""
        self.update_display()

    def digit_pressed(self, digit):
        self.calc.press_digit(digit)
        self.update_display()

    def operator_pressed(self, operator):
        try:
            self.calc.press_operator(operator)
            self.update_display()
        except ZeroDivisionError as error:
                self.handle_error(error)

    def clear_pressed(self):
        self.calc.press_clear()
        self.update_display()

    def clear_entry_pressed(self):
        self.calc.press_clear_entry()
        self.update_display()

    def backspace_pressed(self):
        self.calc.press_backspace()
        self.update_display()

    def equal_pressed(self):
        try:
            self.calc.press_equal()
            self.update_display()
        except ZeroDivisionError as error:
            self.handle_error(error)

    def key_pressed(self, event):
        command = self.key_commands.get(event.keysym)
        if command:
            command()
