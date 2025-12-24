print("<====Testing functions=======>")

def test():
    print("This is a test function.")

test()  # Call the test function

def add(name, age):
    print(f"Hello, {name}! You are {age} years old.")

add("Alice", 30)  # Call add function with arguments

def add_numbers(a, b):
    return a + b

add_numbers(5, 7)  # Call add_numbers but ignore return value
result = add_numbers(5, 7)  # Capture return value
print(f"The sum is: {result}")