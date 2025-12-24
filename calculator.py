"""
Simple Calculator Project
A basic calculator that performs arithmetic operations
"""

def add(a, b):
    """
    Add two numbers
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second number
    
    Args:
        a (float): Numerator
        b (float): Denominator
    
    Returns:
        float: Quotient of a and b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return a / b


def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("       SIMPLE CALCULATOR")
    print("="*40)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("="*40)


def get_numbers():
    """
    Get two numbers from user input
    
    Returns:
        tuple: Two numbers entered by user
    """
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter valid numbers.")


def main():
    """Main function to run the calculator"""
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("\nInvalid choice! Please select a valid option.")
            continue
        
        num1, num2 = get_numbers()
        
        try:
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"\n{e}")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()