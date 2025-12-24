car ={
    "brand": "Hyundai",
    "model": "i20",
    "year": 2022
}
print(f"First update: {car}")

car["colour"] = "Blue"
print(f"Second update: {car}")

car.update({"type": "Hatchback", "mileage": 15000})
print(f"Third update: {car}")

del car["mileage"]
print(f"Fourth update: {car}")

updated_card = car.pop("year")
print(f"Fifth update: {car}")

car.clear()
print(f"Final update: {car}")