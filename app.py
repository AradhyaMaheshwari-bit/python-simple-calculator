"""
GUI callbacks:
    *_pressed() -> GUI -> Calculator

Calculator methods:
    press_*() -> Calculator logic
"""

import tkinter as tk
from modules.calculator import Calculator

def create_app():

    root = tk.Tk()
    root.title("Simple Calculator")
    root.iconbitmap("assets/icon.ico")
    root.geometry("420x350")
    root.resizable(False, False)
    calc = Calculator()

    # ============
    # Display area
    # ============

    display_frame = tk.Frame(root)
    display_frame.pack(padx=20)

    def update_display():
        display_text.set(calc.display)
        expression_label.config(text=calc.expression)

    def handle_error(error):
        calc.display = str(error)
        calc.error_state = True
        calc.expression = ""
        update_display()

    expression_label = tk.Label(display_frame, text=calc.expression, anchor="e", justify="right",)
    expression_label.grid(row=0, column=1, pady=5, sticky="ew")

    display_text = tk.StringVar()
    display_entry = tk.Entry(
        display_frame,
        textvariable=display_text,
        width=25,
        justify="right",
        font=("Segoe UI", 16)
    )
    display_entry.grid(row=1, column=1, pady=5)
    display_text.set(calc.display)

    # ==============
    # Buttons area
    # ==============

    buttons_frame = tk.Frame(root)
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

    def digit_pressed(digit):
        calc.press_digit(digit)
        update_display()

    def clear_pressed():
        calc.press_clear()
        update_display()

    def clear_entry_pressed():
        calc.press_clear_entry()
        update_display()

    def backspace_pressed():
        calc.press_backspace()
        update_display()

    def operator_pressed(operator):
        try:
            calc.press_operator(operator)
            update_display()
        except ZeroDivisionError as error:
            handle_error(error)

    def equal_pressed():
        try:
            calc.press_equal()
            update_display()
        except ZeroDivisionError as error:
            handle_error(error)

    key_commands = {}

    for button in buttons:
        button_type = button["type"]
        button_text = button["text"]
        if button_type == "digit":
            command = lambda text=button_text: digit_pressed(text)
        elif button_type == "operator":
            command = lambda text=button_text: operator_pressed(text)
        elif button_type == "clear":
            if button["mode"] == "all":
                command = clear_pressed
            else:
                command = clear_entry_pressed
        elif button_type == "backspace":
            command = backspace_pressed
        elif button_type == "equal":
            command = equal_pressed
        for key in button["keys"]:
            key_commands[key] = command
        tk.Button(buttons_frame, text=button_text, width=button.get("width", 8), height= 2, command=command).grid(row=button["row"], column=button["column"], columnspan = button.get("columnspan", 1))

    def key_pressed(event):
        command = key_commands.get(event.keysym)
        if command:
            command()

    root.bind("<Key>", key_pressed)

    return root
