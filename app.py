import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("420x320")
root.resizable(False, False)

# ===========
# Title area
# ===========

title_label = tk.Label(root, text="Simple Calculator")
title_label.pack(pady=15)

# ============
# Display area
# ============

display_frame = tk.Frame(root)
display_frame.pack(padx=20)

first_number_label = tk.Label(display_frame, text="First Number: ")
first_number_label.grid(row=0,column=0, pady=5, padx=5)

first_number_text = tk.StringVar()
first_number_entry = tk.Entry(display_frame, textvariable=first_number_text, width=20)
first_number_entry.grid(row=0, column=1, pady=5)
first_number_entry.focus()

second_number_label = tk.Label(display_frame, text="Second Number: ")
second_number_label.grid(row=1, column=0, pady=5, padx=5)

second_number_text = tk.StringVar()
second_number_entry = tk.Entry(display_frame, textvariable=second_number_text, width=20)
second_number_entry.grid(row=1, column=1, pady=5)

# ==============
# Operators area
# ==============

operator_frame = tk.Frame(root)
operator_frame.pack(pady=10)

add_button = tk.Button(operator_frame, text="+", width=5)
subtract_button = tk.Button(operator_frame, text="-", width=5)
multiply_button = tk.Button(operator_frame, text="×", width=5)
divide_button = tk.Button(operator_frame, text="÷", width=5)

add_button.grid(row=0, column=0, padx=5)
subtract_button.grid(row=0, column=1, padx=5)
multiply_button.grid(row=0, column=2, padx=5)
divide_button.grid(row=0, column=3, padx=5)

# ===========
# Result area
# ===========

result_frame = tk.Frame(root)
result_frame.pack(pady = 10)

result_label = tk.Label(result_frame, text="Result: ")
result_label.grid(row=0, column=0, padx=5)

result_value_text = tk.StringVar(value="0")
result_value_label = tk.Label(result_frame, textvariable=result_value_text)
result_value_label.grid(row=0, column=1, padx=5)

root.mainloop()
