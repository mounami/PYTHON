import random

print("🔮 MAGIC 8-BALL 🔮")
print("Ask me a yes/no question...")

answers = ["Yes, definitely!",      # Item 0
    "It is certain.",        # Item 1
    "Without a doubt.",      # Item 2
    "Ask again later.",      # Item 3
    "Cannot predict now.",   # Item 4
    "Don't count on it.",    # Item 5
    "My sources say no.",    # Item 6
    "Outlook not so good."   # Item 7
]

while True: # True = loop forever (until we break out)
    question = input("Your question: ")

    # Check if user wants to quit
    if question.lower() in ["exit", "quit"]: # .lower() makes it work for "QUIT" or "Quit" too
        print("Goodbye!")
        break # break = exit the loop
    response = random.choice(answers)




print("\n🔮", response)