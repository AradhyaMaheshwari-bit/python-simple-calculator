"""
Rules:
1. Replace the default zero
2. append the digit
3. append again
4. don't create leading zero
5. A decimal always needs a leading zero.
6. Only one decimal point is allowed in the current number.
"""
import modules.operations

class Calculator:
    def __init__(self):
        self.display = "0"
        self.stored_value = None
        self.pending_operator = None
        self.waiting_for_new_number = False
        self.error_state = False
        self.expression = ""
        self.last_operator = None
        self.last_operand = None

    def press_digit(self, digit):
            if self.error_state:
                self.press_clear()

            if self.waiting_for_new_number:
                if self.stored_value is None:
                    self.expression = ""
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
        self.error_state = False
        self.expression = ""
        self.last_operator = None
        self.last_operand = None

    def press_clear_entry(self):
        self.display = "0"
        self.error_state = False

    def press_backspace(self):
        '''
        Rules:
        1. If the display is already "0" do nothing.
        2. Otherwise, remove the last character.
        3. After removing it, if the display becomes empty, replace it with "0"
        '''
        if self.error_state:
                self.press_clear()
        if self.display != "0":
            self.display = self.display[:-1]
        if self.display == "":
            self.display = "0"
        if self.pending_operator is None:
            self.expression = ""

    def press_operator(self, operator):
        if self.error_state:
            return
        if self.stored_value is None:
            self.stored_value = float(self.display)
        elif self.waiting_for_new_number:
            pass
        else:
            self._evaluate_pending_operation()
        self.pending_operator = operator
        self.waiting_for_new_number = True
        self.expression = f"{self._format_result(self.stored_value)} {self.pending_operator}"

    def _evaluate_pending_operation(self):
        if self.pending_operator == "+":
            result = modules.operations.add(self.stored_value, float(self.display))
        elif self.pending_operator == "-":
            result = modules.operations.subtract(self.stored_value, float(self.display))
        elif self.pending_operator == "×":
            result = modules.operations.multiply(self.stored_value, float(self.display))
        elif self.pending_operator == "÷":
            result = modules.operations.divide(self.stored_value, float(self.display))
        self.display = self._format_result(result)
        self.stored_value = result

    def press_equal(self):
        if self.error_state:
                self.press_clear()
        if self.pending_operator is not None:
            self.expression = f"{self._format_result(self.stored_value)} {self.pending_operator} {self.display} ="
            self.last_operator = self.pending_operator
            self.last_operand = float(self.display)
            self._evaluate_pending_operation()
        elif self.last_operator is not None:
            self.stored_value = float(self.display)
            self.pending_operator = self.last_operator
            self.display = self._format_result(self.last_operand)
            self.expression = f"{self._format_result(self.stored_value)} {self.pending_operator} {self.display} ="
            self._evaluate_pending_operation()
        self.stored_value = None
        self.pending_operator = None
        self.waiting_for_new_number = True

    def _format_result(self, result):
        if result.is_integer():
            return str(int(result))
        else:
            return str(result)
