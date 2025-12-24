print("<=====Shopping cart application=====>")

cart = {}

cart["apple"] = 2.5
cart["banana"] = 1
cart["orange"] = 3
cart["Bread"] = 1

for item, quantity in cart.items():
    print(f"{item}: {quantity}")

# update cart

cart["banana"] = 1.2  # Update quantity of banana
cart["grape"] = 2.8   # Add new item grape
cart.pop("orange")  # Remove orange from cart

if "milk" in cart:
    print(f"Milk is in the cart: ${cart['milk']}")
else:
    print("Milk is not in the cart.Adding milk to the cart.")
    cart["milk"] = 2.0


print("\nUpdated cart:")
for item, quantity in cart.items():
    print(f"{item}: {quantity}")



