import random
print("<=====Dice game start=====>")

player_name = input("Enter your name: ")
print(f"Welcome, {player_name}, to the dice game!")

# STEP 1: Ask user how many dice to roll
dice_roll = int(input("How many times you wnt to roll the dice? "))

# Roll ONE six-sided die
# dice_num = random.randint(1, 6)
# STEP 2: Ask how many sides each die has
dice_num = int(input("How many sides you want for the dice? "))
# randint(1, 6) = pick random number from 1, 2, 3, 4, 5, or 6
# Example: User types "3"
# input() returns "3" as TEXT
# int() converts "3" to NUMBER 3
# Example: User types "6"
# Now we know: roll 3 dice, each with 6 sides (3d6)

print(f"{player_name} wants to roll {dice_roll}d{dice_num}!")
# This shows: "Rolling 3d6..." (game notation)

# STEP 3: Set up a counter for the total
total = 0
# We'll add each die roll to this

# STEP 4: Roll each die using a loop
for roll in range(dice_roll):
     # range(num_dice) = range(3) = [0, 1, 2]
    # So this loop runs 3 times
    
    # Roll ONE die
    roll_result = random.randint(1, dice_num)
       # First time: picks random from 1-6, maybe gets 4
    # Second time: picks random from 1-6, maybe gets 2
    # Third time: picks random from 1-6, maybe gets 5
    total += roll_result
     # Why i + 1? Because i is 0, 1, 2 but we want to show "Die 1, Die 2, Die 3"
    print(f"Roll {roll + 1}: {roll_result}")

print(f"Total score for {player_name} is: {total}")

if total >= (dice_roll * dice_num) / 2:
    print(f"Congratulations {player_name}, you win!")