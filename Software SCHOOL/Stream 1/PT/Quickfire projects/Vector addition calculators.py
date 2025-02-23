import math
def pythagoreanTherom(a, b):
    return (a**2 + b**2)**0.5
def trigFunctions(degrees):
    return (math.sin(math.radians(degrees)), math.cos(math.radians(degrees)), math.tan(math.radians(degrees)))
def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")
            if operation == '+':
                return num1 + num2
            elif operation == '-':
                return num1 - num2
            elif operation == '*':
                return num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                return num1 / num2
            else:
                raise invalidInput
        except ValueError:
            print("Invalid input, please enter numeric values.")
        except invalidInput:
            print("Invalid operation, please enter one of +, -, *, /.")
        except ZeroDivisionError as e:
            print(e)
class invalidInput(Exception):pass
while True:    
    while True:
        try:
            function = input("Which Function? ")
            if function == "0" or function == "1":
                function = int(function)
                break
            elif function == "c":
                break
            raise invalidInput
        except invalidInput:
            print("Invalid input")
    if function == 0:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print(pythagoreanTherom(a, b))
    elif function == 1:
        degrees = float(input("Enter degrees: "))
        print(f"Sin: %s, Cos: %s, Tan: %s" % trigFunctions(degrees))
    elif function == "c":
        print(calculator())