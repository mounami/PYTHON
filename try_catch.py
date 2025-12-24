try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except ValueError:
    # Runs if conversion to int fails
    print("That's not a valid number!")

except ZeroDivisionError:
    # Runs if dividing by zero
    print("Can't divide by zero!")

except Exception as e:
    # Catches any other error
    print(f"Unexpected error: {e}")

try:
    file = open("data.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File not found!")
    content = ""

else:
    # Runs if NO error occurred
    print("File loaded successfully!")

finally:
    # ALWAYS runs (even if error)
    print("Operation complete")
    if 'file' in locals():
        file.close()