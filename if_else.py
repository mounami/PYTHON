age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote yet")

temp = float(input("Enter the temperature in celsius: "))

# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal
# <= less than or equal

if temp >= 30.0:
    print("It's a hot day!")
elif temp <= 25.0 and temp >= 18.0:
    print("It's a nice day!")
elif temp < 18.0 and temp >= 10.0:
    print("It's a bit chilly today.")
else:
    print("It's cold today!")

# Combining Conditions (and/or)

has_key = True
has_map = True

if has_key and has_map:
    print("You can enter the dungeon!")
elif has_key or has_map:
    print("You're missing something...")
else:
    print("You need both items!")