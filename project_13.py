print("🔢 BULLETPROOF CALCULATOR 🔢\n")

def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def calculate(num1, num2, operation):
    """Perform calculation with error handling"""
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return num1 / num2
        else:
            raise ValueError("Invalid operation")
    
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"

while True:
    print("\n=== Calculator ===")
    
    num1 = get_number("Enter first number: ")
    operation = input("Operation (+, -, *, /): ")
    num2 = get_number("Enter second number: ")
    
    result = calculate(num1, num2, operation)
    print(f"\nResult: {result}")
    
    again = input("\nCalculate again? (yes/no): ")
    if again.lower() != "yes":
        print("👋 Goodbye!")
        break