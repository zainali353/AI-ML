
# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
def pow(a,b):
    return a**b



# Main calculator function
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operator = input("Choose (+, -, *, /,**): ")

        if operator == "+":
            result = add(num1, num2)

        elif operator == "-":
            result = subtract(num1, num2)

        elif operator == "*":
            result = multiply(num1, num2)

        elif operator == "/":
            result = divide(num1, num2)
        elif operator=="**":
            result=pow(num1,num2)

        else:
            print("Invalid operator!")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers!")


calculator()
