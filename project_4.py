print("Would you rather game!")

option_1_count = 0
option_2_count = 0
option_3_count = 0
option_4_count = 0


name = input("What is your name? ")
print(f"Welcome to the game, {name}!")
print("Would you rather...")
print("1. Be invisible")
print("2. Fly")
print("3. Read minds")
print("4. Be super strong")

choice = input("Enter the number of your choice: ")

if choice == "1":
    option_1_count += 1
elif choice == "2":
    option_2_count += 1
elif choice == "3":
    option_3_count += 1
elif choice == "4":
    option_4_count += 1
else:
    print("Invalid choice. Please choose a number between 1 and 4.")


if option_1_count > option_2_count and option_1_count > option_3_count:
    print(f"{name}, you chose to be invisible!")
elif option_2_count > option_1_count and option_2_count > option_3_count:
    print(f"{name}, you chose to fly!")
elif option_3_count > option_4_count and option_3_count > option_1_count:
    print(f"{name}, you chose to read minds!")
else:
    print(f"{name}, you chose to be super strong!")