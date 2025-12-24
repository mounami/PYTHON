# A list is a collection that can hold multiple items:

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 42, True, 3.14]  # Can mix types!
empty = []  # Empty list

# Accessing items by index (position)
print(fruits[0])  # First item: "apple"
print(fruits[1])  # Second item: "banana"
print(fruits[2])  # Third item: "orange"
# print(fruits[3])  # ERROR! Only 3 items (0, 1, 2)

# Negative indices (count from end)
print(fruits[-1])  # Last item: "orange"
print(fruits[-2])  # Second to last: "banana"

#  Adding items in list

fruits.append("grape")  # Add "grape" to end
print(fruits)  # Now: ["apple", "banana", "orange", "grape"]

fruits.insert(0, "kiwi")  # Insert "kiwi" at index 0
print(fruits)  # Now: ["kiwi", "apple", "banana", "orange", "grape"]

fruits.extend(["mango", "peach"])  # Add multiple items
print(fruits)  # Now has mango and peach at the end

new_fruits = fruits + ["pear", "plum"]  # Combine lists
print(new_fruits)  # New list with pear and plum


inventory = ["sword", "potion", "shield", "potion"]

# Remove by value (removes first occurrence)
inventory.remove("potion")  # Removes first "potion"
print(inventory)  # Now: ["sword", "shield", "potion"]

# Remove by index
inventory.pop(0)  # Removes "sword" at index 0
# pop() removes AND returns the item
print(inventory) 
# Remove last item
inventory.pop()  # Removes last item "potion"
print(inventory) 
# Clear entire list
inventory.clear()  # Now inventory is empty
print(inventory) 

# Looping through a list
colors = ["red", "green", "blue"]

for color in colors:
    print(color)

# Method 2: Loop with index numbers
for i in range(len(colors)):
    # len(fruits) = 4 (number of items)
    # range(4) = [0, 1, 2, 3]
    print(f"Color {i + 1}: {colors[i]}")

for index, color in enumerate(colors):
    print(f"Color {index + 1}: {color}")

# List operations

numbers = [10, 20, 30, 40, 50]

print(len(numbers))  # Number of items: 5
print(min(numbers))  # Smallest item: 10
print(max(numbers))  # Largest item: 50
print(sum(numbers))  # Sum of items: 150
print(sorted(numbers))  # Sorted list: [10, 20, 30, 40, 50]
numbers.sort()  # Sorts the list in place

if 30 in numbers:
    print("30 is in the list!")

print(numbers.index(40))  # Index of first occurrence of 40: 3
print(numbers.count(20))  # Count occurrences of 20: 1
numbers.reverse()  # Reverses the list
print(numbers)  # Now: [50, 40, 30, 20, 10]