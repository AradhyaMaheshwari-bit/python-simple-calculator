"""
Rules:
1. Replace the default zero
2. append the digit
3. append again
4. don't create leading zero
5. A decimal always needs a leading zero.
6. Only one decimal point is allowed in the current number.
"""


class Calculator:
    def __init__(self):
        self.display = "0"

    def press_digit(self, digit):
            if self.display == "0":
                if digit == ".":
                    self.display = "0."
                else:
                    self.display = digit
            else:
                if digit == ".":
                    if "." not in self.display:
                        self.display += digit
                else:
                    self.display += digit
