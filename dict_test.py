# Creating a dictionary
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Lists = Ordered, access by position (index)

person = ["John", 25, "New York"]
# Which is which? Confusing!
print(person[0])  # John - but you need to remember position


# Dictionaries = Unordered, access by meaningful key
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print(person["name"])  # Clear! You know what you're getting


# Empty dictionary
empty_dict ={}

# Adding key-value pairs
test_data ={
    "name": "Alice",
    "age": 30,
    "ready": True,
    "items": ["item1", "item2", "item3"]

}

# accessing values using square brackets
print(test_data["name"])
print(test_data["items"])

# accessing values using get() method
print(test_data.get("age"))

#  with default value
print(test_data.get("address", "Not Available"))  # Key doesn't exist

# This CRASHES if key doesn't exist:
print(test_data["phone"])  # KeyError: 'phone' ❌

# This returns None (safe):
print(test_data.get("phone"))  # None ✅