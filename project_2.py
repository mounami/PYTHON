print("=====Character Stats=====")


player_name = input("Enter your player name: ")
player_character = input("Enter your character type (e.g., Warrior, Mage): ")

if player_character.lower() == "warrior":
    health = 150
    attack_power = 20
elif player_character.lower() == "mage":
    health = 50
    attack_power = 30
else:
    health = 100
    attack_power = 15

weapon = input("Choose your weapon (e.g., Sword, Staff): ")

if weapon.lower() == "sword":
    attack_power += 10
elif weapon.lower() == "staff":
    attack_power += 15
else:
    attack_power += 5

print("\n" + "="*30)
print("Character Summary:")

print(f"Player Name: {player_name}")
print(f"character Type: {player_character}")
print(f"Health: {health}")
print(f"Attack Power: {attack_power}")
print(f"Weapon: {weapon}")
print("="*30)

print(f"Armed with your {weapon}, you have {attack_power} attack power left!")
print(f"Good luck on your adventure, {player_name} the {player_character}!")
