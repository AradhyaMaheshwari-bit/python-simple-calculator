'''
pressed_<button_type> == GUI to calc
press_<button_type> == calc to calculator.py
'''

import tkinter as tk
from modules.calculator import Calculator
    # from tkinter import messagebox
    # import modules.operations

def create_app():

    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("420x320")
    root.resizable(False, False)
    calc = Calculator()

    def digit_pressed(digit):
        calc.press_digit(digit)
        display_text.set(calc.display)

    def clear_pressed():
        calc.press_clear()
        display_text.set(calc.display)

    def backspace_pressed():
        calc.press_backspace()
        display_text.set(calc.display)

    # ============
    # Display area
    # ============

    display_frame = tk.Frame(root)
    display_frame.pack(padx=20)

    display_text = tk.StringVar()
    display_entry = tk.Entry(
        display_frame,
        textvariable=display_text,
        width=30,
        justify="right",
        font=("Segoe UI", 16)
    )
    display_entry.grid(row=0, column=1, pady=5)
    display_text.set(calc.display)
    # ==============
    # Buttons area
    # ==============

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    clear_button = tk.Button(buttons_frame, text="AC", width=12, command=clear_pressed)
    backspace_button = tk.Button(buttons_frame, text="⌫", width=5, command=backspace_pressed)
    enter_button = tk.Button(buttons_frame, text="=", width=5)
    decimal_button = tk.Button(buttons_frame, text=".", width=5, command=lambda: digit_pressed("."))
    add_button = tk.Button(buttons_frame, text="+", width=5)
    subtract_button = tk.Button(buttons_frame, text="-", width=5)
    multiply_button = tk.Button(buttons_frame, text="×", width=5)
    divide_button = tk.Button(buttons_frame, text="÷", width=5)
    one_button = tk.Button(buttons_frame, text="1", width=5, command=lambda: digit_pressed("1"))
    two_button = tk.Button(buttons_frame, text="2", width=5, command=lambda: digit_pressed("2"))
    three_button = tk.Button(buttons_frame, text="3", width=5, command=lambda: digit_pressed("3"))
    four_button = tk.Button(buttons_frame, text="4", width=5, command=lambda: digit_pressed("4"))
    five_button = tk.Button(buttons_frame, text="5", width=5, command=lambda: digit_pressed("5"))
    six_button = tk.Button(buttons_frame, text="6", width=5, command=lambda: digit_pressed("6"))
    seven_button = tk.Button(buttons_frame, text="7", width=5, command=lambda: digit_pressed("7"))
    eight_button = tk.Button(buttons_frame, text="8", width=5, command=lambda: digit_pressed("8"))
    nine_button = tk.Button(buttons_frame, text="9", width=5, command=lambda: digit_pressed("9"))
    zero_button = tk.Button(buttons_frame, text="0", width=12, command=lambda: digit_pressed("0"))

    clear_button.grid(row=0, column=0, padx=0, columnspan=2)
    backspace_button.grid(row=0, column=2, padx=0)
    divide_button.grid(row=0, column=3, padx=0)
    seven_button.grid(row=1, column=0, padx=0)
    eight_button.grid(row=1, column=1, padx=0)
    nine_button.grid(row=1, column=2, padx=0)
    multiply_button.grid(row=1, column=3, padx=0)
    four_button.grid(row=2, column=0, padx=0)
    five_button.grid(row=2, column=1, padx=0)
    six_button.grid(row=2, column=2, padx=0)
    subtract_button.grid(row=2, column=3, padx=0)
    one_button.grid(row=3, column=0, padx=0)
    two_button.grid(row=3, column=1, padx=0)
    three_button.grid(row=3, column=2, padx=0)
    add_button.grid(row=3, column=3, padx=0)
    zero_button.grid(row=4, column=0, padx=0, columnspan=2)
    decimal_button.grid(row=4, column=2, padx=0)
    enter_button.grid(row=4, column=3, padx=0)

    return root
