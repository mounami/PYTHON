car ={
    "brand":"Hyundai",
    "color":"Blue",
    "model":"i20",
    "year":2022
}

if "fuel" in car:
    print(f"The fuel type of car is: {car["fuel"]}")
else:
    print("Fuel type not specified.")

if "mileage" not in car:
    print("Mileage not specified.")

# looping through dict
# Loop 1: Just keys
for key in car.keys():
    print(f"Key: {key}")

for key in car:
    print(f"Key: {key}")

# Loop 2: Both key and values
for key in car:
    print(f"{key}: {car[key]}")

# Loop 3: Just values
for value in car.values():
    print(f"Value: {key}")

# Loop 4: Both key and values using items()
for key, value in car.items():
    print(f"{key}: {value}")

# Copying a dictionary
car_copy = car.copy()

print(car.keys())