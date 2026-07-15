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
        self.stored_value = None
        self.pending_operator = None
        self.waiting_for_new_number = False
    def press_digit(self, digit):
            if self.waiting_for_new_number:
                if digit == ".":
                    self.display = "0."
                else:
                    self.display = digit
                self.waiting_for_new_number = False
                return

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

    def press_clear(self):
        self.display = "0"
        self.stored_value = None
        self.pending_operator = None
        self.waiting_for_new_number = False

    def press_backspace(self):
        '''
        Rules:
        1. If the display is already "0" do nothing.
        2. Otherwise, remove the last character.
        3. After removing it, if the display becomes empty, replace it with "0"
        '''
        if self.display != "0":
            self.display = self.display[:-1]
        if self.display == "":
            self.display = "0"

    def press_operator(self, operator):
        self.stored_value = float(self.display)
        self.pending_operator = operator
        self.waiting_for_new_number = True


