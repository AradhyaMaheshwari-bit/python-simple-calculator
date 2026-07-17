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
    root.geometry("420x320")
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

    expression_label = tk.Label(display_frame, text="")
    expression_label.grid(row=0, column=1, pady=5)

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
        {"text": "AC", "type": "clear", "row": 0, "column": 0, "width": 12, "columnspan": 2},
        {"text": "⌫", "type": "backspace", "row": 0, "column": 2},
        {"text": "÷", "type": "operator", "row": 0, "column": 3},
        {"text": "7", "type": "digit", "row": 1, "column": 0},
        {"text": "8", "type": "digit", "row": 1, "column": 1},
        {"text": "9", "type": "digit", "row": 1, "column": 2},
        {"text": "×", "type": "operator", "row": 1, "column": 3},
        {"text": "4", "type": "digit", "row": 2, "column": 0},
        {"text": "5", "type": "digit", "row": 2, "column": 1},
        {"text": "6", "type": "digit", "row": 2, "column": 2},
        {"text": "-", "type": "operator", "row": 2, "column": 3},
        {"text": "1", "type": "digit", "row": 3, "column": 0},
        {"text": "2", "type": "digit", "row": 3, "column": 1},
        {"text": "3", "type": "digit", "row": 3, "column": 2},
        {"text": "+", "type": "operator", "row": 3, "column": 3},
        {"text": "0", "type": "digit", "row": 4, "column": 0, "width": 12, "columnspan": 2},
        {"text": ".", "type": "digit", "row": 4, "column": 2},
        {"text": "=", "type": "equal", "row": 4, "column": 3},
    ]

    def digit_pressed(digit):
        calc.press_digit(digit)
        update_display()

    def clear_pressed():
        calc.press_clear()
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

    for button in buttons:
        button_type = button["type"]
        button_text = button["text"]
        if button_type == "digit":
            command = lambda text=button_text: digit_pressed(text)
        elif button_type == "operator":
            command = lambda text=button_text: operator_pressed(text)
        elif button_type == "clear":
            command = clear_pressed
        elif button_type == "backspace":
            command = backspace_pressed
        elif button_type == "equal":
            command = equal_pressed
        tk.Button(buttons_frame, text=button_text, width=button.get("width", 5), command=command).grid(row=button["row"], column=button["column"], columnspan = button.get("columnspan", 1))

    return root
