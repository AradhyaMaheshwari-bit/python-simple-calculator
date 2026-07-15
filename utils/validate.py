def validate_menu_choice(choice):
    return choice in {"1", "2", "3", "4", "5"}

def validate_operands(a, b):
    try:
        float(a)
        float(b)
        return True
    except ValueError:
        return False

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False   
