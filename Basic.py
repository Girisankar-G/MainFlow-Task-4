"""
Command-Line Calculator in Python:
    * A command-line calculator allows users to perform arithmetic operations directly from the terminal.
    * The calculator will support basic operations like addition, subtraction, multiplication, and division.
"""

# Defining functions for basic arithmetic operations
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
        return "Error: Division by zero"

"""
User Interface Design:
    * The calculator will interact with the user through the terminal.
    * The input function will be used to gather user input for the operation and numbers.
"""

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Options: 1. Add  2. Subtract  3. Multiply  4. Divide")
    
    # Getting user choice and validating it
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        # Getting numbers from the user and validating the input
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            return "Invalid input! Please enter numeric values."

        # Performing the chosen operation
        if choice == '1':
            result = add(num1, num2)
            operation = "addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "division"
        
        print(f"The result of the {operation} is: {result}")
    else:
        print("Invalid choice! Please select a valid operation.")

# Running the calculator function
calculator()
