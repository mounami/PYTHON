import random
print("<========Castle hunt=============>")

character_name = input("Enter your character's name: ")
print(f"Welcome, {character_name}, to the castle hunt adventure!")

print("You find yourself at the entrance of a mysterious castle.")
choice_1 = input("Do you want to enter the castle through main entrance? (yes/no): ").lower()
choice_2 = input("Do you want to sneak around the back of the castle? (yes/no): ").lower()

if choice_1 == "yes":
    print("You bravely enter through the main entrance.")

    # sub choice
    guard_present = input("A guard is present. Do you want to fight or sneak past? (fight/sneak): ").lower()
    if guard_present == "fight":
        character_strength = random.randint(1, 10)
        guard_strength = random.randint(1, 10)

        if character_strength >= guard_strength:
            print("You fought valiantly and defeated the guard! You found a treasure chest inside the castle. You win!")
        else:
            print("The guard was too strong. You were captured. Game over.")
    elif guard_present == "sneak":
        print("You successfully sneaked past the guard but got lost in the castle. Game over.")
    else:
        print("Invalid choice. Game over.")
elif choice_2 == "no":
    print("You decided not to sneak around the back, found a gate that is locked.")

    found_key = input("Did you find the key? (yes/no): ").lower()
    if found_key == "yes":
        print("You unlocked the gate and entered the castle courtyard. You found a hidden treasure! You win!")
    else:
        print("Without the key, you couldn't enter the castle. Game over.")

else:
    print("Invalid choice. Game over.")