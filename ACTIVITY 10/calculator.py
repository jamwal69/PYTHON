def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator(operator, x, y):
    switch = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide,
    }
    # Get the function from the dictionary
    operation = switch.get(operator, lambda: "Invalid operation")
    
    # Execute the function and return the result
    return operation(x, y)

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operator = input("Select operation (1, 2, 3, 4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = calculator(operator, num1, num2)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
