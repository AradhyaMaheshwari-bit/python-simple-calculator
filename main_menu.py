import utils.validate
import modules.operations

menu_actions = {
    "1" : modules.operations.add,
    "2" : modules.operations.subtract,
    "3" : modules.operations.multiply,
    "4" : modules.operations.divide,
}

def print_main_menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main_menu():
    while True:
        print_main_menu()

        choice = input("Enter your choice: ")

        if not utils.validate.validate_menu_choice(choice):
            print("Please enter a valid choice (1-5): ")
            continue
        if choice == "5":
            print("Thank you for using the calculator!")
            break
        else:
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            if not utils.validate.validate_operands(a, b):
                print("Invalid input. Please enter numeric values.")
                continue
            a = float(a)
            b = float(b)
        try:
            result = menu_actions[choice](a, b)
            print(f"Result: {result}")
            print()
        except ZeroDivisionError as e:
            print(e)
