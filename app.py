import tkinter as tk
from tkinter import messagebox
import modules.operations
import utils.validate

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("420x320")
root.resizable(False, False)

def calculate(operation):
    a = first_number_text.get().strip()
    b = second_number_text.get().strip()

    if not utils.validate.is_number(a):
            messagebox.showerror("Error", "First number must be numeric.")
            first_number_text.set("")
            first_number_entry.focus()
            result_value_text.set("0")
            return
    if not utils.validate.is_number(b):
            messagebox.showerror("Error", "Second number must be numeric.")
            second_number_text.set("")
            second_number_entry.focus()
            result_value_text.set("0")
            return

    a = float(a)
    b = float(b)
    try:
        result = operation(a,b)
        result_value_text.set(result)
    except ZeroDivisionError as e:
        messagebox.showerror("Error", f"{e}")
        second_number_text.set("")
        second_number_entry.focus()
        result_value_text.set("0")

def clear():
    first_number_text.set("")
    second_number_text.set("")
    result_value_text.set("0")
    first_number_entry.focus()

# ===========
# Title area
# ===========

title_label = tk.Label(root, text="Simple Calculator", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=15)

# ============
# Display area
# ============

display_frame = tk.Frame(root)
display_frame.pack(padx=20)

first_number_label = tk.Label(display_frame, text="First Number: ", font=("Segoe UI", 10))
first_number_label.grid(row=0,column=0, pady=5, padx=5)

first_number_text = tk.StringVar()
first_number_entry = tk.Entry(display_frame, textvariable=first_number_text, width=24)
first_number_entry.grid(row=0, column=1, pady=5)
first_number_entry.focus()

second_number_label = tk.Label(display_frame, text="Second Number: ", font=("Segoe UI", 10))
second_number_label.grid(row=1, column=0, pady=5, padx=5)

second_number_text = tk.StringVar()
second_number_entry = tk.Entry(display_frame, textvariable=second_number_text, width=24)
second_number_entry.grid(row=1, column=1, pady=5)

# ==============
# Operators area
# ==============

operator_frame = tk.Frame(root)
operator_frame.pack(pady=10)

add_button = tk.Button(operator_frame, text="+", width=5, command=lambda: calculate(modules.operations.add))
subtract_button = tk.Button(operator_frame, text="-", width=5, command=lambda: calculate(modules.operations.subtract))
multiply_button = tk.Button(operator_frame, text="×", width=5, command=lambda: calculate(modules.operations.multiply))
divide_button = tk.Button(operator_frame, text="÷", width=5, command=lambda: calculate(modules.operations.divide))
clear_button = tk.Button(operator_frame, text="C", width=3,height=2, command=clear, font=("", 12))

add_button.grid(row=0, column=0, padx=5)
subtract_button.grid(row=1, column=0, padx=5)
multiply_button.grid(row=0, column=1, padx=5)
divide_button.grid(row=1, column=1, padx=5)
clear_button.grid(row=0, column=3, padx=5, rowspan=2)

# ===========
# Result area
# ===========

result_frame = tk.Frame(root)
result_frame.pack(pady = 10)

result_label = tk.Label(result_frame, text="Result: ", font=("Segoe UI", 12, "bold"))
result_label.grid(row=0, column=0, padx=5)

result_value_text = tk.StringVar(value="0")
result_value_label = tk.Label(result_frame, textvariable=result_value_text, font=("Segoe UI", 12, "bold"))
result_value_label.grid(row=0, column=1, padx=5)

root.mainloop()
