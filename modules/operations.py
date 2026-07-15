def add(a, b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
        if a==0:
            raise ZeroDivisionError("Result is undefined")
        else:
            raise ZeroDivisionError("Cannot divide by zero")
    return a/b

